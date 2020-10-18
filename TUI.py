import os
import getpass

def reset():
	os.system("tput setab 8 && clear && tput setaf 10")
	print("\t\t\tTUI (Terminal User Interface)\n")
	os.system("tput setaf 14")
def out():
	input("\n\t Press ENTER to continue..........")
	os.system("tput setaf 7 && tput setab 0 && clear")
	exit()

reset()
password = getpass.getpass()
apass='sts'
if password != apass:
	print("Authentication Failure!")
	out()

reset()
location=input("Where do you want to run this job (local/remote):")


if location=='local':
	print("You are now running on Local System")
	
	while True:
		print("""\n
		1. Current Date & Time
		2. Calender of Current Month
		3. Add User to this OS
		4. Make Directory
		5. Make File
		99. Exit""")

		opt=input("Enter your choice: ")
		opt=int(opt)

		if opt == 1:
			os.system("date")
		elif opt == 2:
			os.system("cal")
		elif opt == 3:
			usrnm=input("Enter username: ")
			os.system("adduser {}".format(usrnm))
		elif opt == 4:
			dirnm=input("Enter Directory name: ")
			os.system("mkdir {}".format(dirnm))
		elif opt == 5:
			filenm=input("Enter File name: ")
			os.system("vim {}".format(filenm))
		elif opt == 99:
			break
		else:
			print("Invalid Input")
		input("\n\t Press ENTER to continue..........")
		reset()

elif location=='remote':
	remoteIP=input("Enter ip-address of the remote system: ")
	print("You are now running on remote System")
	sshcmd=("ssh {}".format(remoteIP))
	
	while True:
		print("""\n
		1. Current Date & Time
		2. Calender of Current Month
		3. Add User to this OS
		4. Make Directory
		5. Make File
		99. Exit""")

		opt=input("Enter your choice: ")
		opt=int(opt)

		if opt == 1:
			os.system(sshcmd+" date")
		elif opt == 2:
			os.system(sshcmd+" cal")
		elif opt == 3:
			usrnm=input("Enter username: ")
			os.system(sshcmd+" adduser {}".format(usrnm))
		elif opt == 4:
			dirnm=input("Enter Directory name: ")
			os.system(sshcmd+" mkdir {}".format(dirnm))
		elif opt == 5:
			filenm=input("Enter File name: ")
			os.system(sshcmd+" vim {}".format(filenm))
		elif opt == 99:
			break
		else:
			print("Invalid Input")
		input("\n\t Press ENTER to continue..........")
		reset()

else:
	print("Invalid Option")

out()
