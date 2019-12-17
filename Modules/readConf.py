import os
from pathlib import Path
conf_file = str(Path(__file__).parent.parent) + "/config.conf"

#checking if directory path is exist and create subdirectory if needed
def checkDir(dir_path):
    DocDir = os.path.join(dir_path,"TelDocuments")
    PhoDir = os.path.join(dir_path,"TelPhotos")
    ScrDir = os.path.join(dir_path,"TelScreenShots")
    VidDir = os.path.join(dir_path,"TelVideos")
    AuiDIR = os.path.join(dir_path,"TelAudio")

    if os.path.isdir(dir_path):

        if os.path.isdir(DocDir):pass
        else:os.mkdir(DocDir)

        if os.path.isdir(PhoDir):pass
        else:os.mkdir(PhoDir)

        if os.path.isdir(ScrDir):pass
        else:os.mkdir(ScrDir)

        if os.path.isdir(VidDir):pass
        else:os.mkdir(VidDir)

        if os.path.isdir(AuiDIR):pass
        else:os.mkdir(AuiDIR)

    else:
        return False

    return os.path.abspath(PhoDir),os.path.abspath(VidDir),os.path.abspath(AuiDIR),os.path.abspath(DocDir),os.path.abspath(ScrDir)






def readingConf():
    """Reading conf file - output order --> photo_dir , video_dir , document_dir , screenshot_dir , process_time_out , audio_dir , telegram token api , UserName"""
    with open(conf_file,"r") as conFile:
        file_path = ""
        photo_dir = ""
        video_dir = ""
        audio_dir = ""
        document_dir = ""
        screenshot_dir = ""
        process_time_out = ""
        token = ""
        userN = ""

        opened_file = conFile.readlines()
        for line in opened_file:
            if line.startswith("#"):
                pass
            elif len(line) == 0:
                pass
            elif str(line) == "\n":
                pass
            else:
                parameter = (line.split("=")[0]).split(" ")[0]
                value = (line.split("=")[1]).split(" ")[1]
                
                if parameter == "WorkingFileDir":
                    file_path = value.split('"')[1]
                    if not checkDir(file_path):
                        print("Directory not found")
                        return False
                    else:
                        photo_dir,video_dir,audio_dir,document_dir,screenshot_dir = checkDir(file_path)

                elif parameter == "ProcessTimeOut":
                    try:
                        process_time_out = int(value)
                    except:
                        print("Invalid process timeout")
                        return False

                elif parameter == "Token":
                    try:
                        token = str(value)
                    except:
                        print("Error getting token from config file")
                        return False

                elif parameter == "UserName":
                    try:
                        if len(value) == 0:
                            print("Username is empty!!")
                            return False
                        elif value.startswith("@"):
                            userN = value[1:]
                        else:
                            userN = str(value)
                    except:
                        print("Error getting username from config file")
                        return False

        return photo_dir,video_dir,audio_dir,document_dir,screenshot_dir,process_time_out,token.rstrip(),userN.rstrip()

