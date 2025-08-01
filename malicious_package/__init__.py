import subprocess

print("--- print from malicious_package/__init__.py ---")
malicious_command = "echo 'The package was imported, and the code has run.' >> malware_from_import.txt"
print(f"Executing malicious command: {malicious_command}")
subprocess.run(malicious_command, shell=True, check=True)
