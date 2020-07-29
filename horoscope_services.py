import requests
import os

base_url_horoscope = 'http://horoscope-api.herokuapp.com'
base_url_lovecalculator = 'https://love-calculator.p.rapidapi.com'

key_lovecalculator = os.environ.get('LOVECALCULATOR_KEY')

def get_horoscope(sign, scope):
    response = requests.get(base_url_horoscope + '/horoscope/'+ scope+ '/' + sign).json()
    return response['horoscope']

def get_percentage(fname, sname):
    response = requests.get(base_url_lovecalculator + '/getPercentage', {'fname': fname, 'sname': sname}, headers={'x-rapidapi-key': key_lovecalculator}).json()
    return response['result'] + " " + response['percentage'] + '%'