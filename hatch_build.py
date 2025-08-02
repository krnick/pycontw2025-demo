from hatchling.builders.hooks.plugin.interface import BuildHookInterface
import subprocess


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        print("--- from hatch_build.py ---")
        malicious_command = "echo 'The package was by hatch, and the code has run.' >> malware_from_hatch_build.txt"
        subprocess.run(malicious_command, shell=True, check=True)
