import subprocess
def cmd(commands:[], cwd=None):
    try:
        return subprocess.run(commands, cwd=cwd, check=True)
    except subprocess.CalledProcessError as e:
        print("Error: can't execute command: %s" % commands)
        print(e)

def check_cmd(commands:[], cwd=None):
    try:
        return subprocess.check_output(commands, cwd=cwd)
    except subprocess.CalledProcessError as e:
        print("Error: can't execute command: %s" % commands)
        print(e)
        return False