# MovieBot

Chatbot de consulta de filmes no telegram. Utiliza o Watson Assistant como gerenciador e a API do The Movie Database para consultas.

## Branches

Temos 3 branches para o projeto:

* Master: branch original que utiliza o long polling do Telegram
* GCloud: branch para deploy no GCloud App Engine. Utiliza webhooks manualmente com o Flask
* Heroku: branch para deploy no Heroku, utilizando a funcionalidade de webhook existente na biblioteca python-telegram-bot

## Configurações

Tanto a branch master quanto a GCloud precisa-se que se configure o arquivo de configuração config.ini com as configuraçõe de cada
api utilizada no projeto.

A branch do Heroku foi feita para se realizar deploy automatico a partir do GitHub, portanto utiliza variáveis de ambiente para configuração:

A seguir as variáveis que devem ser configuradas no Heroku:

* WATSON_ASSISTANT_TOKEN: token IAM do Watson Assistant
* WATSON_ASSISTANT_URL: URL do Watson Assistant
* ASSISTANT_ID: ID do Assistant criado no Watson Assistant
* S2T_TOKEN: token IAM da API Watson SpeechToText
* S2T_URL: URL da API Watson SpeechToText
* T2S_TOKEN: token IAM da API Watson TextToSpeech
* T2S_URL: URL da API Watson TExtToSpeech
* TELEGRAM_BOT_TOKEN: token do bot criado no Telegram
* TELEGRAM_WEBHOOK: url da aplicação do heroku (https://\<appname\>.herokuapp.com)
* TMDB_KEY: chave da API do TMDB

## Bugs conhecidos

* A branch GCloud não está lidando muito bem com o gerenciamento de sessão do Watson Assistant.
Toda vez que uma mensagem é recebida, uma nova sessão é criada