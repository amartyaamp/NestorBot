
### NESTORBot - Your companion to handle mails

Have you ever wondered about the usual day at work?
You get to office, check your important mails, reply or compose new urgent/important and set new tasks according to mail status.
You also set new contacts on basis of the mails.
Many mails are also frequently repetitive - like the time you take the late office cab, or the status report to your boss.

If you think you are spending more time on this (And can't outsource!) and have less time on actual work, Nestor can help you.

#### Features planned (in no particular order)
- Create and send mail [Working with simple smtplib]
- Read important mails - user requests
- Send calendar meeting invites and fix non-conflicting times
- Add contacts
- Important notifications - priority mails/ meeting/ 
- Adding mail templates

#### Installation

Nestor uses Micrsoft Bot builder and pybotframework.

_Prerequisite : Python 3 (Anaconda preferred in case of windows)_
1. Install Microsoft Bot Framework Emulator - [BotBuilder](https://github.com/Microsoft/BotFramework-Emulator)
2. Install pybotframework (This will install flask and other backbones of Nestor) - [PyBotFramework](https://github.com/michhar/pybotframework)
3. Clone this repo -
```
git clone https://github.com/amartyaamp/NestorBot.git
```
#### Running Nestor
1. Nestor currently uses SMTP library which requires SMTP server name and the source authentication details.
In the constants.py file - fill destination SMTP server details, and your authentication details - mail id and password.  
```
#SMTP details for Outlook
SMTP_SERVER_OUTLOOK = "smtp-mail.outlook.com"
SMTP_SERVER_PORT_OUTLOOK = 587

#Source mail authentication details
SOURCE_MAIL = "mailIdHere"
SOURCE_PASSWORD = "passwordHere"
```

2. Run the flask app
```
python NestorBot.py
```
3. Launch the botframework emulator you installed above and load the ``` http://localhost:3978/api/messages``` address
4. The app should be booted by now. You see the screen below.
<img src="https://raw.githubusercontent.com/amartyaamp/NestorBot/master/res/img/botframework_start.PNG" width="50%"></img>

#### Sending mail 
Nestor matches entities and intents through regex expressions only. Give keyword "mail" to start a mail-sending conversation.

<img src="https://raw.githubusercontent.com/amartyaamp/NestorBot/master/res/img/botframework_mail.PNG" width="50%"></img>
<img src="https://raw.githubusercontent.com/amartyaamp/NestorBot/master/res/img/botframework_mail_progress.PNG" width="45%"></img>
