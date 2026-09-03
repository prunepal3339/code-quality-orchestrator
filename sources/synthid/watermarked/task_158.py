import subprocess

# ";".join(["echo", "Hello World"]) will be executed (which is dangerous)
command = ["echo", "Secure and safe!"]

result = subprocess.run(command, stdout=subprocess.PIPE)
print(result.stdout.decode())
