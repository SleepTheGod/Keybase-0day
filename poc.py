```py
#!/usr/bin/env python3

import requests

def get_user_info(username):
    url = f"https://keybase.io/_/api/1.0/getsalt.json?email_or_username={username}&generate_hmac_pwh(password,%20salt,%20login_session)"
    response = requests.get(url)
    data = response.json()
    return data

def print_user_info(username):
    user_info = get_user_info(username)
    if 'salt' in user_info:
        print("Username:", username)
        print("Salt:", user_info['salt'])
        print("Login Session:", user_info['login_session'])
        print("UID:", user_info['uid'])
        print("CSRF Token:", user_info['csrf_token'])
    else:
        print("Failed to retrieve information for username:", username)

def main():
    # Prompt the user to enter the target username
    target_username = input("Enter the target username to look up: ")

    # Retrieve and print information for the target username
    print_user_info(target_username)

if __name__ == "__main__":
    # Check if script is being run as root
    import os
    if os.geteuid() != 0:
        print("Please run this script as root.")
        exit(1)

    main()
```
