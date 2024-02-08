import time

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def game_over():
    delay_print("Fim de jogo.")

def bad_ending():
    delay_print("Você falhou em descobrir a verdade. A justiça não prevaleceu.")

def good_ending():
    delay_print("Você descobriu a verdade e trouxe justiça para Veridale.")

def intro():
    delay_print("Ecos da Justiça")
    delay_print("Uma história de drama, crime e redenção...")
    delay_print("Você é Lily Andrews, uma advogada de defesa, e seu cliente é Marcus Turner, acusado de roubo.")

def act1():
    delay_print("Ato 1: O Roubo Enigmático")
    delay_print("Você inicia sua investigação e descobre que o artefato roubado possui uma história sombria.")
    delay_print("Você tem duas opções:")
    delay_print("1. Investigar a cena do crime no museu.")
    delay_print("2. Pesquisar o passado de Marcus Turner.")
    choice = input("O que você deseja fazer? (1 ou 2): ")
    if choice == "1":
        delay_print("Você examina cuidadosamente a cena do crime e encontra uma pista crucial.")
    elif choice == "2":
        delay_print("Você pesquisa o passado de Marcus Turner e descobre que ele tinha um motivo para roubar o artefato.")
    else:
        game_over()

def act2():
    delay_print("Ato 2: Sombras da Traição")
    delay_print("Você continua sua investigação e encontra evidências que ligam Marcus Turner ao negociante de arte Vincent Blackwood.")
    delay_print("Você tem duas opções:")
    delay_print("1. Interrogar Marcus Turner sobre sua conexão com Vincent Blackwood.")
    delay_print("2. Investigar o escritório de Vincent Blackwood.")
    choice = input("O que você deseja fazer? (1 ou 2): ")
    if choice == "1":
        delay_print("Você interroga Marcus Turner e ele revela que Vincent Blackwood o chantageou.")
    elif choice == "2":
        delay_print("Você invade o escritório de Vincent Blackwood e encontra documentos incriminadores.")
    else:
        game_over()

def act3():
    delay_print("Ato 3: Revelando a Verdade")
    delay_print("Você continua a coletar evidências e descobre uma conexão surpreendente entre o artefato roubado e um evento trágico de seu próprio passado.")
    delay_print("Você tem duas opções:")
    delay_print("1. Revelar sua conexão pessoal com o caso em tribunal.")
    delay_print("2. Manter sua conexão pessoal em segredo e focar nas evidências.")
    choice = input("O que você deseja fazer? (1 ou 2): ")
    if choice == "1":
        delay_print("Você revela sua conexão pessoal e ganha a simpatia do júri.")
    elif choice == "2":
        delay_print("Você mantém sua conexão pessoal em segredo e apresenta evidências convincentes no tribunal.")
    else:
        game_over()

def act4():
    delay_print("Ato 4: A Batalha Final")
    delay_print("Você se prepara para a batalha final no tribunal, onde enfrentará as autoridades corruptas envolvidas no encobrimento do crime relacionado ao artefato roubado.")
    delay_print("Durante o julgamento, você tem a oportunidade de apresentar provas e argumentos para expor a corrupção.")
    delay_print("Você tem duas opções:")
    delay_print("1. Focar na exposição das autoridades corruptas.")
    delay_print("2. Apresentar uma defesa forte para seu cliente, Marcus Turner.")
    choice = input("O que você deseja fazer? (1 ou 2): ")
    if choice == "1":
        delay_print("Você expõe as autoridades corruptas e elas são condenadas.")
    elif choice == "2":
        delay_print("Você apresenta uma defesa sólida para Marcus Turner e ele é considerado inocente.")
    else:
        game_over()

def game():
    intro()
    act1()
    act2()
    act3()
    act4()
#LOL
    delay_print("O julgamento chegou ao fim. Agora é a hora de enfrentar as consequências de suas escolhas.")
    delay_print("Você tem duas opções:")
    delay_print("1. Seguir em frente e deixar o passado para trás.")
    delay_print("2. Revelar a verdade por trás do evento trágico de seu próprio passado.")
    choice = input("O que você deseja fazer? (1 ou 2): ")
    if choice == "1":
        good_ending()
    elif choice == "2":
        delay_print("Ao revelar a verdade sobre seu passado, você obtém redenção e traz justiça para Veridale.")
        good_ending()
    else:
        game_over()

if __name__ == "__main__":
    game()
