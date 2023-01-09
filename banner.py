#Adding neccessary imports
import os
import re

def grabbanner():
	
	#Asking User for IP & Port
	print("Please input an IPv4 address and the port you wish to use." + "\n")
	
	print("IP: ")
	ip = input()
	
	#Using Regex to insure that it is a valid IP"
	validip = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
	
	if(re.search(validip, ip)):
		pass
	else:
		print("Invalid IP")
		exit()
		
	print("\n" + "Port: ")
	port = input()

	#Using Regex to insure that it is a valid Port"
	validport = "^([1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$"
	  
	if(re.search(validport, port)):
		pass
	else:
		print("Invalid Port")
		exit()
	
	print("\n")

	#Running Nmap command with given IP & Port <- returning results & printing out to user
	cmd = "nmap -sV -p " + port + " --script=banner " + ip
	process = os.popen(cmd)
	results = str(process.read())
	
	return results
	   
print(grabbanner())