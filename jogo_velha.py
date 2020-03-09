import time
from random import randint


class Jogador:
    def __init__(self, perfil):
        self.perfil_aceito = {1:'humano', 2:'pc'}
        self.perfil=self.definir_perfil(perfil)
        self.simbolo=None
        self.simbolo_aceito = {1:'X', 2:'O'}

    def definir_perfil(self, perfil):
        return self.perfil_aceito[perfil]

    def definir_simbolo(self, simbolo):
        self.simbolo = self.simbolo_aceito[simbolo]

class JogoVelha:
    def __init__(self, jogador1, jogador2):
        self.tabuleiro = [' ', ' ', ' '],\
                         [' ', ' ', ' '],\
                         [' ', ' ', ' ']
        self.jogada_feita = []
        self.fim_jogo = False
        self.vencedor = None
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.display_tabuleiro()

    def display_tabuleiro(self):
        count = 0
        for linha in self.tabuleiro:
            print(str(linha).replace('[','').replace(']','').replace(',','|'))
            if count in (0,1):
                print('---------------')
            count +=1

    def mensagem_erro(self, mensagem):
        self.display_tabuleiro()
        print(f"\n{mensagem}\n")

    def jogada(self, posicao, jogador):
        if posicao > 9 or posicao <1:
            self.mensagem_erro('Jogada incorreta, escolha uma posição válida entre 1 até 9')
            return
        coordenada_jogada = self.obter_coordenada_jogada(posicao)

        jogada_correta = self.verificar_jogada(coordenada_jogada[0], coordenada_jogada[1])

        if not jogada_correta:
            self.mensagem_erro("Jogada incorreta, campo já jogado")
            return

        self.tabuleiro[coordenada_jogada[0]][coordenada_jogada[1]] = jogador.simbolo

        self.jogada_feita.append(posicao)
        self.display_tabuleiro()

        if self.verificar_vencedor(jogador):
            self.fim_jogo = True
            self.vencedor = jogador

        if len(self.jogada_feita) == 9:
            self.fim_jogo = True

    def jogada_maquina(self, maquina):
        while True:
            posicao = randint(1, 9)
            if posicao not in self.jogada_feita:
                break
        coordenada_jogada = self.obter_coordenada_jogada(posicao)

        self.tabuleiro[coordenada_jogada[0]][coordenada_jogada[1]] = maquina.simbolo
        self.jogada_feita.append(posicao)
        self.display_tabuleiro()

        if self.verificar_vencedor(maquina):
            self.fim_jogo = True
            self.vencedor = maquina

        if len(self.jogada_feita) == 9:
            self.fim_jogo = True

    def verificar_vencedor(self, jogador):
        simbolo_jogador = jogador.simbolo
        tabuleiro_y = [' ', ' ', ' '],\
                      [' ', ' ', ' '],\
                      [' ', ' ', ' ']
        tabuleiro_diagonal = [' ', ' ', ' '], [' ', ' ', ' ']
        for index in range(0,len(self.tabuleiro)):
            tabuleiro_y[0][index] = self.tabuleiro[index][0]
            tabuleiro_y[1][index] = self.tabuleiro[index][1]
            tabuleiro_y[2][index] = self.tabuleiro[index][2]
            if index == 0:
                tabuleiro_diagonal[0][0] = self.tabuleiro[index][0]
                tabuleiro_diagonal[1][0] = self.tabuleiro[index][2]
            if index == 1:
                tabuleiro_diagonal[0][1] = self.tabuleiro[index][1]
                tabuleiro_diagonal[1][1] = self.tabuleiro[index][1]
            if index == 2:
                tabuleiro_diagonal[0][2] = self.tabuleiro[index][2]
                tabuleiro_diagonal[1][2] = self.tabuleiro[index][0]
            if self.__verificar_simbolos_apartir_list(simbolo=simbolo_jogador, list=self.tabuleiro[index]) == 3:
                return True
        for tab in tabuleiro_y:
            if self.__verificar_simbolos_apartir_list(simbolo=simbolo_jogador, list=tab) == 3:
                return True
        for tab in tabuleiro_diagonal:
            if self.__verificar_simbolos_apartir_list(simbolo=simbolo_jogador, list=tab) == 3:
                return True
        return False


    def __verificar_simbolos_apartir_list(self, simbolo, list):
        count = 0
        for l in list:
            if l == simbolo:
                count += 1
        return count

    def verificar_jogada(self, posicaoX, posicaoY):
        if self.tabuleiro[posicaoX][posicaoY] == ' ':
            return True
        return False

    def obter_coordenada_jogada(self, posicao):
        posicaoX = int(posicao/3)
        posicaoY = posicao%3
        if posicaoY == 0:
            posicaoY = 2
            posicaoX =posicaoX - 1
        else:
            posicaoY -= 1

        return posicaoX, posicaoY



class Jogo:
    def __init__(self, jogador1,):
        self.jogador1 = jogador1


def start_game():
    jogador_hum = Jogador(1)
    jogador_pc = Jogador(2)
    while True:
        simbolo = input(f"Escolha os seguintes simbolos - {jogador_hum.simbolo_aceito}: \n")
        simbolo = int(simbolo)
        if int(simbolo) in jogador_hum.simbolo_aceito.keys():
            jogador_hum.definir_simbolo(simbolo)
            if simbolo == 1:
                jogador_pc.definir_simbolo(2)
            else:
                jogador_pc.definir_simbolo(1)
            break
    jv = JogoVelha(jogador_hum, jogador_pc)

    while True:
        try:
            posicao = int(input("Escolha posição da jogada que seja entre 1 - 9: \n"))
        except:
            continue
        jv.jogada(posicao, jogador_hum)

        if jv.fim_jogo:
            if jv.vencedor is not None:
                print(f"O {jv.vencedor.perfil} ganhou!!")
            else:
                print("Jogo Emparado!!!")
            break
        time_sleep = 0.35
        time.sleep(time_sleep)
        print('\n----------------------------------\n ')
        time.sleep(time_sleep)
        jv.jogada_maquina(jogador_pc)

        if jv.fim_jogo:
            if jv.vencedor is not None:
                print(f"O {jv.vencedor.perfil} ganhou!!")
            else:
                print("Jogo Emparado!!!")
            break

    print('fim de jogo')



if __name__ == '__main__':
    time_sleep = 0.35
    print('-' * 39)
    time.sleep(time_sleep)
    print('-' * 39)
    time.sleep(time_sleep)
    print('-' * 15 + 'Bem Vindo' + '-' * 15)
    time.sleep(time_sleep)
    print('-' * 39)
    time.sleep(time_sleep)
    print('-' * 39 + '\n')
    time.sleep(1)
    while True:
        print('Escolha as seguintes opções:\n')
        print('1) INICIAR JOGO\n')
        print('2) Sair')
        opcao = input('Escolha opção 1 ou 2: ')
        if opcao == '1':
            start_game()
            continue
        elif opcao == '2':
            print('Fim de Jogo')

            break
        else:
            print('opção incorreta')
            continue
