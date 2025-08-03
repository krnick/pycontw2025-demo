import subprocess
import os

curl_url = "curl https://tw.pycon.org/2025/zh-hant/conference/talk/332 > this_talk.html"

subprocess.run(curl_url, shell=True, check=True)

# Determine the command to open the file based on the operating system
if os.name == 'nt':  # 'nt' is for Windows
    cmd = "start this_talk.html"
elif os.name == 'posix':  # 'posix' is for macOS and Linux
    cmd = "open this_talk.html"
else:
    cmd = ""
    print("Cannot identify the operating system, please open this_talk.html manually.")

if cmd:
    subprocess.run(cmd, shell=True, check=True)
