import paramiko

# Define the file, destination, and command to be used
file = input("Enter the file name: ")
destination = input("Enter the destination path: ")
command = input("Enter the command to run: ")

# Open the file containing the IP addresses
with open("ip.txt", "r") as f:
    ip_addresses = f.readlines()

# Create an SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Loop over the IP addresses
for ip in ip_addresses:
    ip = ip.strip()
    try:
        # Connect to the IP address
        client.connect(ip, username='YOUR_USERNAME', password='YOUR_PASSWORD')
        sftp = client.open_sftp()
        # Transfer the file
        sftp.put(file, destination)
        sftp.close()
        # Run the command
        stdin, stdout, stderr = client.exec_command(command)
        print(f'Successful connect and file transfer to {ip}')
    except Exception as e:
        print(f'Error connecting to {ip}: {e}')
    finally:
        client.close()

