import telepot
import datetime
import time
import RPi.GPIO as GPIO
import picamera

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
BUTTON_PIN=37
MOTOR_CONTROL_PIN=11
GPIO.setup(BUTTON_PIN,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)#下拉電阻
GPIO.setup(MOTOR_CONTROL_PIN,GPIO.OUT)

bot = telepot.Bot('yourtoken')
while True:
    GPIO.setwarnings(False)
    BUTTON_STATUS=GPIO.input(BUTTON_PIN)
     #開關壓下去
    if(BUTTON_STATUS==True):
         #輸出高電壓到調速馬達
         GPIO.output(MOTOR_CONTROL_PIN,1)
         time.sleep(3)
         #停住幾秒
         GPIO.output(MOTOR_CONTROL_PIN,0)
         #拍照
         camera = picamera.PiCamera()
         time.sleep(5)
         camera.capture('success22.png')
         camera.close()
         photo = 'success22.png'
         bot.sendPhoto(847958195,photo=open(photo, 'rb'))
         #停住幾秒
         GPIO.output(MOTOR_CONTROL_PIN,1)
         time.sleep(1)
         #開關放開
         for i in range(10):
            print(str(i)+"一圈跑完")
    else:
         GPIO.output(MOTOR_CONTROL_PIN,0)