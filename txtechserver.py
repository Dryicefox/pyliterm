do = True
import getpass
currentdir = "l"
name = input("root@10.160.1.251: ")
server = ['ls', 'ssh root@10.160.1.244']

if name in server:
	currentdir = "server1"

if currentdir == "server1":
	print("Hint.txt, PW.docx, ClassSchedule.csv, ReadMe.txt")
while do == True:
	newname = input("root@10.160.1.251: ").split()
	if newname[0] == "less":
		if newname[1]== "ReadMe.txt":
			print("For your security, you will not be able to see yourself type")
			password = getpass.getpass("*Document Locked* - Enter Password: ")
			if password == "raiderpower":
				print("Welcome new faculty! To get to your email server, connect via the admin account located at 10.160.1.32")
			else:
				print("******************************************ACCESS DENIED******************************************")
				import txtechserver
		if newname[1] == "Hint.txt":
			 print("""			Dear Dr.S,

			In case you forget your password, like normal, What is the cheer you and I participated in with the whole crowd at our favorite past time last saturday?
			Remember, all lowercase, all one word.
			Cant wait to see you in class tomorrow :)

			Love, Lacie""")
		if newname[1] == "PW.docx":
			 print("This is File 2")
		if newname[1] == "ClassSchedule.csv":
			 print("Notes from IT: To connect to the faculty list, SSH into 10.160.1.244")
	if newname[0] =="ls":
		print("Hint.txt, PW.docx, ClassSchedule.csv, ReadMe.txt")
	if newname[0] =="ssh":
		if newname[1] =="root@10.160.1.244":
			import pylifac
			do = False
		if newname[1] =="admin@10.160.1.32":
			import pylimailserver
			do = False
	if newname[0] =="exit":
		##from pyliterm.py import cd():
		do = False

##import pylifac
