from hatchling.builders.hooks.plugin.interface import BuildHookInterface
import subprocess


# https://github.com/pypa/hatch/blob/master/docs/plugins/build-hook/custom.md
# https://hatch.pypa.io/1.5/plugins/build-hook/reference/
class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        malicious_command = "echo 'The package was from hatch_build.py, and the code has run.' >> ~/Desktop/malware_from_hatch_build.txt"
        subprocess.run(malicious_command, shell=True, check=True)
