#!/usr/bin/env python3


## moving files with SFTP

##import paramiko so we can talk SSH
import paramiko
import os
ip = 0
def movethemfiles(remote, location):
    ## iterate across the files within directory
    for x in os.listdir('/home/student/Ansible-Class/filestocopy/'): # iterate on directory contents
        if not os.path.isdir("/home/student/Ansible-Class/filestocopy/" + x): # filter everything that is NOT a directory
            remote.put("/home/student/Ansible-Class/filestocopy/" + x, location + '/' + x) # move file to target location
         
    
print("Enter IP Address, Username, and Password. Type Done in 'IP Address' when finished.")
while (ip != 'done'):
    try:     
         ## where to connect to
         ip = input("Enter IP Address: ")
         if ip != 'done':
             t = paramiko.Transport(ip, 22) ## IP and Port
         else:
             break
         
         ## how to connect (see other labs on using id_rsa private / public keypairs)
         usn = input("Enter Username: ")
         pwd = input("Enter Password: ")
         loc = input("Enter directory to place files: ")
         t.connect(username = usn, password = pwd)
         
         ## make an sftp conneciton object
         sftp = paramiko.SFTPClient.from_transport(t)

         movethemfiles(sftp, loc)        
                 
         ## close the connection
         sftp.close() # close the connection
    except:
        if sftp:
            sftp.close()
