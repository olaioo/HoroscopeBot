import horoscope_services
import translator

def action_handler(action, parameters, return_var):
    return_values = {}
    if action == 'previsao':
        return_values = get_horoscope(parameters, return_var)
    elif action == 'combinar':
        return_values = get_percentage(parameters, return_var)
    elif action == 'descobrir_signo':
        return_values = get_sign(parameters, return_var)
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

    response_text = horoscope_services.get_horoscope(sign, scope)

    translated = translator.translate(response_text)

    return {
        return_var: translated
    }

def get_percentage(parameters, return_var):
    fname = parameters['fname']
    sname = parameters['sname']

    response_text = horoscope_services.get_percentage(fname, sname)

    translated = translator.translate(response_text)
    
    return {
        return_var: translated
    }

def get_sign(parameters, return_var):
    date = parameters['date']

    response_text = horoscope_services.get_sign(date)

    translated = translator.translate(response_text)

    return {
        return_var: "Leão" if translated == "Leo" else translated
    }