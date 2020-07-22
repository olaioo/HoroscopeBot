from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from session_manager import SessionManager
import os
import logging
import actions

IAM_TOKEN = os.environ.get('WATSON_ASSISTANT_TOKEN')
ASSISTANT_URL = os.environ.get('WATSON_ASSISTANT_URL')


logger = logging.getLogger('TelegramBot')

authenticator = IAMAuthenticator(IAM_TOKEN)
assistant_id = os.environ.get('ASSISTANT_ID')

assistant = AssistantV2(
    version='2020-02-05',
    authenticator=authenticator
)

assistant.set_service_url(ASSISTANT_URL)

def create_session():
    response = assistant.create_session(assistant_id)
    return response.get_result()['session_id']

def validate_session(chat_id):
    # check if session is valid for current chat_id
    logger.info('Validando sessão de ' + str(chat_id))
    if not SessionManager.getInstance().checkSession(chat_id):
        session_id = create_session()
        logger.info('Sessão criada para ' + str(chat_id))
    else:
        session_id = SessionManager.getInstance().getSession(chat_id)
        logger.info('Sessão atualizada para ' + str(chat_id))

    SessionManager.getInstance().updateSession(chat_id, session_id)

def execute_action(session_id, response):
    #verifica se a resposta tem acao para ser executada
    if 'actions' in response['output']:
        action = response['output']['actions'][0]
        logger.info('Executando ação ' + action['name'])
        #executa a ação correta e recebe dados em um dicionario
        result_data = actions.action_handler(action['name'], action['parameters'], action['result_variable'])
        #envia dados de resposta como contexto para o Watson Assistant
        response = assistant.message(
            assistant_id=assistant_id,
            session_id=session_id,
            context=result_data
        ).get_result()
    return response


def send_message(session_id, message):
    logger.info('Enviando mensagem para o Assistant: ' + message)
    response = assistant.message(
        assistant_id=assistant_id,
        session_id=session_id,
        input={
            'message_type': 'text',
            'text': message
        }
    )
    result = response.get_result()
    logger.info(result)
    result = execute_action(session_id, result)
    logger.info('Recebido do assistant: ' + result['output']['generic'][0]['text'])
    return result['output']['generic'][0]['text']
