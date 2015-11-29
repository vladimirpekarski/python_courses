__author__ = 'vladimir.pekarsky'

import httplib
import json
import sys

KEY = 'key'

def get_emotions_list(image_url):
    image = {'url': image_url}
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': KEY
    }
    try:
        conn = httplib.HTTPSConnection('api.projectoxford.ai')
        conn.request('POST', '/emotion/v1.0/recognize', '{}'.format(image), headers)
        response = conn.getresponse()
        check_response_code(response)
        response_str = response.read()
        parsed_str = json.loads(response_str)
        for face in parsed_str:
            for emotion, rate in face['scores'].iteritems():
                print('{}: {}'.format(emotion, rate))
            print('')

        conn.close()
    except Exception as e:
        print(e.message)


def check_response_code(response):
    response_code = response.status
    if response_code != 200:
        print('something went wrong')
        sys.exit(response_code)

get_emotions_list('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWaAjSvXhfgIAv2tHWsR-UxPChUN4c7PI9TaJjviC7qID-G6II')
get_emotions_list('http://www.asba.com/resource/resmgr/Articles/smilebig.jpg')
get_emotions_list('https://oneneighbourhood.files.wordpress.com/2014/11/surprise.jpg')
get_emotions_list('http://img2.tvtome.com/i/u/28c79aac89f44f2dcf865ab8c03a4201.png')