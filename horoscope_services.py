import requests
import os

base_url_horoscope = 'http://horoscope-api.herokuapp.com'

def get_horoscope(sign, scope):
    response = requests.get(base_url_horoscope + '/horoscope/today/' + sign)
    return response['horoscope']