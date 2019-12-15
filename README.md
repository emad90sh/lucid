# **LUCID Bot**
This is a simple telegram bot written in python to remotely manage your PC<br>
It uses **[python-telegram-bot](https://python-telegram-bot.org/)** modules to connect to telegram API <br><br><br>


# **Pre-Installation**
Python **Version-3.X** should be installed on the PC<br>
[Download Python](https://www.python.org/downloads/)<br>
This script supports (**Windows** - **Linux** - **Mac OS**)<br><br><br>


# **Installation**
## **Configuration**
- ### Modify **config.conf** file:
    - Working path needed when something download or takes screenshot<br>
      Default is Files directory<br>
      **WorkingFileDir = "Files"**

    - When some process starts, if it can't return any standard output, a default   output will return<br>
      Time frame is second<br>
      Default is 10<br>
      **ProcessTimeOut = 10**

    - Telegram token bot API<br>
      **[Get telegram token](https://telegram.me/BotFather)**<br>
      **Token = Your telegram bot token (without quotation)**

    - Allow username<br>
      Only allow this user to access your bot<br>
      **UserName = your telegram username (without quotation)**

<br>

## **Windows**
1. `python -m pip install -r requirements.txt` **Installing requirements**<br>
2. `python password.py` **to create password for critical command (shutdown , reboot , kill) Default password is: *lucid2019***<br>
3. `python lucid.py`

<br>

## **Linux / Mac OS**
1. `pip3 install -r requirements.txt` **Installing requirements**<br>
2. `python3 password.py` **to create password for critical command (shutdown , reboot , kill) Default password is: *lucid2019***<br>
3. `sudo python3 lucid.py` **(If you run script without sudo, reboot and shutdown stop working)**

<br>

## **Features**
- ### **Telegram commands**
      /runc - Running os command
      /download - Send file to OS
      /upload - Upload file from OS
      /screenshot - Take screenshot and send
      /reboot - Reboot OS
      /shutdown - Shutdown OS
      /kill - killing your process




<br><br><br>

## **This script is tested on**
- ### **Windows 8.1/10**
- ### **Linux 4.19**
- ### **Mac OS Mojave**
