from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import telegram
import datetime
from mss import mss
import platform
import os
from pathlib import Path


#Change to working dir
workingDirPath = Path(__file__).parent
os.chdir(workingDirPath)


#checking config file
print("\nReading config file .....")
from Modules.readConf import readingConf
if not readingConf():
    print("error reading config file")
    exit(1)
else:
    ScreenShotDir = readingConf()[4]
    UserNameID = readingConf()[7]
    TelegramToken = readingConf()[6]




#importing custom modules
from Modules.command import runCommand,executeCommand
from Modules.download import photo_downloader,document_downloader,video_downloader,audio_downloader
from Modules.upload import photo_uploader,video_uploader,document_uploader,audio_uploader
from Modules.power import rebootFunc,shutdownFunc,killOwnPro


#get username that can connect to bo
available_username = f"@{UserNameID}"



#getting OS information
os_type = f"{platform.system()} {platform.release()}"




#connect to telegram API ----------------------------- start -----------------------------
print("Connecting to telegram API .....")
try:
    telegram.Bot(token=TelegramToken).get_me()
    updater = Updater(token=TelegramToken, use_context=True)
    dispatcher = updater.dispatcher
except:
    print("Invalid telegram Token")
    exit(1)

#connet to telegram API ----------------------------- end -----------------------------




#Disable all active handlers ----------------------------- start -----------------------------

command_handler_status = False
download_handler_status = False
download_handler_status_file = False
upload_handler_status = False
upload_handler_status_file = False
restart_handler_status = False
turnOff_handler_status = False
kill_msg_handle_status = False

def disable_all_handlers():
    global command_handler_status,download_handler_status,download_handler_status_file,upload_handler_status,upload_handler_status_file,restart_handler_status,turnOff_handler_status,kill_msg_handle_status


    if command_handler_status:
        dispatcher.remove_handler(recCommand_handler)
        command_handler_status = False

    if download_handler_status:
        dispatcher.remove_handler(rec_download)
        download_handler_status = False

    if download_handler_status_file:
        dispatcher.remove_handler(getting_files)
        download_handler_status_file = False
    
    if upload_handler_status:
        dispatcher.remove_handler(rec_upload)
        upload_handler_status = False

    if upload_handler_status_file:
        dispatcher.remove_handler(getting_upload_files)
        upload_handler_status_file = False

    if restart_handler_status:
        dispatcher.remove_handler(restart_handler)
        restart_handler_status = False

    if turnOff_handler_status:
        dispatcher.remove_handler(turnOff_handler)
        turnOff_handler_status = False

    if kill_msg_handle_status:
        dispatcher.remove_handler(kill_msg_handle)
        kill_msg_handle_status = False

#Disable all active handlers ----------------------------- end -----------------------------





#Download functions ----------------------------- start -----------------------------

#check download file
def downloader(update, context):
    global getting_files,download_handler_status_file

    def disable_built_in_handlers():
        global download_handler_status_file
        if download_handler_status_file:
            dispatcher.remove_handler(getting_files)
            download_handler_status_file = False
        
    reply_num = update.message.text

    if int(reply_num) == 1:
        disable_built_in_handlers()
        context.bot.send_message(chat_id=update.message.chat_id,text="Upload your photo", reply_to_message_id=update.message.message_id)
        download_handler_status_file = True
        getting_files = MessageHandler(Filters.photo, photo_downloader)
        dispatcher.add_handler(getting_files)


    if int(reply_num) == 2:
        disable_built_in_handlers()
        context.bot.send_message(chat_id=update.message.chat_id,text="Upload your video", reply_to_message_id=update.message.message_id)
        download_handler_status_file = True
        getting_files = MessageHandler(Filters.video, video_downloader)
        dispatcher.add_handler(getting_files)


    if int(reply_num) == 3:
        disable_built_in_handlers()
        context.bot.send_message(chat_id=update.message.chat_id,text="Upload your audio", reply_to_message_id=update.message.message_id)
        download_handler_status_file = True
        getting_files = MessageHandler(Filters.audio, audio_downloader)
        dispatcher.add_handler(getting_files)


    if int(reply_num) == 4:
        disable_built_in_handlers()
        context.bot.send_message(chat_id=update.message.chat_id,text="Upload your file", reply_to_message_id=update.message.message_id)
        download_handler_status_file = True
        getting_files = MessageHandler(Filters.document, document_downloader)
        dispatcher.add_handler(getting_files)

#Download functions ----------------------------- end -----------------------------




#Upload functions ----------------------------- start -----------------------------

#check upload file
def uploader(update, context):
    global getting_upload_files,upload_handler_status_file

    def disable_built_in_handlers_upload():
        global upload_handler_status_file
        if upload_handler_status_file:
            dispatcher.remove_handler(getting_upload_files)
            upload_handler_status_file = False
        
    reply_num_upload = update.message.text

    if int(reply_num_upload) == 1:
        disable_built_in_handlers_upload()
        context.bot.send_message(chat_id=update.message.chat_id,text="Enter your photo file path: ", reply_to_message_id=update.message.message_id)
        upload_handler_status_file = True
        getting_upload_files = MessageHandler(Filters.all, photo_uploader)
        dispatcher.remove_handler(rec_upload)
        upload_handler_status = False
        dispatcher.add_handler(getting_upload_files)


    if int(reply_num_upload) == 2:
        disable_built_in_handlers_upload()
        context.bot.send_message(chat_id=update.message.chat_id,text="Enter your video file path: ", reply_to_message_id=update.message.message_id)
        upload_handler_status_file = True
        getting_upload_files = MessageHandler(Filters.all, video_uploader)
        dispatcher.remove_handler(rec_upload)
        upload_handler_status = False
        dispatcher.add_handler(getting_upload_files)


    if int(reply_num_upload) == 3:
        disable_built_in_handlers_upload()
        context.bot.send_message(chat_id=update.message.chat_id,text="Enter your audio file path: ", reply_to_message_id=update.message.message_id)
        upload_handler_status_file = True
        getting_upload_files = MessageHandler(Filters.all, audio_uploader)
        dispatcher.remove_handler(rec_upload)
        upload_handler_status = False
        dispatcher.add_handler(getting_upload_files)


    if int(reply_num_upload) == 4:
        disable_built_in_handlers_upload()
        context.bot.send_message(chat_id=update.message.chat_id,text="Enter your document file path: ", reply_to_message_id=update.message.message_id)
        upload_handler_status_file = True
        getting_upload_files = MessageHandler(Filters.all, document_uploader)
        dispatcher.remove_handler(rec_upload)
        upload_handler_status = False
        dispatcher.add_handler(getting_upload_files)

#Upload functions ----------------------------- end -----------------------------




#Base command functions & handlers ----------------------------- start -----------------------------

#Functions------------------------------------------------------------------------
#starting bot Func
def start(update, context):
    disable_all_handlers()
    username = str(update.message.chat.first_name) + " " + str(update.message.chat.last_name)
    showRes = f"Welcome to *LUCID* bot 😊 \nName: {username}\nOS: {os_type.replace('Darwin','Mac OS')}"
    context.bot.send_message(chat_id=update.message.chat_id,text=showRes,parse_mode=telegram.ParseMode.MARKDOWN)

#Kill process Func
def killItSelf(update,context):
    disable_all_handlers()
    global kill_msg_handle,kill_msg_handle_status
    context.bot.send_message(chat_id=update.message.chat_id,text="Enter password: ")
    kill_msg_handle_status = True
    kill_msg_handle = MessageHandler(Filters.text,killOwnPro)
    dispatcher.add_handler(kill_msg_handle)


#restart OS Func
def restartOS(update, context):
    disable_all_handlers()
    global restart_handler,restart_handler_status
    context.bot.send_message(chat_id=update.message.chat_id,text="Enter password: ")
    restart_handler_status = True
    restart_handler = MessageHandler(Filters.text,rebootFunc)
    dispatcher.add_handler(restart_handler)


#shutdown OS Func
def shutdownOS(update, context):
    disable_all_handlers()
    global turnOff_handler,turnOff_handler_status
    context.bot.send_message(chat_id=update.message.chat_id,text="Enter password: ")
    turnOff_handler_status = True
    turnOff_handler = MessageHandler(Filters.text,shutdownFunc)
    dispatcher.add_handler(turnOff_handler)


#command environment mode
def commandENV(update, context):
    disable_all_handlers()
    context.bot.send_message(chat_id=update.message.chat_id, text="You are now in command mode\nWrite any command you want\nYou can exit command mode use another base commands")
    global recCommand_handler,command_handler_status
    command_handler_status = True
    recCommand_handler = MessageHandler(Filters.text, runCommand)
    dispatcher.add_handler(recCommand_handler)


#download environment mode
def downloadENV(update, context):
    disable_all_handlers()
    context.bot.send_message(chat_id=update.message.chat_id, text="File type:\nPhoto --> 1\nVideo --> 2\nAudio --> 3\nDocument --> 4")
    global rec_download,download_handler_status
    download_handler_status = True
    rec_download = MessageHandler(Filters.text,downloader)
    dispatcher.add_handler(rec_download)


#uplaod environment mode
def uplaodENV(update, context):
    disable_all_handlers()
    context.bot.send_message(chat_id=update.message.chat_id, text="File type:\nPhoto --> 1\nVideo --> 2\nAudio --> 3\nDocument --> 4")
    global rec_upload,upload_handler_status
    upload_handler_status = True
    rec_upload = MessageHandler(Filters.text,uploader)
    dispatcher.add_handler(rec_upload)


#screenshot function
def screen_shot(update, context):
    disable_all_handlers()
    FileTimeName = ScreenShotDir + str("/SC-") + datetime.datetime.now().strftime("%m-%dTime%H-%M-%S") + str(".jpg")
    mss().shot(output=FileTimeName)
    context.bot.send_message(chat_id=update.message.chat_id,text="Uploading screenshot .....")
    context.bot.send_document(chat_id=update.message.chat_id, document=open(FileTimeName,"rb"),reply_to_message_id=update.message.message_id)
#Functions------------------------------------------------------------------------


#Handlers-------------------------------------------------------------------------
print("Starting handlers .....")

#starting bot
start_handler = CommandHandler('start', start,Filters.user(username=available_username))
dispatcher.add_handler(start_handler)


#restarting OS
reboot_handler = CommandHandler('reboot',restartOS,Filters.user(username=available_username))
dispatcher.add_handler(reboot_handler)


#shutting down OS
shutdown_handler = CommandHandler('shutdown',shutdownOS,Filters.user(username=available_username))
dispatcher.add_handler(shutdown_handler)


#running command on OS
runCommand_handler = CommandHandler('runc',commandENV,Filters.user(username=available_username))
dispatcher.add_handler(runCommand_handler)


#downloading file to OS
download_handler = CommandHandler('download',downloadENV,Filters.user(username=available_username))
dispatcher.add_handler(download_handler)


#uploading file to OS
upload_handler = CommandHandler('upload',uplaodENV,Filters.user(username=available_username))
dispatcher.add_handler(upload_handler)


#send screenshot
screen_shot_handler = CommandHandler('screenshot',screen_shot,Filters.user(username=available_username))
dispatcher.add_handler(screen_shot_handler)


#kill process
kill_handler = CommandHandler('kill',killItSelf,Filters.user(username=available_username))
dispatcher.add_handler(kill_handler)
#Handlers-------------------------------------------------------------------------

#Base command functions & handlers ----------------------------- end -----------------------------




#start python telegram bot
updater.start_polling()
print("LUCID bot is running :)")