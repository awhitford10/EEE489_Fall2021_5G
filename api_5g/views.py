from django.conf import settings
from sklearn.neighbors import KNeighborsClassifier
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import os
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
            return JsonResponse({'led_setting':1, 'time': (time.perf_counter()-initial_time)*1000})
        elif luminance>=1:
            return JsonResponse({'led_setting':0, 'time': (time.perf_counter()-initial_time)*1000})
    

def video(request, picture_data):
    '''
    This is an API call for the video camera
    The rasberry pi should send a fetch request to http://{IP address for local machine}:8000/rasberryvideo/{binary_picture}
    output will be a binary value to control the camera
    '''
    initial_time = time.perf_counter()

    pic_list_of_strings = picture_data.split(',')
    data_to_predict = pd.DataFrame([int(x) for x in pic_list_of_strings])
    data_to_predict = data_to_predict.transpose()


    # Creates Dataframes for training data from static files
    file_path = os.path.join(settings.STATIC_ROOT, 'data/sign_mnist_train.csv')
    df_train = pd.read_csv(file_path, delimiter=',')
    y_train = df_train['label']
    x_train = df_train[df_train.columns[1:]]

    
    KNN = KNeighborsClassifier(n_neighbors=5)
    KNN.fit(x_train,y_train)
    print(data_to_predict)                  

    prediction = KNN.predict(data_to_predict)
    print(prediction)

    return JsonResponse({'prediction': str(prediction[0]), 'time': (time.perf_counter()-initial_time)*1000})

