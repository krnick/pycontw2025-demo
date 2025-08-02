from hatchling.builders.hooks.plugin.interface import BuildHookInterface
import subprocess


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        malicious_command = "echo 'The package was from hatch_build.py, and the code has run.' >> ~/Desktop/malware_from_hatch_build.txt"
        subprocess.run(malicious_command, shell=True, check=True)
