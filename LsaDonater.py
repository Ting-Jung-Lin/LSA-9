import telepot
import time
from telepot.loop import MessageLoop
from picamera import PiCamera

# LsaDonate Token
bot = telepot.Bot('5015633065:AAEJNx8OoHl2fjBDUR1DXDIFMoxdD2rYuN8')
def handle(msg):
    global checkisme
    chat_id = msg['chat']['id']
    telegramText = msg['text']
    print('Message received from ' + str(chat_id))
    # 開始連線，向 bot 訂閱通知
    if telegramText == '/start':
        bot.sendMessage(chat_id, 'Hi! This is a box you can donate some money:)')

#當偵測到有人投錢，就回傳照片與時間


MessageLoop(bot, handle).run_as_thread()
print("I'm listening...")

while True:
    time.sleep(1)
