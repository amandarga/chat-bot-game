import telebot

CHAVE_API = "8322855954:AAGwam-tzC6puWuDlQz5-X_XObyPEOmd0_g"

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["1"])
def o1(mensagem):
    texto = """
    *God of War* \n
    Depois de uma vida marcada pela guerra e pela tragédia, Kratos, o antigo deus da guerra da mitologia grega, busca redenção em uma nova terra: o reino dos deuses nórdicos. Vivendo isolado nas florestas da Escandinávia, ele tenta deixar para trás o passado violento e criar seu filho Atreus como um homem melhor do que ele foi. 
    Quando a morte da esposa desencadeia uma jornada inesperada, pai e filho embarcam em uma perigosa viagem para cumprir seu último desejo: espalhar suas cinzas no ponto mais alto dos nove reinos. Ao longo do caminho, eles enfrentam monstros, deuses e segredos do passado, enquanto Kratos luta para controlar sua fúria e ensinar a Atreus o verdadeiro significado de força, honra e humanidade. 
    Entre batalhas épicas e momentos de profunda emoção, God of War é uma história sobre paternidade, redenção e o eterno conflito entre o homem e o deus dentro de si.
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["2"])
def o2(mensagem):
    texto = """
    *Red Dead Redemption 2* \n
    No ocaso do Velho Oeste, o fora-da-lei Arthur Morgan e os membros da gangue Van der Linde lutam para sobreviver em um mundo que está mudando rapidamente. Após um assalto fracassado na cidade de Blackwater, o grupo é forçado a fugir, caçado por agentes federais e caçadores de recompensas. 
    Enquanto a lealdade à gangue e ao carismático líder Dutch van der Linde começa a ser testada, Arthur enfrenta um dilema moral: seguir cegamente os ideais do bando ou buscar sua própria redenção. Em meio a paisagens deslumbrantes, tiroteios brutais e escolhas difíceis, ele descobre que cada decisão tem um preço — e que até mesmo os mais duros fora-da-lei não podem escapar de suas consequências. 
    Red Dead Redemption 2 é uma jornada épica sobre honra, lealdade e a luta por um lugar em um mundo que está deixando os cowboys para trás.
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["3"])
def o3(mensagem):
    texto = """
    *Resident Evil 4* \n
    Seis anos após o desastre biológico em Raccoon City, o agente especial Leon S. Kennedy é enviado em uma missão secreta para resgatar Ashley Graham, a filha sequestrada do presidente dos Estados Unidos. Sua busca o leva a uma isolada vila na Europa, onde os habitantes foram infectados por um parasita misterioso conhecido como Las Plagas.
    Enquanto enfrenta hordas de aldeões hostis, monstros grotescos e inimigos que desafiam a razão humana, Leon descobre uma conspiração que ameaça muito mais do que a vida da garota — colocando em risco toda a humanidade.
    Entre ação intensa, suspense constante e atmosfera sombria, Resident Evil 4 redefine o horror de sobrevivência, equilibrando perfeitamente medo, estratégia e adrenalina.
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["4"])
def o4(mensagem):
    texto = """
    *The Legend of Zelda: Breath of the Wild* \n
    Após um sono de cem anos, o herói Link desperta em um mundo devastado e repleto de ruínas. Sem memória de seu passado, ele descobre que o reino de Hyrule foi destruído por uma força sombria conhecida como Calamity Ganon, que agora ameaça ressurgir e consumir tudo novamente.
    Guiado por vozes do passado e pela força de sua própria coragem, Link parte em uma jornada épica para recuperar suas lembranças, reunir aliados e libertar as quatro poderosas Criaturas Divinas. Somente então ele poderá enfrentar Ganon e salvar a princesa Zelda, que há um século mantém o mal contido com suas últimas forças.
    Em um vasto mundo aberto, cheio de segredos, perigos e liberdade total, Breath of the Wild redefine a aventura, convidando o jogador a explorar, descobrir e forjar seu próprio caminho para a lenda.
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["5"])
def o5(mensagem):
    texto = """
    *Cyberpunk 2077* \n
    Em um futuro distópico onde megacorporações dominam o mundo e a linha entre homem e máquina é quase inexistente, V — um mercenário em ascensão — busca o maior prêmio de todos: um implante lendário que promete a imortalidade.
    Ambientado em Night City, uma metrópole vibrante e brutal, cheia de neon, violência e ambição, V precisa forjar seu próprio caminho entre gangues, hackers e executivos sem alma. Quando um golpe dá errado, ele se vê conectado à consciência digital do lendário fora-da-lei Johnny Silverhand, vivido por Keanu Reeves — e juntos, lutam pelo controle do corpo e pelo destino da cidade.
    Com escolhas morais complexas, personagens marcantes e uma narrativa que se molda às decisões do jogador, Cyberpunk 2077 é uma jornada sobre poder, identidade e o preço de desafiar o sistema.
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["6"])
def o6(mensagem):
    texto = """
    *Hogwarts Legacy* \n
    Muito antes das aventuras de Harry Potter, no final do século XIX, um novo estudante chega à Escola de Magia e Bruxaria de Hogwarts com um segredo extraordinário: a rara habilidade de manipular uma antiga e poderosa magia esquecida pelo tempo.
    Como aluno recém-admitido, o jogador pode escolher sua casa, assistir a aulas icônicas como Poções, Defesa Contra as Artes das Trevas e Herbologia, e explorar livremente o vasto mundo mágico — desde os salões encantados de Hogwarts até as florestas sombrias e vilarejos misteriosos além dos muros do castelo.
    Mas uma rebelião sombria ameaça o equilíbrio do mundo bruxo. Cabe a você dominar feitiços, formar alianças e decidir o destino da magia antiga — usando-a para proteger ou para destruir.
    Hogwarts Legacy é uma jornada de descoberta, poder e escolhas, onde cada decisão molda o legado que você deixará em Hogwarts.
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