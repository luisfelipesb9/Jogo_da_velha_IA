import math
import time
from jogador import jogador_computador, jogador_esperto, jogador_humano

class jogo_da_velha:
    def __init__(self):
        self.borda = self.fazer_borda() # Para o tabuleiro 3x3 será utilizada uma só lista
        self.vencedor_atual = None # Indicar quem venceu

    @staticmethod
    def fazer_borda():
        return[' ' for _ in range(9)]

    def print_borda(self):
        # Só pega as linhas
        for linha in [self.borda[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(linha) + ' |')

    @staticmethod
    def print_borda_numeros():
        # 0 | 1 | 2 ... diz o número correspondente a cada casa do tabuleiro
        numero_da_borda = [[str(i) for i in range(j*3, (j+1) * 3)] for j in range(3)]
        for linha in numero_da_borda:
            print('| ' + ' | '.join(linha) + ' |')
    
    def faca_sua_jogada(self, quadrado, carta): # make_move
        # Realiza a jogada
        if self.borda[quadrado] == ' ':
            self.borda[quadrado] = carta
            if self.vencedor(quadrado, carta):
                self.vencedor_atual = carta
            return True
        return False

    def vencedor(self, quadrado, carta):
        # Checar as 3 linhas de qualquer jeito.
        indice_linha = math.floor(quadrado / 3)
        linha = self.borda[indice_linha * 3 : (indice_linha + 1) * 3]
        if all([s == carta for s in linha]):
            return True

        # Conferir a coluna
        indice_coluna = quadrado % 3
        coluna = [self.borda[indice_coluna + i * 3] for i in range(3)]
        if all([s == carta for s in coluna]):
            return True
        # Verificar diagonais
        # Somente os movimentos que são possíveis ganhar
        # (0, 2, 4, 6, 8)
        if quadrado % 2 == 0:
            diagonal1 = [self.borda[i] for i in [0, 4, 8]]  # Esquerda para direita
            if all([s == carta for s in diagonal1]):
                return True
            diagonal2 = [self.borda[i] for i in [2, 4, 6]]  # Direita para esquerda
            if all([s == carta for s in diagonal2]):
                return True
        return False
            # Se der tudo errado, então não foi na diagonal.

    def movimentos_possiveis(self):
        return [i for i, x in enumerate(self.borda) if x == " "]

    def quadrados_vazios(self):
        return ' ' in self.borda

    def numero_quadrados_vazios(self):
        return self.borda.count(' ')

def jogar(jogo, jogador_x, jogador_o, print_jogo=True):
    # Vai retornar o vencedor do jogo com a carta 
    # None representa um empate.

    if print_jogo:
        jogo.print_borda_numeros()
    
    carta = 'X' 
        # A que vai iniciar, continua enquanto tiver quadrados vazios.
        # Deixa jogar sozinho, não importa o vencedor
        # Implementação, para quebrar o loop.
    while jogo.quadrados_vazios():
        # Ordenar a vez do jogador correspondente
        if carta == 'O':
            quadrado = jogador_o.proxima_jogada(jogo)
        else:
            quadrado = jogador_x.proxima_jogada(jogo)

            # Função para fazer uma jogada.
        if jogo.faca_sua_jogada(quadrado, carta):
            if print_jogo:
                print(carta + f' faz uma jogada no quadrado {quadrado}')
                jogo.print_borda()
                print('') # Linha vazia

            if jogo.vencedor_atual:
                if print_jogo:
                    print(carta + ' venceu!')
                return carta # Acaba o jogo

                # Fez uma jogada, precisamos alternar a vez
            carta = 'O' if carta == 'X' else 'X'
        
        time.sleep(.8)

    if print_jogo:
        print('Empatou!')


if __name__ == '__main__':
    jogador_x = jogador_esperto('X')
    jogador_o = jogador_humano('O')
    t = jogo_da_velha()
    jogar(t, jogador_x, jogador_o, print_jogo=True)
