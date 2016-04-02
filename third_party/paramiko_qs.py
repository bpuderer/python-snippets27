import paramiko


paramiko.util.log_to_file('paramiko_qs.log')

client = paramiko.SSHClient()
client.load_system_host_keys()
#only use the following line if you trust the server you're connecting to
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect('192.168.1.100', username='usr1', password='pswd')

# I/O streams returned as file-like objects
stdin, stdout, stderr = client.exec_command('ls -l')

#print stdout.readlines()
for line in stdout:
    print line.strip('\n')

client.close()


client.connect('192.168.1.100', username='usr1', password='pswd')
stdin, stdout, stderr = client.exec_command('sudo -S whoami')
stdin.write('supswd'+'\n')
stdin.flush()
for line in stdout:
    print line.strip('\n')
client.close()


########################################


#write file, existing file trunc'd
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('192.168.1.100', username='usr1', password='pswd')

sftp_client = ssh_client.open_sftp()
remote_file = sftp_client.open('/tmp/sftptest.log', mode='w')

remote_file.write("first line in sftptest.log since mode='w' truncates an existing file\n")

remote_file.close()
sftp_client.close()
ssh_client.close()

#---------------------

#append to file
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('192.168.1.100', username='usr1', password='pswd')

sftp_client = ssh_client.open_sftp()
remote_file = sftp_client.open('/tmp/sftptest.log', mode='a')

remote_file.writelines(["line appended to sftptest.log since mode='a'\n", "another line appended to sftptest.log\n"])

remote_file.close()
sftp_client.close()
ssh_client.close()

#---------------------

#reading
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('192.168.1.100', username='usr1', password='pswd')

sftp_client = ssh_client.open_sftp()
#mode='r' for reading is the default
remote_file = sftp_client.open('/tmp/sftptest.log')

file_contents = remote_file.readlines()
print file_contents

remote_file.close()
sftp_client.close()
ssh_client.close()

#----------------

#remove
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('192.168.1.100', username='usr1', password='pswd')

sftp_client = ssh_client.open_sftp()
sftp_client.remove('/tmp/sftptest.log')

sftp_client.close()
ssh_client.close()
