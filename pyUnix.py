import os

def cls():

	#This clears the screen

	os.system('cls')

inShell = 0

#This allocates the items into their specified directories

root = "/dev\n/boot\n/pac\n/home\n/credits"

dev = "/vmi"

boot = "/shell\n/com"

pac = "/pdev\n/pgen\n/poth"

credits = "credits.txt\nlicense.txt"

vmi = "vInfo.txt\nvName.txt"

shell = "1st.txt\n2nd.txt"

com = "comInfo.txt"

pdev = "neofetch"

pgen = "cat"

poth = "credits"

#This defines what's in all the text files

creditsTxt = "Made by god_king_nahrwal(Scratch) in Python with Vscode by Microsoft and some help from w3schools."

license = "You can redistribute this if you make modifications and provide credit to all parties used to make this and modify it."

vInfo = "Running pyUnix v1.0.0\nRam: 32gb\nCpu: 2.10 GHz\nGpu: 16.9gb\nssd: 2TB"

comInfo = "pyUnix is running in a VM, no PC info is available"

first = "inShell = 1\n\ninitmfs()\ncom.start\npromt()"

second = "import os\n\ndef cls():\n\n   os.system('cls')\n\nname = input('Name: ')\n\nhost = input('PC name: ')\n\ninShell = 0"

README = "Welcome to pyUnix, a mock operating system made in python based on Unix and Linux.\nAll the info you need to know regarding navigating this operating system can be accessed using the 'help' command."

#This edits the help instructions

help = "pwd - prints the working directory\n   ex - pwd\ncd - change directories\n   ex - cd /dev\nls - lists a directories contents\n   ex - ls\ncredits - shows the credits\n   ex - credits\ncat - reads a file as long as it's in your current directory\n   ex - cat license.txt\ncd .. takes you up in the file system\n   ex - if you're in /dev/vmi and you use cd .. you'll go to /dev\nshutdown - shuts the vm down\n   ex - shutdown\nclear - clears the screen\n   ex - clear\nneofetch - prints OS information\n   ex - neofetch\ndu - shows how much space the specified file is taking up\n   ex - du vInfo.txt\npcrn - renames your PC after you type it and press enter\n   ex - pcrn\nwhoami - prints your username\n   ex - whoami\nuname - prints the OS name\n   ex - uname\n\nItems in a directory starting with '/' are directories"

cls()

#This prompts you for your name and PC name

name = input("Name: ")

home = "/"+name

cd = home	

cls()

host = input("PC name: ")

#This sets the virtual machines name to the PC's name and the user's name

vName = host + "\n" + name

dis = "~"

nameDir = "README.txt"

#Sets the version number

version = "v1.0.0"

inShell = 1

cls()

#Initial message

print("Type 'help' for a list of commands")

while inShell:
	
	answer = input(name + "@" + host + dis + ": ")
	
	if answer == "help":
		
		cls()
		
		print(help + "\n")
	
	#Sets the directory

	if answer == "cd /":
		
		cd = root
		dis = "/"

	if answer == "cd /dev":
		
		if dis == "/":

			cd = dev
			dis = "/dev"
	
	if answer == "cd /boot":
		
		if dis == "/":

			cd = boot
			dis = "/boot"

	if answer == "cd /pac":
		
		if dis == "/":

			cd = pac
			dis = "/pac"
	
	if answer == "cd /credits":
		
		if dis == "/":

			cd = credits
			dis = "/credits"
	
	if answer == "cd /dev/vmi":
		
		cd = vmi
		
		dis = "/dev/vmi"

	if answer == "cd /vmi":
		
		if dis == "/dev":
			
			cd = vmi
			
			dis = "/dev/vmi"
	
	if answer == "cd /boot/shell":
		
		cd = shell
		dis = "/boot/shell"

	if answer == "cd /shell":
		
		if dis == "/boot":
			
			cd = shell
			dis = "/boot/shell"

	if answer == "cd /boot/com":
		
		cd = com
		dis = "/boot/com"

	if answer == "cd /com":
		
		if dis == "/boot":
			
			cd = com
			dis = "/boot/com"

	if answer == "cd /pac/pdev":
		
		cd = pdev
		dis = "/pac/pdev"

	if answer == "cd /pdev":
		
		if dis == "/pac":
			
			cd = pdev
			dis = "/pac/pdev"

	if answer == "cd /pac/pgen":
		
		cd = pgen
		dis = "/pac/pgen"

	if answer == "cd /pgen":
		
		if dis == "/pac":
			
			cd = pgen
			dis = "/pac/pgen"

	if answer == "cd /pac/poth":
		
		cd = poth
		dis = "/pac/poth"

	if answer == "cd /poth":
		
		if dis == "/pac":
			
			cd = poth
			dis = "/pac/poth"

	if answer == "cd /home":

		if dis == "/":

			cd = home
			dis = "/home"

		if dis == "/home/"+name:

			cd = home
			dis = "/home"

	if answer == "cd /home/"+name:
		
		cd = nameDir
		dis = "/home/"+name

	if answer == "cd /"+name:

		if dis == "/home":

			cd = nameDir
			dis = "/home/"+name

	if answer == "pwd":
		
		print(dis)

	if answer == "ls":
		
		print(cd)

	#Goes up a directory

	if answer == "cd ..":
		
		if cd == dev:

			cd  = root
			dis = "/"
			
		if cd == boot:

			cd = root
			dis = "/"

		if cd == pac:

			cd = root
			dis = "/"

		if cd == credits:

			cd = root
			dis = "/"
		
		if cd == vmi:

			cd = dev
			dis = "/dev"

		if cd == shell:

			cd = boot
			dis = "/boot"

		if cd == com:

			cd = boot
			dis = "/boot"

		if cd == pdev:

			cd = pac
			dis = "/pac"

		if cd == pgen:

			cd = pac
			dis = "/pac"

		if cd == poth:

			cd = pac
			dis = "/pac"

		if cd == nameDir:

			cd = home
			dis = "~"

		if cd == home:

			if dis == "~":

				cd = home
				dis = "/home"


	if answer == "cat credits.txt":

		if cd == credits:

			print(creditsTxt)

	if answer == "cat license.txt":

		if cd == credits:

			print(license)

	if answer == "cat vInfo.txt":

		if cd == vmi:

			print(vInfo)

	if answer == "cat vName.txt":

		if cd == vmi:

			print(vName)


	if answer == "cat 1st.txt":

		if cd == shell:

			print(first)

	if answer == "cat 2nd.txt":

		if cd == shell:

			print(second)

	if answer == "cat comInfo.txt":

		if cd == com:

			print(comInfo)

	if answer == "cat README.txt":

		if cd == nameDir:

			print(README)

	if answer == "credits":
		
		print(creditsTxt)

	if answer == "shutdown":

		print("pyUnix.shutdown")

		cls()

		quit()
	
	if answer == "clear":

		cls()
	
	if answer == "neofetch":

		print("          .?77777777777777$.             "+name+"@"+host)
		print("          777..777777777777$+             --------------")
		print("         .77    7777777777$$$             OS: pyUnix "+version)
		print("         .777 .7777777777$$$$             Host: pyUnix Virtual Machine")
		print("         .7777777777777$$$$$$             Kernel: "+version)
		print("         ..........:77$$$$$$$             Uptime: N/A")
		print("  .77777777777777777$$$$$$$$$.=======.    Packages: 3")
		print(" 777777777777777777$$$$$$$$$$.========    Shell: pyUnix built-in shell")
		print("7777777777777777$$$$$$$$$$$$$.=========   Terminal: /boot/shell")
		print("77777777777777$$$$$$$$$$$$$$$.=========   CPU: pyUnix vCPU (4) @ 2.10 GHz")
		print("777777777777$$$$$$$$$$$$$$$$ :========+.  Memory: 32 gb")
		print("77777777777$$$$$$$$$$$$$$+..=========++~")
		print("777777777$$..~=====================+++++")
		print("77777777$~.~~~~=~=================+++++.")
		print("777777$$$.~~~===================+++++++.")
		print("77777$$$$.~~==================++++++++: ")
		print(" 7$$$$$$$.==================++++++++++. ")
		print(" .,$$$$$$.================++++++++++~.  ")
		print("         .=========~.........           ")
		print("         .=============++++++           ")
		print("         .===========+++..+++           ")
		print("         .==========+++.  .++           ")
		print("          ,=======++++++,,++,           ")
		print("          ..=====+++++++++=.            ")
		print("                ..~+=...                ")

	if answer == "pcrn":
		
		host = input("New name: ")

	if answer == "du vInfo.txt":
		if dis == "/dev/vmi":
			print("7     vInfo.txt")

	if answer == "du vName.txt":
		if dis == "/dev/vmi":
			print("4     vName.txt")

	if answer == "du 1st.txt":
		if dis == "/boot/shell":
			print("7     1st.txt")

	if answer == "du 2nd.txt":
		if dis == "/boot/shell":
			print("15     2nd.txt")

	if answer == "du comInfo.txt":
		if dis == "/boot/com":
			print("11     comInfo.txt")

	if answer == "du README.txt":
		if dis == "/home/"+name:
			print("19     README.txt")

	if answer == "du credits.txt":
		if dis == "/credits":
			print("9     credits.txt")

	if answer == "du license.txt":
		if dis == "/credits":
			print("10     license.txt")

	if answer == "whoami":
		print(name)

	if answer == "uname":
		print("pyUnix")

	

# men kisser code above /\
		