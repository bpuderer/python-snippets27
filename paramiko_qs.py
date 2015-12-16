import paramiko

paramiko.util.log_to_file('paramiko_qs.log')

ssh = paramiko.SSHClient()

ssh.load_system_host_keys()
#only use the following line if you trust the server you're connecting to
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


ssh.connect('192.168.1.100', username='usr1', password='pswd')
stdin, stdout, stderr = ssh.exec_command('whoami')
lines = stdout.readlines()
ssh.close()
for line in lines:
    print line.strip('\n')


ssh.connect('192.168.1.100', username='usr1', password='pswd')
stdin, stdout, stderr = ssh.exec_command('sudo -S whoami')
stdin.write('supswd'+'\n')
stdin.flush()
lines = stdout.readlines()
ssh.close()
for line in lines:
    print line.strip('\n')
