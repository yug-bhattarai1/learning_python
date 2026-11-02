import requests

def basic_auth_request(username, password):
    r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=(f'{username}', f'{password}'))

    if r.status_code == 200:
        print("Authentication successful!")
    else:
        print("Authentication failed. Please check your username and password.")

    
username = input("Enter username: ")
password = input("Enter password: ")
basic_auth_request(username, password)
