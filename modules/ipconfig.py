import commands as cm
import os

def run(**args):
	if os.name=='nt':
		print ("[*] In ipconfig module.")
		ipData = cm.getoutput("ipconfig")
		return str(ipData)
	else:
		print ("[*] In ipconfig module.")
		ipData = cm.getoutput("ifconfig")
		return str(ipData)
	
	return
