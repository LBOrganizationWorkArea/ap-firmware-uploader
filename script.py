import nmap
import os
import sys
firmware=sys.argv[1]
# send command to cmd
print("FIRMWARE OTA : " + firmware)
string = "poetry run ap-uploader " +  " " + (firmware)
os.system('cmd /k '+string)


