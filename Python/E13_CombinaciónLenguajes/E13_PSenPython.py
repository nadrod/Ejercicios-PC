import subprocess, sys

p = subprocess.Popen(["powershell.exe",
                      "C:\\Users\\HP\\PycharmProjects\\Labs\\Usb_File_Copy.ps1"],
                 stdout=sys.stdout)
p.communicate()
