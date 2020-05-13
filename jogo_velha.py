import time
from random import randint, random
from copy import deepcopy



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
        self.jogada_correta = False
        # self.display_tabuleiro()

    def display_tabuleiro(self):
        count = 0
        for linha in self.tabuleiro:
            print(str(linha).replace('[','').replace(']','').replace(',','|'))
            if count in (0,1):
                print('---------------')
            count +=1

    def mensagem_erro(self, mensagem):
        self.display_tabuleiro()
        self.jogada_correta = False
        print(f"\n{mensagem}\n")

    def jogada(self, posicao, jogador):
        self.jogada_correta = False
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

        self.jogada_correta = True

    def jogada_maquina(self, maquina):
        if maquina.simbolo == 'X':
            hum_simbolo = 'O'
        else:
            hum_simbolo = 'X'

        #verificar se é possivel vencer na proxima jogada
        for i in range(1,10):
            tabuleiro_y = deepcopy(self.tabuleiro)
            if i not in self.jogada_feita:
                cood_jod = self.obter_coordenada_jogada(i)
                tabuleiro_y[cood_jod[0]][cood_jod[1]] = maquina.simbolo
                if self.verificar_vencedor(simbolo_jogador=maquina.simbolo, tabuleiro=tabuleiro_y):
                    self.tabuleiro[cood_jod[0]][cood_jod[1]] = maquina.simbolo
                    self.jogada_feita.append(i)
                    self.display_tabuleiro()
                    return

        #verificar se o jogador pode vencer na próxima rodada
        for i in range(1,10):
            tabuleiro_y = deepcopy(self.tabuleiro)
            if i not in self.jogada_feita:
                cood_jod = self.obter_coordenada_jogada(i)
                tabuleiro_y[cood_jod[0]][cood_jod[1]] = hum_simbolo
                if self.verificar_vencedor(simbolo_jogador=hum_simbolo, tabuleiro=tabuleiro_y):
                    self.tabuleiro[cood_jod[0]][cood_jod[1]] = maquina.simbolo
                    self.jogada_feita.append(i)
                    self.display_tabuleiro()
                    return

        jogada = self.mov_aleatorio([1, 3, 7, 9])
        if jogada:
            cood_jod = self.obter_coordenada_jogada(jogada)
            self.tabuleiro[cood_jod[0]][cood_jod[1]] = maquina.simbolo
            self.jogada_feita.append(jogada)
            self.display_tabuleiro()
            return

        if 5 not in self.jogada_feita:
            cood_jod = self.obter_coordenada_jogada(5)
            self.tabuleiro[cood_jod[0]][cood_jod[1]] = maquina.simbolo
            self.jogada_feita.append(5)
            self.display_tabuleiro()
            return

        jogada = self.mov_aleatorio([2, 4, 6, 8])
        if jogada:
            cood_jod = self.obter_coordenada_jogada(jogada)
            self.tabuleiro[cood_jod[0]][cood_jod[1]] = maquina.simbolo
            self.jogada_feita.append(jogada)
            self.display_tabuleiro()
            return



    def mov_aleatorio(self, list_mov):
        mov_possivel = []
        for i in list_mov:
            if i not in self.jogada_feita:
                mov_possivel.append(i)
        if mov_possivel:
            import random
            return random.choice(mov_possivel)
        return None

    def verificar_vencedor(self, simbolo_jogador, tabuleiro):
        tabuleiro_y = [' ', ' ', ' '],\
                      [' ', ' ', ' '],\
                      [' ', ' ', ' ']
        tabuleiro_diagonal = [' ', ' ', ' '], [' ', ' ', ' ']
        for index in range(0,len(tabuleiro)):
            tabuleiro_y[0][index] = tabuleiro[index][0]
            tabuleiro_y[1][index] = tabuleiro[index][1]
            tabuleiro_y[2][index] = tabuleiro[index][2]
            if index == 0:
                tabuleiro_diagonal[0][0] = tabuleiro[index][0]
                tabuleiro_diagonal[1][0] = tabuleiro[index][2]
            if index == 1:
                tabuleiro_diagonal[0][1] = tabuleiro[index][1]
                tabuleiro_diagonal[1][1] = tabuleiro[index][1]
            if index == 2:
                tabuleiro_diagonal[0][2] = tabuleiro[index][2]
                tabuleiro_diagonal[1][2] = tabuleiro[index][0]
            if self.__verificar_simbolos_apartir_list(simbolo=simbolo_jogador, list=tabuleiro[index]) == 3:
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



def jogaPrimeiro():

    if randint(0, 1) == 0:
        return 'pc'
    else:
        return 'hum'

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

    turno = jogaPrimeiro()

    while True:
        if turno == 'hum':

            jogador = jogador_hum
            while not jv.jogada_correta:
                try:
                    posicao = int(input("Escolha posição da jogada que seja entre 1 - 9: \n"))
                except:
                    continue
                jv.jogada(posicao, jogador)

        else:
            jogador = jogador_pc
            jv.jogada_maquina(jogador)

        if jv.verificar_vencedor(simbolo_jogador=jogador.simbolo,tabuleiro=jv.tabuleiro):
            jv.fim_jogo = True
            jv.vencedor = jogador

        if len(jv.jogada_feita) == 9:
            jv.fim_jogo = True
        jv.jogada_correta = False
        time_sleep = 0.35
        time.sleep(time_sleep)
        print('\n----------------------------------\n ')
        time.sleep(time_sleep)
        # jv.jogada_maquina(jogador_pc)

        if jv.fim_jogo:
            if jv.vencedor is not None:
                print(f"O {jv.vencedor.perfil} ganhou!!")
            else:
                print("Jogo Emparado!!!")
            break

        if turno == 'hum':
            turno = 'pc'
        else:
            turno = 'hum'

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
