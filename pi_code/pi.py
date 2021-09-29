# This code is made to be imported on the rasberry pi unit itself
# the library "requests" needs to be installed into the pi unit before unit will work
# url may need to be adjusted

from requests import get
from PIL import Image, ImageOps
# import smbus
import sys
import time as t
import json
# import board
# import adafruit_veml7700
# from picamera import PiCamera


# camera = PiCamera()                             # camera
# i2c = board.I2C()                               # uses board.SCL and board.SDA
# veml7700 = adafruit_veml7700.VEML7700(i2c)      # light sensor
DEVICE_BUS = 1
DEVICE_ADDR = 0x11
# bus = smbus.SMBus(DEVICE_BUS)



while True:

    ############################# LED Section ###########################################
  
    # led_fetch_url = f'https://eee489-5g.herokuapp.com/rasberryled/{veml7700.lux}'   # fetch for lux value
    led_fetch_url = f'https://eee489-5g.herokuapp.com/rasberryled/0'   # fetch for lux value
    print('low lux value simulated')
    led_response = get(led_fetch_url).json()                                        # make a get request to heroku website

    if led_response['led_setting'] == 1:
        # bus.write_byte_data(DEVICE_ADDR, 1, 0xFF)           # turns on led if fetch request sends back on command
        print('led turns on')
        # image = camera.capture(format = 'jpeg')             # Image taken if led is on
        print('takes picture')
        t.sleep(1)             
        # bus.write_byte_data(DEVICE_ADDR, 1, 0x00)           # turns off led if fetch sends back off
        print('led turns off')
        break

    elif led_response['led_setting'] == 0:
        # bus.write_byte_data(DEVICE_ADDR, 1, 0x00)           # turns off led if fetch sends back off
        print('led turns off')
        t.sleep(1)  


    ############################ Image Section ##########################################


    # image_fetch_url = f'https://eee489-5g.herokuapp.com/rasberryled/test'   # fetch for lux value
    # image_response = get(image_fetch_url).json()

    # if image_response['complete'] == 1:
    #     break    

    
    t.sleep(1)                                              # controls burst interval

im = Image.open('HandsignalA.jpg')
im = ImageOps.grayscale(im)
im = im.resize((28,28), Image.ANTIALIAS)                    #resize image to same size as ML analysis

im.save('resize.jpg')                                       #image saved to for viewing purposes 
pic = list(im.getdata())          #This info needs to be pushed to fetch request


pic_string = (",".join([str(x) for x in pic]))

image_fetch_url = f'https://eee489-5g.herokuapp.com/rasberryvideo/{pic_string}'   
image_response = get(image_fetch_url, data={'picture_data':pic}).json()
print(image_response)

