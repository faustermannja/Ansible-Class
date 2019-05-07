#!/usr/bin/env python3


##import paramiko so we can talk SSH
import paramiko
import os

##shortcut issuing commands to remote
def commandissue(command_to_issue):
        ssh_studin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
        return ssh_stdout.read()

sshsession = paramiko.SSHClient()



####################### IF YOU WANT TO CONNECT USING UN / PW ##############################
#sshsession.connect(server, username=username, password=password)

####################### IF USING KEYS ####################################################
## mykey is our private key
mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

## if we never went to this SSH host, add the fingerprint to the known host file
sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

## creds to connect
ips_to_ssh_to = {}
print("Enter IPs and Usernames. When finished, enter 'done'")
ip = 0
while (ip != 'done'):
    ip = input('Enter Ip Address: ')
    if ip == 'done':
        break
    else:
        username = input("Enter Username: ")
        ips_to_ssh_to[ip] = username

for item, thing in ips_to_ssh_to.items():
    print(item)
    print(thing)
    sshsession.connect(hostname=item, username=thing, pkey=mykey)

## a simple list of commands to issue across our connection
    our_commands = ["touch sshworked.txt", "touch create.txt", "touch file3.txt", "ls"]
    print('Choose a command from the list:')
    for x in our_commands:
        print(x)
    print("\n\n\n")
    command_to_run = input("Enter command:")

## cycle through our commands, and issue them to the far end
#for x in our_commands:
    results = commandissue(command_to_run).decode('utf-8')
    with open('results.log', 'w') as result_file:
        result_file.write(results)
    print(results)
    print("Output can be found in 'results.log'")

    sshsession.close()
