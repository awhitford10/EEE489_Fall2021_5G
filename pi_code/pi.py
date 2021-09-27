# This code is made to be imported on the rasberry pi unit itself
# the library "requests" needs to be installed into the pi unit before unit will work
# url may need to be adjusted

from requests import get
import smbus
import sys
import time as t
import board
import adafruit_veml7700
from picamera import PiCamera

camera = PiCamera()                             # camera
i2c = board.I2C()                               # uses board.SCL and board.SDA
veml7700 = adafruit_veml7700.VEML7700(i2c)      # light sensor
DEVICE_BUS = 1
DEVICE_ADDR = 0x11
bus = smbus.SMBus(DEVICE_BUS)



while True:

    ############################# LED Section ###########################################
  
    led_fetch_url = f'https://eee489-5g.herokuapp.com/rasberryled/{veml7700.lux}'   # fetch for lux value
    led_response = get(led_fetch_url).json()                                        # make a get request to heroku website

    if led_response['led_setting'] == 1:
        bus.write_byte_data(DEVICE_ADDR, 1, 0xFF)           # turns on led if fetch request sends back on command
        image = camera.capture(format = 'jpeg')             # Image taken if led is on
        t.sleep(1)             
        bus.write_byte_data(DEVICE_ADDR, 1, 0x00)           # turns off led if fetch sends back off

    elif led_response['led_setting'] == 0:
        bus.write_byte_data(DEVICE_ADDR, 1, 0x00)           # turns off led if fetch sends back off
        t.sleep(1)  


    ############################ Image Section ##########################################


    image_fetch_url = f'https://eee489-5g.herokuapp.com/rasberryled/{     }'   # fetch for lux value
    image_response = get(image_fetch_url).json()

    if image_response['complete'] == 1:
        break    

    
    t.sleep(1)                                              # controls burst interval