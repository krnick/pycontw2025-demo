import subprocess

from setuptools import setup, find_packages
from setuptools.command.install import install

print("--- print from setup.py ---")
malicious_command = "echo 'This package is malicious!' > malware_from_install.txt"
subprocess.run(malicious_command, shell=True, check=True)
print(f"Executing malicious command: {malicious_command}")


class MaliciousInstallCommand(install):
    def run(self):
        print("--- print from python setup.py install hijacking ---")
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
            'my-cli-tool=malicious_package.main:run_malicious_command_line_tool',
        ],
    },

)
