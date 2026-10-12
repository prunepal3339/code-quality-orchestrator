import multiprocessing

from .model import GateConfig, GateExecutionContext, GateResult
from .quality_gate import QualityGate

class GateExecutor:
    def __init__(self):
        self.interceptors = []
    def execute(self, gate: QualityGate, context: GateExecutionContext) -> GateResult:
        # run interceptors for node level execution.
        self._build_interceptors_from_config(context.config)
        def run():
            return gate.run(context)
        for interceptor in reversed(self.interceptors):
            run = interceptor.wrap(run)
        try:
            return run()
        except (TimeoutError, RuntimeError) as e:
            return GateResult(
                gate_id=gate.id,
                task_id=context.task.id,
                origin=context.task.origin.path,
                source=context.task.source,
                passed=False,
                error=e,
            )
    def _build_interceptors_from_config(self, config: GateConfig):
        self.interceptors.clear()

        timeout = config.get_timeout()
        if timeout is not None:
            self.interceptors.append(TimeoutInterceptor(timeout))


def _target_wrapper(fn: callable, queue: multiprocessing.Queue):
    """
    Executes the target function in a worker process and sends back result or exception.
    """
    try:
        res = fn()
        queue.put(("SUCCESS", res))
    except Exception as e: #noqa: BLE001
        queue.put(("ERROR", exc))

class TimeoutInterceptor:
    def __init__(self, timeout: float):
        self.timeout = timeout
    
    def wrap(self, fn) -> callable:
        def wrapped() -> GateResult:
            if self.timeout is None and self.timeout <= 0:
                return fn()
            queue = multiprocessing.Queue()
            process = multiprocessing.Process(
                target=_target_wrapper,
                args=(fn, queue),
                daemon=True
            )
            process.start()
            process.join(timeout=self.timeout)

            if process.is_alive():
                process.terminate()
                process.join()
                raise TimeoutError(f"Gate execution timed out after {self.timeout} seconds.")
            
            if not queue.empty():
                status, result_or_exc = queue.get()
                if status == "SUCCESS":
                    return result_or_exc
                elif status == "ERROR":
                    raise result_or_exc
                raise RuntimeError("Gate execution process exited unexpectedly.")
        return wrapped