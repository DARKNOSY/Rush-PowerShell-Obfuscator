#https://github.com/DARKNOSY/Rush-PowerShell-Obfuscator, made by DARKN0$Y

import os
import base64
import requests

def print_header():
    header_text = f"Rush PowerShell Obfuscator by @DARKNOSY - Stars: {stars_count}, Forks: {forks_count}, Watchers: {watchers_count}"
    console_width = os.get_terminal_size().columns
    padding_width = (console_width - len(header_text)) // 2
    header_line = "=" * console_width
    print("\033[1m")  # Bold text
    print("\033[95m" + header_line)
    print("\033[94m" + " " * padding_width + header_text + " " * padding_width)
    print("\033[95m" + header_line + "\033[0m")
    print("\033[0m")  # Reset text style

def print_success(message):
    print("\033[92m" + message + "\033[0m")

def print_error(message):
    print("\033[91m" + message + "\033[0m")

# Function to obfuscate the script content 'n' times
def obfuscate_script(script_content, n):
    encoded_script = base64.b64encode(script_content.encode()).decode()
    for i in range(1, n+1):
        print(f"Obfuscation Layer {i}/{n}")
        script_content = f'''# Obfuscated using https://github.com/DARKNOSY/Rush-PowerShell-Obfuscator, made by DARKN0$Y

$decodedScript = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String(@"
{encoded_script}
"@))
Invoke-Expression -Command $decodedScript
'''
        encoded_script = base64.b64encode(script_content.encode()).decode()
    return script_content

def get_stats():
    global stars_count, forks_count, watchers_count

    username = "DARKNOSY"
    repo_name = "Rush-PowerShell-Obfuscator"
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        repo_data = response.json()
        stars_count = repo_data["stargazers_count"]
        forks_count = repo_data["forks_count"]
        watchers_count = repo_data["watchers_count"]

    else:
        print("Failed to fetch repository details.")

# Set the console title
print("\033]0;Rush PowerShell Obfuscator by DARKNOSY\007")

get_stats()

# Display the header with the repository counts
print_header()

# Ask the user for the path to the original PowerShell script
original_script_path = input("\033[96mDrag powershell script here:\033[0m ")

# Read the content of the original script
with open(original_script_path, 'r') as file:
    original_script_content = file.read()

# Ask the user how many times they want to obfuscate the script
num_obfuscations = int(input("\033[96mEnter the number of times to obfuscate the script:\033[0m "))

# Obfuscate the script 'num_obfuscation' times
obfuscated_script_content = obfuscate_script(original_script_content, num_obfuscations)

# Get the folder path of the original script
folder_path, file_name = os.path.split(original_script_path)

# Create the path for the obfuscated script in the same folder
obfuscated_script_path = os.path.join(folder_path, f"OBF_{file_name}")

# Save the obfuscated script to the specified path
with open(obfuscated_script_path, 'w') as file:
    file.write(obfuscated_script_content)

print_success("\nObfuscation completed.")
print_success(f"Obfuscated script saved to: \033[96m{obfuscated_script_path}\033[0m")

# Credits to username "DARKNOSY" for the obfuscator
print("\n\033[93mThanks for using Rush PowerShell Obfuscator!")
print("GitHub Repository: https://github.com/DARKNOSY/Rush-PowerShell-Obfuscator\033[0m")

# Keep the console open after completing the obfuscation
input("\nPress Enter to exit...")
