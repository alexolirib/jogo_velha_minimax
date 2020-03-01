class Jogador:
    def __init__(self):
        self.perfil=None
        self.perfil_aceito = {1:'usuario', 2:'pc'}
        self.simbolo=None
        self.simbolo_aceito = {1:'X', 2:'Y'}

    def definir_perfil(self, perfil):
        self.perfil = self.perfil_aceito[perfil]

    def definir_simbolo(self, simbolo):
        self.simbolo = self.simbolo_aceito[simbolo]

class JogoVelha:
    def __init__(self, jogador1, jogador2):
        self.tabuleiro = ['', '', ''],\
                         ['', '', ''],\
                         ['', '', '']
        self.jogador1 = jogador1
        self.jogador2 = jogador2

    def display_tabuleiro(self):
        pass

    def jogada(self, posicao):
        if posicao > 9 or posicao <1:
            print('Jogar Incorreta, escolha uma posição válida entre 1 até 9')

class Jogo:
    def __init__(self, jogador1,):
        self.jogador1 = jogador1


def main():
    pass


if __name__ == '__main__':
    main()
