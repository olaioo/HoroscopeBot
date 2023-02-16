import requests
import os

from datetime import datetime

base_url_horoscope = 'http://horoscope-api.herokuapp.com'
base_url_lovecalculator = 'https://love-calculator.p.rapidapi.com'

key_rapidapi = os.environ.get('RAPIDAPI_KEY')

def get_horoscope(sign, scope):
    response = requests.get(base_url_horoscope + '/horoscope/'+ scope+ '/' + sign).json()
    return response['horoscope']

def get_percentage(fname, sname):
    response = requests.get(base_url_lovecalculator + '/getPercentage', {'fname': fname, 'sname': sname}, headers={'x-rapidapi-key': key_rapidapi}).json()
    return response['result'] + " " + response['percentage'] + '%'

def get_sign(date):
    inner_date = datetime.fromisoformat(date)
    month = inner_date.month * 100
    if month < 120 :
        return 'Capricorn'
    elif month < 219 :
        return 'Aquarius'
    elif month < 321 :
        return 'Pisces'
    elif month < 420 :
        return 'Aries'
    elif month < 521 :
        return 'Taurus'
    elif month < 621 :
        return 'Gemini'
    elif month < 723 :
        return 'Cancer'
    elif month < 823 :
        return 'Leo'
    elif month < 923 :
        return 'Virgo'
    elif month < 1023 :
        return 'Libra'
    elif month < 1122 :
        return 'Scorpio'
    elif month < 1222 :
        return 'Sagittarius'
    else :
        return 'Mystery'