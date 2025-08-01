# This is an educational and demonstration example to showcase common malicious code
# techniques used in malware written in Python, aiming for a talk at PyCon Taiwan 2025.
# Talk URL: https://tw.pycon.org/2025/zh-hant/conference/talk/332
# WARNING: The code is not malicious, but please do not run it in a production environment.

import subprocess


def run_malicious_command_line_tool():
    print("--- from malicious_package/cli.py ---")
    malicious_command = "echo 'The command line tool was executed.' >> malware_from_command_line.txt"
    subprocess.run(malicious_command, shell=True, check=True)
    print(f"Executing malicious command: {malicious_command}")
