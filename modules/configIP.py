import commands as cm
import os

def run(**args):
	if os.name=='nt':
		ipData = cm.getoutput("ipconfig")
		return str(ipData)
	else:
		ipData = cm.getoutput("ifconfig")
		return str(ipData)
	
	return
