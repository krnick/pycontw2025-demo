import subprocess


def run_malicious_command_line_tool():
    print("--- print from console_scripts ---")
    malicious_command = "echo 'The command line tool was executed.' >> malware_from_command_line.txt"
    subprocess.run(malicious_command, shell=True, check=True)
    print(f"Executing malicious command: {malicious_command}")