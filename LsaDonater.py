import telepot
import datetime
import time
from telepot.loop import MessageLoop
#from picamera import PiCamera

# LsaDonate Token
bot = telepot.Bot('5070507195:AAHi5vBDOxF1c5AymErTqd_BA7UYvI6_X9A')
def handle(msg):
    global checkisme
    chat_id = msg['chat']['id']
    telegramText = msg['text']
    print('Message received from ' + str(chat_id))
    # 開始連線，向 bot 訂閱通知
    if telegramText == '/start':
        bot.sendMessage(chat_id, 'Hi! This is a box you can donate some money:)')
        photo = 'test.png'
        bot.sendPhoto(chat_id,photo=open(photo, 'rb'))

        
MessageLoop(bot, handle).run_as_thread()
print("I'm listening...")
#print(datetime.now())

while True:
    time.sleep(1)
