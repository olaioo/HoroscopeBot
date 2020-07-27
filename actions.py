import horoscope_services


def action_handler(action, parameters, return_var):
    return_values = {}
    if action == 'previsao':
        return_values = get_horoscope(parameters, return_var)
    return {
            'skills': {
                'main skill': {
                    'user_defined': return_values
                }
            }
        }

def get_horoscope(parameters, return_var):
    sign = parameters['signo']
    scope = parameters['escopo']

    return {
        return_var: horoscope_services.get_horoscope(sign, scope)
    }