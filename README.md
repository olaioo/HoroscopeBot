# HoroscopeBot

Chatbot de consulta de horoscopo no telegram. Utiliza o Watson Assistant como gerenciador e as seguintes API's:

* Horoscope API (https://rapidapi.com/Alejandro99aru/api/horoscope-astrology/)
* Love Calculator (https://rapidapi.com/ajith/api/love-calculator/)
* Zodiac Sign (Implementação Própria)

## Funcionalidades

O HoroscopeBot descobre seu signo pela data de nascimento, entrega horóscopo diário, semanal e mensal. Também determina a afinidade entre duas pessoas pelo seus nomes. Consegue interagir tanto por texto, quanto por mensagem de áudio.

## Instalação

Requisitos necessários para efetuar a instalação são:

* Possuir os serviços da IBM: Watson Assistant, Watson SpeechToText e Watson TextToSpeech
* Bot no Telegram
* Conta no RapidAPI


Carregue a skill para o Watson Assistant localizada na raíz do projeto com o nome 'skill-HoroscopoChatBot.json', em seguida defina ela como skill padrão. 


Para a aplicação, basta clonar ou realizar um fork do repositório, adicionar as configurações da seção abaixo e em seguida rodar o Dockerfile e o docker-compose.yml.

## Configurações

A seguir as variáveis de ambiente que devem ser configuradas no servidor:

* WATSON_ASSISTANT_TOKEN: token IAM do Watson Assistant
* WATSON_ASSISTANT_URL: URL do Watson Assistant
* ASSISTANT_ID: ID do Assistant criado no Watson Assistant
* S2T_TOKEN: token IAM da API Watson SpeechToText
* S2T_URL: URL da API Watson SpeechToText
* T2S_TOKEN: token IAM da API Watson TextToSpeech
* T2S_URL: URL da API Watson TExtToSpeech
* TELEGRAM_BOT_TOKEN: token do bot criado no Telegram
* TELEGRAM_WEBHOOK: url da aplicação
* RAPIDAPI_KEY: token para acessar as API's lovecalculator e zodiacsign, adquirido em (https://rapidapi.com/)

## Demonstração

O HoroscopeBot está online e pode ser acessado pelo telegram, basta adicioná-lo pelo username [@IA3Chatbot](https://t.me/IA3Chatbot)

Exemplos de perguntas:

* Quero descobrir o meu signo, nasci em 05/06/1998.
* Qual é o horoscopo semanal para peixes?
* Quero saber a afinidade entre duas pessoas
  * Alberto
  * Maria