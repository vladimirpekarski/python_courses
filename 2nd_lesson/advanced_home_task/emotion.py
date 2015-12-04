__author__ = 'vladimir.pekarsky'

import httplib
import json
import sys

KEY = 'key'

def print_emotions(image_url):
    if not image_url:
        print('Url is empty')
        sys.exit(-1)

    image = {'url': image_url}
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': KEY
    }

    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request('POST', '/emotion/v1.0/recognize', '{}'.format(image), headers)
    response = conn.getresponse()
    check_response_code(response)
    for face in read_response(response):
        for emotion, rate in face['scores'].iteritems():
            print('{}: {}'.format(emotion, rate))
        print('')

    conn.close()


def read_response(response):
    response_str = response.read()
    parsed_str = json.loads(response_str)

    return parsed_str


def check_response_code(response):
    response_code = response.status
    if response_code != 200:
        parsed_response = read_response(response)
        if response_code == 400:
            print(parsed_response['error']['message'])
        else:
            print(parsed_response['message'])

        sys.exit(response_code)


print_emotions('https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRG31eVOx2WjxT1XyT8ZpN2mvqp-ezSjaWH_NqZCIYq8J6xC8EW')
print_emotions('http://www.asba.com/resource/resmgr/Articles/smilebig.jpg')
print_emotions('https://oneneighbourhood.files.wordpress.com/2014/11/surprise.jpg')
print_emotions('http://img2.tvtome.com/i/u/28c79aac89f44f2dcf865ab8c03a4201.png')