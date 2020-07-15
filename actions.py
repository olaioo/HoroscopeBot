import movies


def action_handler(action, parameters, return_var):
    return_values = {}
    if action == 'trendings':
        return_values = get_trendings(parameters, return_var)
    elif action == 'search':
        return_values = search_movies(parameters, return_var)
    return {
            'skills': {
                'main skill': {
                    'user_defined': return_values
                }
            }
        }

def get_trendings(parameters, return_var):
    is_day = (parameters['periodo'] == 'dia')
    movie_titles = movies.get_trendings(is_day)

    # trato os nomes aqui para facilitar, tratar no assistant eh mais complexo
    # pois nao tenho o mesmo poder de programacao
    movie_string = '\n\n'
    for movie in movie_titles:
        movie_string += movie + ',\n'
    movie_string = movie_string[:-2]
    return {
        return_var: movie_string
    }

def search_movies(parameters, return_var):
    query = parameters['termo']
    movie_titles = movies.search_movies(query)

    # trato os nomes aqui para facilitar, tratar no assistant eh mais complexo
    # pois nao tenho o mesmo poder de programacao
    movie_string = '\n\n'
    for movie in movie_titles:
        movie_string += movie + ',\n'
    movie_string = movie_string[:-2]
    return {
        return_var: movie_string
    }


