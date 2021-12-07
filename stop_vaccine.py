# STOP/DJVU Vaccine
# Prevents STOP/DJVU Ransomware from encrypting your files
# Note: This may not work for future versions of this ransomware
# So backup your files!
#
# Authors: Karsten Hahn, John Parol @ GDATA CyberDefense
# Twitter: @struppigel

import ctypes
import win32con, win32api
import os

vaccine_file = os.path.join(os.getenv('LOCALAPPDATA'), 'bowsakkdestx.txt')	
IDYES = 6

def already_vaccinated():
	return os.path.isfile(vaccine_file)

def nothing_done_msg():
	ctypes.windll.user32.MessageBoxW(0, "Nothing was changed", "STOP/DJVU Vaccine", 0)

def user_consent():
	answer = ctypes.windll.user32.MessageBoxW(0, "This will apply a vaccine for STOP/DJVU to your system. Please note that vaccines use harmless parts of the actual malware to make the malware believe it already infected the system. This may cause antivirus products to believe your system is infected by STOP. Continue anyways?", "STOP DJVU Vaccine", 4)
	if answer == IDYES:
		return True
	else: 
		return False

def vaccinate():		
	try:
		vaccine_content = b"\x7B\x22\x70\x75\x62\x6C\x69\x63\x5F\x6B\x65\x79\x22\x3A\x22\x74\x68\x69\x73\x20\x69\x73\x20\x61\x20\x76\x61\x63\x63\x69\x6E\x65\x20\x64\x6F\x20\x6E\x6F\x74\x20\x72\x65\x6D\x6F\x76\x65\x22\x2C\x22\x69\x64\x22\x3A\x22\x20\x59\x6F\x75\x20\x77\x65\x72\x65\x20\x70\x72\x6F\x74\x65\x63\x74\x65\x64\x20\x62\x79\x20\x53\x54\x4F\x50\x20\x76\x61\x63\x63\x69\x6E\x65\x22\x7D"
		with open(vaccine_file, 'wb') as f:
			f.write(vaccine_content)
		win32api.SetFileAttributes(vaccine_file, win32con.FILE_ATTRIBUTE_HIDDEN)
		ctypes.windll.user32.MessageBoxW(0, "Your system is vaccinated!", "STOP/DJVU Vaccine", 0)
	except:
		ctypes.windll.user32.MessageBoxW(0, "Something went wrong while trying to vaccinate your system", "STOP/DJVU Vaccine", 0)
	
if __name__ == "__main__":
	if already_vaccinated():
		answer = ctypes.windll.user32.MessageBoxW(0, "Your system is already vaccinated or has had a not fully cleaned STOP infection. Continue anyways?", "STOP/DJVU Vaccine", 4)
		if answer == IDYES:
			os.remove(vaccine_file)
			if user_consent():
				vaccinate()
			else:
				nothing_done_msg()
		else:
			nothing_done_msg()
	else: 
		if user_consent():
			vaccinate()
		else:
			nothing_done_msg()
