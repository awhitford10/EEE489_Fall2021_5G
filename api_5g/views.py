from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def led(request, luminance):
    '''
    This is an API call for the LED response
    The rasberry pi should send a fetch request to 
    '''
    if request.method=="GET":
        if luminance<50:
            return JsonResponse({'led_setting':1})
        else:
            return JsonResponse({'led_setting':0})
    

def video(request):
    return HttpResponse('Video Test')

