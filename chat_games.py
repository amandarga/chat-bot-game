import telebot

CHAVE_API = "8322855954:AAGwam-tzC6puWuDlQz5-X_XObyPEOmd0_g"

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["1"])
def o1(mensagem):
    texto = """
    *God of War* \n
    Depois de uma vida marcada pela guerra e pela tragédia, Kratos, o antigo deus da guerra da mitologia grega, busca redenção em uma nova terra: o reino dos deuses nórdicos. Vivendo isolado nas florestas da Escandinávia, ele tenta deixar para trás o passado violento e criar seu filho Atreus como um homem melhor do que ele foi. Quando a morte da esposa desencadeia uma jornada inesperada, pai e filho embarcam em uma perigosa viagem para cumprir seu último desejo: espalhar suas cinzas no ponto mais alto dos nove reinos. Ao longo do caminho, eles enfrentam monstros, deuses e segredos do passado, enquanto Kratos luta para controlar sua fúria e ensinar a Atreus o verdadeiro significado de força, honra e humanidade. Entre batalhas épicas e momentos de profunda emoção, God of War é uma história sobre paternidade, redenção e o eterno conflito entre o homem e o deus dentro de si.
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["2"])
def o2(mensagem):
    texto = """
    *Red Dead Redemption 2* \n
    No ocaso do Velho Oeste, o fora-da-lei Arthur Morgan e os membros da gangue Van der Linde lutam para sobreviver em um mundo que está mudando rapidamente. Após um assalto fracassado na cidade de Blackwater, o grupo é forçado a fugir, caçado por agentes federais e caçadores de recompensas. Enquanto a lealdade à gangue e ao carismático líder Dutch van der Linde começa a ser testada, Arthur enfrenta um dilema moral: seguir cegamente os ideais do bando ou buscar sua própria redenção. Em meio a paisagens deslumbrantes, tiroteios brutais e escolhas difíceis, ele descobre que cada decisão tem um preço — e que até mesmo os mais duros fora-da-lei não podem escapar de suas consequências. Red Dead Redemption 2 é uma jornada épica sobre honra, lealdade e a luta por um lugar em um mundo que está deixando os cowboys para trás.
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["3"])
def o3(mensagem):
    texto = """
    *Resident Evil 4* \n
    
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["4"])
def o4(mensagem):
    texto = """
    *The Legend of Zelda: Breath of the Wild* \n
    
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["5"])
def o5(mensagem):
    texto = """
    *Cyberpunk 2077* \n
    
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["6"])
def o6(mensagem):
    texto = """
    *Hogwarts Legacy* \n
    
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["7"])
def o7(mensagem):
    texto = """
    Tchau! Espero que tenha gostado!
    """
    bot.send_message(mensagem.chat.id, texto)

def verificar(mensagem):
    return mensagem.text and not mensagem.text.startswith('/')

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Oiee! Espero que esteja bem! Aqui tem algumas sinopses de jogos para você!
    
    /1 - God of War
    /2 - Red Dead Redemption 2
    /3 - Resident Evil 4
    /4 - The Legend of Zelda: Breath of the Wild
    /5 - Cyberpunk 2077
    /6 - Hogwarts Legacy        
    /7 - Sair"""
    bot.reply_to(mensagem, texto)

bot.polling()