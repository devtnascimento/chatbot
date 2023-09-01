from chatbot import ChatBot
import os

myChatBot = ChatBot()

new_model = input("Novo modelo? (Y/n): ")

if new_model in ['', 'y', 'Y']:

    #apenas carregar um modelo pronto
    myChatBot.createModel()
else:
    #criar o modelo
    myChatBot.loadModel()

print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Bem vindo ao Chatbot\n")

pergunta = input("como posso te ajudar? \n")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print(resposta + "   ["+intencao[0]['intent']+"]")

while (intencao[0]['intent']!="despedida"):
    pergunta = input("posso lhe ajudar com algo a mais?\n")
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    print("\n")
    print(resposta + "   [" + intencao[0]['intent'] + "]")
    print("\n\n")

print("Foi um prazer atendê-lo!\n")



