import os.path


def photo_uploader(update,context):#upload photo (support jpg,png)
    chatID = update.message.chat_id
    msg_id=update.message.message_id
    msg_path = update.message.text
    if os.path.isfile(msg_path):#checking if file is exist
        fileEX = msg_path.split(".")[-1]
        if fileEX == "png" or fileEX == "jpg":#checking file extension
            context.bot.send_message(chat_id=chatID,text="File found\nUploading .....",reply_to_message_id=msg_id)
            context.bot.send_photo(chat_id=chatID, photo=open(msg_path, 'rb'),reply_to_message_id=int(msg_id))
        else:
            context.bot.send_message(chat_id=chatID,text="File found\nIvalid file format",reply_to_message_id=msg_id)
    else:
        context.bot.send_message(chat_id=chatID,text="File not found",reply_to_message_id=msg_id)


def video_uploader(update,context):#upload video (support mp4)
    chatID = update.message.chat_id
    msg_id=update.message.message_id
    msg_path = update.message.text
    if os.path.isfile(msg_path):#checking if file is exist
        fileEX = msg_path.split(".")[-1]
        if fileEX == "mp4":#checking file extension
            context.bot.send_message(chat_id=chatID,text="File found\nUploading .....",reply_to_message_id=msg_id)
            context.bot.send_video(chat_id=chatID, video=open(msg_path, 'rb'),reply_to_message_id=int(msg_id))
        else:
            context.bot.send_message(chat_id=chatID,text="File found\nIvalid file format",reply_to_message_id=msg_id)
    else:
        context.bot.send_message(chat_id=chatID,text="File not found",reply_to_message_id=msg_id)



def audio_uploader(update,context):#upload video (support mp4)
    chatID = update.message.chat_id
    msg_id=update.message.message_id
    msg_path = update.message.text
    if os.path.isfile(msg_path):#checking if file is exist
        fileEX = msg_path.split(".")[-1]
        if fileEX == "mp3":#checking file extension
            context.bot.send_message(chat_id=chatID,text="File found\nUploading .....",reply_to_message_id=msg_id)
            context.bot.send_audio(chat_id=chatID, audio=open(msg_path, 'rb'),reply_to_message_id=int(msg_id))
        else:
            context.bot.send_message(chat_id=chatID,text="File found\nIvalid file format",reply_to_message_id=msg_id)
    else:
        context.bot.send_message(chat_id=chatID,text="File not found",reply_to_message_id=msg_id)


def document_uploader(update,context):#upload document file (support any file format)
    chatID=update.message.chat_id
    msg_id=update.message.message_id
    msg_path = update.message.text
    if os.path.isfile(msg_path):#checking if file is exist
        context.bot.send_message(chat_id=chatID,text="File found\nUploading .....",reply_to_message_id=msg_id)
        context.bot.send_document(chat_id=chatID, document=open(msg_path, 'rb'),reply_to_message_id=int(msg_id))
    else:
        context.bot.send_message(chat_id=chatID,text="File not found",reply_to_message_id=msg_id)