#dili Python ile Call Bomber Kodu

#gerekli kütüphaneleri import edin
import os
import time
import random
import requests

#yapılacak aramaların sayısını belirtin
num = 0

#aramaların yapılacağı numarayı belirtin
phone_no = "xxxxxxxxxx"

#aramaların yapılacağı süreyi belirtin
while (num < 100):
    api_request = requests.post("http://api.textlocal.in/send/",
    {
        'apikey':'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        'numbers': phone_no,
        'message' : "This is a bomb call",
    })
    print("Sunucu tarafından gönderilen cevap:", api_request.text)
    num = num + 1
    time.sleep(1)