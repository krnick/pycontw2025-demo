# This is an educational and demonstration example to showcase common malicious code
# techniques used in malware written in Python, aiming for a talk at PyCon Taiwan 2025.
# Talk URL: https://tw.pycon.org/2025/zh-hant/conference/talk/332
# WARNING: The code is not malicious, but please do not run it in a production environment.

__version__ = "0.0.1"

import subprocess

print("--- from malicious_package/__init__.py ---")
malicious_command = "echo 'The package was imported, and the code has run.' >> malware_from_import.txt"
print(f"Executing malicious command: {malicious_command}")
subprocess.run(malicious_command, shell=True, check=True)
