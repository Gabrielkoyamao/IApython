from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')

conversa = ['Oi', 'Ola', 'Tudo Bem?', 'Eu estou bem']
conversa2 = ["Qual o seu filme preferido", "Os Vingadores"]

bot.set_trainer(ListTrainer)
bot.train(conversa)
bot.train(conversa2)


while True:
    quest = input("Voce: ")
    resposta = bot.get_response(quest)
    if float(resposta.confidence) > 0.5:
        print("Bot: ",resposta)
    else:
        print("Bot: Eu nao sei! ")