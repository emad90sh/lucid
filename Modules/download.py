import datetime


from Modules.readConf import readingConf
photoDIR = readingConf()[0]
videoDIR = readingConf()[1]
audioDIR = readingConf()[2]
documentDIR = readingConf()[3]


def photo_downloader(update, context):#download photo (Only compress photo)
    PhtoName = str(photoDIR) + "/Photo-" + str(datetime.datetime.now().strftime("%m-%dTime%H-%M-%S")) + ".jpg"
    file = context.bot.getFile(update.message.photo[-1].file_id)
    context.bot.send_message(chat_id=update.message.chat_id,text="Downloading .....",reply_to_message_id=int(update.message.message_id))
    file.download(PhtoName)
    context.bot.send_message(chat_id=update.message.chat_id,text="Done",reply_to_message_id=int(update.message.message_id))


def video_downloader(update, context):#download photo (Only compress video)
    VideoName = str(videoDIR) + "/Video-" + str(datetime.datetime.now().strftime("%m-%dTime%H-%M-%S")) + ".mp4"
    file = context.bot.getFile(update.message.video.file_id)
    context.bot.send_message(chat_id=update.message.chat_id,text="Downloading .....",reply_to_message_id=int(update.message.message_id))
    file.download(VideoName)
    context.bot.send_message(chat_id=update.message.chat_id,text="Done",reply_to_message_id=int(update.message.message_id))


def audio_downloader(update, context):#download audio (mp3)
    AudioName = str(audioDIR) + "/Audio-" + str(datetime.datetime.now().strftime("%m-%dTime%H-%M-%S")) + ".mp3"
    file = context.bot.getFile(update.message.audio.file_id)
    context.bot.send_message(chat_id=update.message.chat_id,text="Downloading .....",reply_to_message_id=int(update.message.message_id))
    file.download(AudioName)
    context.bot.send_message(chat_id=update.message.chat_id,text="Done",reply_to_message_id=int(update.message.message_id))


def document_downloader(update, context):#download document (any file or send anything as file)
    DocumentDir = str(documentDIR) + "/" + str(update.message.document.file_name)
    file = context.bot.getFile(update.message.document.file_id)
    context.bot.send_message(chat_id=update.message.chat_id,text="Downloading .....",reply_to_message_id=int(update.message.message_id))
    file.download(DocumentDir)
    context.bot.send_message(chat_id=update.message.chat_id,text="Done",reply_to_message_id=int(update.message.message_id))