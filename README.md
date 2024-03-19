SSH Password Cracker
This Python script is created to perform a brute-force attack on an SSH server using the paramiko library. 
The script retrieves users on a specified IP address and attempts an SSH connection for each user using a provided password list.

In this script, the paramiko library is utilized to establish SSH connections and execute commands on the remote server. 
The script first connects to the SSH server using the provided credentials. 
Then, it retrieves a list of users from the /etc/passwd file. 
For each user, the script attempts to connect using passwords from the provided list until a successful connection is established or all passwords are exhausted.
