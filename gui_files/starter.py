import subprocess
import os
import time

def start_spring_boot():
    jar_path = "kompress-0.0.1-SNAPSHOT.jar"
    return subprocess.Popen(["java", "-jar", jar_path])

def start_tkinter_gui():
    os.system("python3 ui.py")

if __name__ == "__main__":
    spring_boot_process = start_spring_boot()
    time.sleep(2)
    start_tkinter_gui()
    spring_boot_process.wait()
