from hashlib import sha256
import platform,os,sys



#rebooting functions ------------------------------ start ------------------------------
def rebooting():
    osName = platform.system()
    if osName.startswith("Windows"):
        os.system("shutdown /r /t 0")
    elif osName.startswith("Linux") or osName.startswith("Darwin"):
        os.system("sudo reboot now")


def rebootFunc(update,context):
    with open("passwd.sha256","r") as passwd_file:
        hash_pass = passwd_file.readline()
        pass_prompt = update.message.text
        new_pass_hash = sha256(pass_prompt.encode("utf-8")).hexdigest()
        if str(hash_pass) == str(new_pass_hash):
            context.bot.send_message(chat_id=update.message.chat_id,text="Rebooting system")
            rebooting()
        else:
            context.bot.send_message(chat_id=update.message.chat_id,text="Invalid password")
#rebooting functions ------------------------------ end ------------------------------



#shutting down functions ------------------------------ start ------------------------------
def shuttingDown():
    osName = platform.system()
    if osName.startswith("Windows"):
        os.system("shutdown /s /t 0")
    elif osName.startswith("Linux") or osName.startswith("Darwin"):
        os.system("sudo shutdown -h now")


def shutdownFunc(update,context):
    with open("passwd.sha256","r") as passwd_file:
        hash_pass = passwd_file.readline()
        pass_prompt = update.message.text
        new_pass_hash = sha256(pass_prompt.encode("utf-8")).hexdigest()
        if str(hash_pass) == str(new_pass_hash):
            context.bot.send_message(chat_id=update.message.chat_id,text="shutting down system")
            shuttingDown()
        else:
            context.bot.send_message(chat_id=update.message.chat_id,text="Invalid password")
#shutting down functions ------------------------------ end ------------------------------



#killing functions ------------------------------ start ------------------------------
def killing():
    osName = platform.system()
    if osName.startswith("Windows"):
        os.system(f'taskkill /F /PID {os.getpid()}')
    elif osName.startswith("Linux") or osName.startswith("Darwin"):
        os.system('kill %d' % os.getpid())


def killOwnPro(update , context):
    with open("passwd.sha256","r") as passwd_file:
        hash_pass = passwd_file.readline()
        pass_prompt = update.message.text
        new_pass_hash = sha256(pass_prompt.encode("utf-8")).hexdigest()
        if str(hash_pass) == str(new_pass_hash):
            context.bot.send_message(chat_id=update.message.chat_id,text="Killing own proccess")
            killing()
        else:
            context.bot.send_message(chat_id=update.message.chat_id,text="Invalid password")
#killing functions ------------------------------ start ------------------------------
