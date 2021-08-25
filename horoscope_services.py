import requests
import os

base_url_horoscope = 'http://horoscope-api.herokuapp.com'
base_url_lovecalculator = 'https://love-calculator.p.rapidapi.com'
base_url_zodiacsign = 'https://zodiac-sign.p.rapidapi.com'

key_rapidapi = os.environ.get('RAPIDAPI_KEY')

def get_horoscope(sign, scope):
    response = requests.get(base_url_horoscope + '/horoscope/'+ scope+ '/' + sign).json()
    return response['horoscope']

def get_percentage(fname, sname):
    response = requests.get(base_url_lovecalculator + '/getPercentage', {'fname': fname, 'sname': sname}, headers={'x-rapidapi-key': key_rapidapi, 'x-rapidapi-host': base_url_lovecalculator.replace('https://','')}).json()
    return response['result'] + " " + response['percentage'] + '%'

def get_sign(date):
    response = requests.get(base_url_zodiacsign + '/sign', {'date': date}, headers={'x-rapidapi-key': key_rapidapi, 'x-rapidapi-host': base_url_horoscope.replace('https://','')})
    return response.text