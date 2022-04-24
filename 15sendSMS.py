import requests

filename  = 'phones.txt'
text = ''' امیر هستم ببخشید بابت تاخیر در ارسال کتاب'''

def readphones(filename):
    with open(filename) as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    return content

def send_sms(number, text):
    api_key = '47585054733046676E6A705954345734496F52304A3851794573764A5334644A34486D5A424A664D2B67773D'
    url = 'https://api.kavenegar.com/v1/%s/sms/send.json' % (api_key)

    data = {'receptor': number, 'message': text}
    r = requests.post(url, data=data)
    #TODO send sms and return result
    return r.ok

phones = readphones(filename)
for phone in phones:
    if not send_sms(phone, text):
        print (phone)
