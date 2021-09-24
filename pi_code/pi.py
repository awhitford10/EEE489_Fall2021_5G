# This code is made to be imported on the rasberry pi unit itself
# the library requests needs to be installed into the pi unit before unit will work
# url may need to be adjusted


from requests import get


url = 'http://0.0.0.0:8000/rasberryled/49'

led_response = get(url).json()

print(led_response)