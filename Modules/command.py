import subprocess,os

#Import custom modules
from Modules.readConf import readingConf
timeOut = readingConf()[5]#getting time out value from config file


#send command to OS and answer result
def runCommand(update, context):
    msg = update.message.text
    ret = executeCommand(msg)
    context.bot.send_message(chat_id=update.message.chat_id,text=ret,reply_to_message_id=int(update.message.message_id))


#execute command in OS
def executeCommand(comm):
    if comm[:2] == "cd":#change directory
        try:
            os.chdir(comm[3:])
            return os.getcwd()
        except: return "Invalid path"
    elif comm == "pwd":
        return os.getcwd()
    else:
        try:
            proccess=subprocess.Popen(comm, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE ,stdin=subprocess.PIPE)
            proccess.wait(timeout=int(timeOut))
            result=proccess.stdout.read() + proccess.stderr.read()
            return result.decode('utf-8')
        except:
            return f"Process timeout\nThis error happen because the process can't return any out put\nTime out: {str(timeOut)}"
            
