# STOP/DJVU Ransomware Vaccine
 
Prevents STOP/DJVU Ransomware from encrypting your files.
This tool does not prevent the infection itself. STOP ransomware may still place ransom notes and may change settings on the systems. 
But STOP ransomware will not encrypt files anymore if the system has the vaccine.

* Instead of a personal ID, ransom notes will contain a string that files were protected by the vaccine.
* Files that have a size of 5 bytes or less will still be renamed by the ransomware, but stay unchanged apart from that. This is because the ransomware starts encryption at the 6th byte. So I guess STOP thinks those files were successfully encrypted and hence renames them.

**Notes:** Vaccines in general work by adding harmless parts of a malware to the system to trick it into believing the system is already infected. Antivirus software may detect the vaccine.

The vaccine may not work for future versions of this ransomware.
So if you already take the time to apply it, also take the time to backup your files!

**Authors:** Karsten Hahn, John Parol @ GDATA CyberDefense

**Tested versions:** STOP/DJVU Ransomware versions from August 2019 to Dec 2021
If you want a sample to test, you can download one from here: https://bazaar.abuse.ch/sample/e28fad4106120da332e8bbcd7288373ae7035654f54faf52abbfa51b6fdbd996/
