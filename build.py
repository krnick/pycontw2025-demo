# This is an educational and demonstration example to showcase common malicious code
# techniques used in malware written in Python, aiming for a talk at PyCon Taiwan 2025.
# Talk URL: https://tw.pycon.org/2025/zh-hant/conference/talk/332
# WARNING: The code is not malicious, but please do not run it in a production environment.

import subprocess


def build():
    """
    This function is Poetry's build hook, automatically called before the packaging process begins.
    Here we demonstrate malicious code that executes a shell command.
    """
    malicious_command = "echo 'The package was from build.py via pyproject.toml, and the code has run.' >> ~/Desktop/malware_from_build_py.txt"
    subprocess.run(malicious_command, shell=True, check=True)


if __name__ == "__main__":
    build()
