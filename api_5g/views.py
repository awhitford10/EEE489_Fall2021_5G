from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import time



def led(request, luminance):
    '''
    This is an API call for the LED response
    The rasberry pi should send a fetch request to http://{IP address for local machine}:8000/rasberryled/{light sensor output}
    output will be a binary value to control the LED
    '''
    initial_time = time.perf_counter()
    if request.method=="GET":
        if luminance<1:
            return JsonResponse({'led_setting':1, 'time in milliseconds': (time.perf_counter()-initial_time)*1000})
        elif luminance>=1:
            return JsonResponse({'led_setting':0, 'time in milliseconds': (time.perf_counter()-initial_time)*1000})
    

def video(request, picture_data):
    '''
    This is an API call for the video camera
    The rasberry pi should send a fetch request to http://{IP address for local machine}:8000/rasberryvideo/{binary_picture}
    output will be a binary value to control the camera
    '''
    # df_train = pd.read_csv('../ASL_ML_images/sign_mnist_train/sign_mnist_train.csv', delimiter=',')
    # df_test = pd.read_csv('../ASL_ML_images/sign_mnist_test/sign_mnist_test.csv', delimiter=',')

    return JsonResponse({'picture':picture_data})

