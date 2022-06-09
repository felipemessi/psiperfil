import subprocess


def start():
    cmd = ["python", "manage.py", "runserver", "0.0.0.0:8000"]
    subprocess.run(cmd)

def dev():
    cmd = ["python", "manage.py", "runserver", "--settings=settings.local.py"]
    subprocess.run(cmd)