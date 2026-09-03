import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class SecurityEventHander(FileSystemEventHandler):
    def on_modified(self, event):
        # Log the modification event
        print(f"Security alert: File {event.src_path} has been modified.")

    def on_created(self, event): 
        # Log creation event
        if 'log' in event.src_path:
            return
        print("Security alert: New file created at {}".format(event.src_path))

    def on_deleted(self, event):
        # Log deletion event
        print(f'Security alert: File deleted from {event.src_dir}')

def start_monitoring(path_to_watch):
    event_handler = SecurityEventHandlder()
    observer = Observer()

    observer.schedule(event_handler, path=path_to_watch, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    path_to_watch = '/path/to/your/directory'
    start_monitoring('/path/to/monitor')
