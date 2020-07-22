import requests
import os



base_url = 'https://api.themoviedb.org/3'
api_key = os.environ.get('TMDB_KEY')


def get_trendings(is_day):
    endpoint = ''
    if is_day:
        endpoint = '/trending/movie/day'
    else:
        endpoint = '/trending/movie/week'

    parameters = '?' + 'language=pt-BR' + '&api_key=' + api_key

    final_url = base_url + endpoint + parameters

    response = requests.get(final_url).json()

    return [movie['title'] for movie in response['results']]

def search_movies(query):
    endpoint = '/search/movie'

    parameters = '?' + 'query=' + query + '&language=pt-BR' + '&api_key=' + api_key

    final_url = base_url + endpoint + parameters

    response = requests.get(final_url).json()
    return [movie['title'] for movie in response['results']]

