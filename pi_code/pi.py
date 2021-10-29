# This code is made to be imported on the rasberry pi unit itself
# the library "requests" needs to be installed into the pi unit before unit will work
# url may need to be adjusted

from requests import get
from PIL import Image, ImageOps
import pyspeedtest
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

    total_time = t.perf_counter()

    ############################# LED Section ###########################################
  
    # led_fetch_url = f'https://eee489-5g.herokuapp.com/rasberryled/{veml7700.lux}'   # fetch for lux value with pi
    led_fetch_url = f'http://127.0.0.1:8000/rasberryled/0'   # fetch for local simulation
    print('\n\n____________________________________________\n\nlow lux value simulated\n')
    led_get = get(led_fetch_url)
    led_response = led_get.json()                  # make a get request to heroku website
    print('led setting:',led_response['led_setting'],'\nled backend processing time in milliseconds:',led_response['time'])
    print('LED fetch response time(milliseconds): ', led_get.elapsed.total_seconds()*1000)

    if led_response['led_setting'] == 1:
        # bus.write_byte_data(DEVICE_ADDR, 1, 0xFF)           # turns on led if fetch request sends back on command
        print('\nled turns on')
        # image = camera.capture(format = 'jpeg')             # Image taken if led is on
        print('takes picture')
        t.sleep(1)             
        # bus.write_byte_data(DEVICE_ADDR, 1, 0x00)           # turns off led if fetch sends back off
        print('led turns off\n')

    elif led_response['led_setting'] == 0:
        # bus.write_byte_data(DEVICE_ADDR, 1, 0x00)           # turns off led if fetch sends back off
        print('led turns off')
        t.sleep(1)  


    ############################ Image Section ##########################################

    # im = image                                                # image from rasberry pi not used in simulation
    im = Image.open('HandsignalA.jpg')                          # image upload for cpu simulation
    im = ImageOps.grayscale(im)                                 # Converts image to grayscale
    im = im.resize((28,28), Image.ANTIALIAS)                    # Resize image to same size as ML analysis (28x28px)

    #im.save('resize.jpg')                                      #image saved to for viewing purposes/troubleshooting 
    pic = list(im.getdata())                                    # Gets image data as a list of pixels


    pic_string = (",".join([str(x) for x in pic]))              # joins data for minimal string

    # image_fetch_url = f'https://eee489-5g.herokuapp.com/rasberryvideo/{pic_string}' 
    image_fetch_url = f'http://127.0.0.1:8000/rasberryvideo/{pic_string}'   
    get_image = get(image_fetch_url)
    image_response = get_image.json()

    print('Prediction:',image_response['prediction'],'\nVideo backend procesing time in milliseconds:', image_response['time'] )
    end_time = (t.perf_counter()-total_time)*1000
    print('\nTotal time:', end_time)
    print('delta time(back and forth communication):', end_time - image_response['time'] - led_response['time'] )
    print('Image fetch response time(milliseconds): ', get_image.elapsed.total_seconds()*1000)

    t.sleep(1)

    print('\nend of simulation\n_______________________________')
    break                                                       #break after one run through for testing 




