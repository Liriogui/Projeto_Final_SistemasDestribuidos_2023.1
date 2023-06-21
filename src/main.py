import telebot
import mysql.connector


CHAVE_API = "6070088798:AAEOhJrqc8rYNdFGHeG6qs-tdR1WUSbZhwk"
bot = telebot.TeleBot(CHAVE_API)


db = mysql.connector.connect(host='172.0.0.1',user='root',password='root',database='teste')
cur = db.cursor()


@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    Cardápio 
    /pizza            🍕
    /hamburguer       🍔
    /cachorro_Quente  🌭
    /coca_cola        🍾
    /bare             🍾
    /FantaLaranja     🍾"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["pizza"])
def pizza(mensagem):
    text = """
    /Mussarela             R$35,00 
    /Calabresa             R$40,00 
    /Marguerita            R$40,00 
    /4Queijos              R$45,00 
    /Frango_com_Catupiry   R$45,00 
    /Portuguesa            R$45,00 
    /Atum                  R$35,00
    /Bacon                 R$35,00"""
    bot.send_message(mensagem.chat.id,text)

@bot.message_handler(commands=["Mussarela"]) 
def mussarela(mensagem):
       cur.execute("SELECT pizza FROM pizzas WHERE id = 1")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)


@bot.message_handler(commands=["Calabresa"]) 
def calabresa(mensagem):
       cur.execute("SELECT pizza FROM pizzas WHERE id = 2")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)


@bot.message_handler(commands=["Marguerita"]) 
def marguerita(mensagem):
       cur.execute("SELECT pizza FROM pizzas WHERE id = 3")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)

@bot.message_handler(commands=["4Queijos"]) 
def queijos(mensagem):
       cur.execute("SELECT pizza FROM pizzas WHERE id = 4")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)

@bot.message_handler(commands=["Frango_com_Catupiry"]) 
def frango(mensagem):
       cur.execute("SELECT pizza FROM pizzas WHERE id = 5")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)

@bot.message_handler(commands=["Atum"]) 
def atum(mensagem):
       cur.execute("SELECT pizza FROM pizzas WHERE id = 7")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)

@bot.message_handler(commands=["Portuguesa"]) 
def portuguesa(mensagem):
       cur.execute("SELECT pizza FROM pizzas WHERE id = 6")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)

@bot.message_handler(commands=["Bacon"]) 
def bacon(mensagem):
       cur.execute("SELECT pizza FROM pizzas WHERE id = 8")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)

#Hamburguers

@bot.message_handler(commands=["hamburguer"])
def hamburguer(mensagem):
    text = """
    /Big_Mac              R$25,90
    /Whopper              R$29,90 
    /Cheeseburger         R$55,00
    /Double_Double        R$29,90
    /ShackBurger          R$35,90 """
    bot.send_message(mensagem.chat.id,text)


@bot.message_handler(commands=["Big_Mac"]) 
def big(mensagem):
       cur.execute("SELECT hamburguer FROM hamburguer WHERE id = 1")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)

@bot.message_handler(commands=["Whopper"]) 
def whopper(mensagem):
       cur.execute("SELECT hamburguer FROM hamburguer WHERE id = 2")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)

@bot.message_handler(commands=["Cheeseburger"]) 
def cheeseburguer(mensagem):
       cur.execute("SELECT hamburguer FROM hamburguer WHERE id = 3")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)

@bot.message_handler(commands=["Double-Double"]) 
def double(mensagem):
       cur.execute("SELECT hamburguer FROM hamburguer WHERE id = 4")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)

@bot.message_handler(commands=["ShackBurger"]) 
def shack(mensagem):
       cur.execute("SELECT hamburguer FROM hamburguer WHERE id = 5")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)

#cachorro quente   
@bot.message_handler(commands=["cachorro_Quente"])
def quente(mensagem):
    text = """
    /Classico     R$12,90
    /Brasileiro   R$13,90 
    /Mexicano     R$10,00
    /Havaiano     R$11,90"""
    bot.send_message(mensagem.chat.id,text)


@bot.message_handler(commands=["Classico"]) 
def classico(mensagem):
       cur.execute("SELECT cachorro_quente FROM cachorro_quente WHERE id = 1")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)

@bot.message_handler(commands=["Brasileiro"]) 
def brasileiro(mensagem):
       cur.execute("SELECT cachorro_quente FROM cachorro_quente WHERE id = 2")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)

@bot.message_handler(commands=["Mexicano"]) 
def mexicano(mensagem):
       cur.execute("SELECT cachorro_quente FROM cachorro_quente WHERE id = 3")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)

@bot.message_handler(commands=["Havaiano"]) 
def havaiano(mensagem):
       cur.execute("SELECT cachorro_quente FROM cachorro_quente WHERE id = 4")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)


#coca------------------------------------------------

@bot.message_handler(commands=["coca_cola"]) 
def coca(mensagem):
    text = """
    /coca500ML   R$5,90
    /coca1L      R$7,90
    /coca2L      R$10,99"""
    bot.send_message(mensagem.chat.id, text)

@bot.message_handler(commands=["coca500ML"]) 
def coca(mensagem):
       cur.execute("SELECT coca FROM coca WHERE id = 1")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)


@bot.message_handler(commands=["coca1L"]) 
def coca(mensagem):
       cur.execute("SELECT coca FROM coca WHERE id = 2")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)
       
@bot.message_handler(commands=["coca2L"]) 
def mussarela(mensagem):
       cur.execute("SELECT coca FROM coca WHERE id = 3")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)
#---------------------------------------------------------------

@bot.message_handler(commands=["bare"]) 
def coca(mensagem):
    text = """
    /bare500ML R$4,90
    /bare1L    R$6,90
    /bare2L    R$8,00"""
    bot.send_message(mensagem.chat.id, text)

@bot.message_handler(commands=["bare500ML"]) 
def mussarela(mensagem):
       cur.execute("SELECT bare FROM bare WHERE id = 1")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)

@bot.message_handler(commands=["bare1L"]) 
def mussarela(mensagem):
       cur.execute("SELECT bare FROM bare WHERE id = 2")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)
       
@bot.message_handler(commands=["bare2L"]) 
def mussarela(mensagem):
       cur.execute("SELECT bare FROM bare WHERE id = 3")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)

#============================================================================

@bot.message_handler(commands=["FantaLaranja"]) 
def fanta(mensagem):
    text = """
    /FantaLaranja500ML   R$5,90
    /FantaLaranja1L      R$6,99 
    /FantaLaranja2L      R$7,99"""
    bot.send_message(mensagem.chat.id, text)

@bot.message_handler(commands=["FantaLaranja500ML"]) 
def fanta(mensagem):
       cur.execute("SELECT fanta FROM fanta WHERE id = 1")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)

@bot.message_handler(commands=["FantaLaranja1L"]) 
def fanta(mensagem):
       cur.execute("SELECT bare FROM bare WHERE id = 2")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)
       
@bot.message_handler(commands=["FantaLaranja2L"]) 
def fanta(mensagem):
       cur.execute("SELECT bare FROM bare WHERE id = 3")
       r = cur.fetchall()
       text = r
       t = "Pedido realizado!"
       bot.send_message(mensagem.chat.id,t)
       bot.send_message(mensagem.chat.id,text)
#==================================================
#Gerar link de pagamento

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    text = """
    Link de Pagamento:\n
    https://nubank.com.br/pagar/1gb8rc/VR3oHTwCIQ"""
    bot.send_message(mensagem.chat.id, text)

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    text = """
    Envie um email para:\n
    salaches@gmail.com\n
    Teremos um prazer em atendê-lo"""
    bot.send_message(mensagem.chat.id, text)


#---------------------------------------------------------------------------------------------------------------
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    text = """
    \nSEJA BEM VINDO A S.A LACHES🤖
    
     Escolha uma opção (Clique no item):
     /opcao1 Fazer um pedido
     /opcao2 Realizar Pagamento
     /opcao3 Reclamar de um pedido

    Escolha apenas dentre as opções acima.."""
    bot.reply_to(mensagem, text)

bot.polling()
