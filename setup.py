# This is an educational and demonstration example to showcase common malicious code
# techniques used in malware written in Python, aiming for a talk at PyCon Taiwan 2025.
# Talk URL: https://tw.pycon.org/2025/zh-hant/conference/talk/332
# WARNING: The code is not malicious, but please do not run it in a production environment.
import subprocess

from setuptools import setup, find_packages
from setuptools.command.install import install

print("--- from setup.py ---")
malicious_command = "echo 'This package is malicious!' > malware_from_install.txt"
subprocess.run(malicious_command, shell=True, check=True)
print(f"Executing malicious command: {malicious_command}")


class MaliciousInstallCommand(install):
    def run(self):
        print("--- from setup.py MaliciousInstallCommand(install) install hijacking ---")
        malicious_install_cmd = "echo 'hijacking install!' > malware_from_hijacking_install.txt"
        subprocess.run(malicious_install_cmd, shell=True)
        print(f"Executing malicious command: {malicious_install_cmd}")

        install.run(self)


setup(
    name='malicious-package',
    version='0.0.1',
    description='A seemingly harmless Python package.',
    packages=find_packages(),
    cmdclass={
        'install': MaliciousInstallCommand
    },
    entry_points={
        'console_scripts': [
            'cli-tool=malicious_package.cli:run_malicious_command_line_tool',
        ],
    },

)