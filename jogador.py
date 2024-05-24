# Jogo da velha utilizando o algoritmo minimax
import math
import random

# Classe base para um jogador
class jogador_base:
    def __init__(self, carta):
        # 'carta' representa a jogada, X ou O
        self.carta = carta

    # Método para a próxima jogada, a ser implementado pelas subclasses
    def proxima_jogada(self, jogo):
        pass

# Classe para o jogador que é o computador
class jogador_computador(jogador_base):
    def __init__(self, carta):
        # Inicializa a classe base com a carta do jogador
        super().__init__(carta)

    # Método para a próxima jogada do computador
    def proxima_jogada(self, jogo):
        quadrado = random.choice(jogo.movimentos_possiveis)
        return quadrado


# Classe para o jogador humano
class jogador_humano(jogador_base):
    def __init__(self, carta):
        # Inicializa a classe base com a carta do jogador
        super().__init__(carta)
    
    # Método para a próxima jogada do humano
    def proxima_jogada(self, jogo):
        quadrado_valido = False
        val = None
        while not quadrado_valido:
            quadrado = input(self.carta +'\'s turn. Input move (0-8):')
            # Verificar se o valor que entrou é correto
            # Se sim, coloca. Se não, fala que é inválido
            # Se não tiver o lugar na borda, diz que não é válido
            # Resumindo, verificar se o que entrou é verdade
            try:
                val = int(quadrado)
                if val not in jogo.movimentos_possiveis():
                    raise ValueError
                quadrado_valido = True # Se sim, está correto
            except ValueError:
                print('Quadrado Inválido. Tente novamente.')
        return val

class jogador_esperto(jogador_base):
    def __init__(self,carta):
        super().__init__(carta)
    
    def proxima_jogada(self,jogo):
        if len(jogo.movimentos_possiveis()) == 9:
            quadrado = random.choice(jogo.movimentos_possiveis())
        else:
            quadrado = self.minimax(jogo,self.carta)['position']
        return quadrado

    def minimax(self, state,jogador_base):
        usuario_principal = self.carta # Usuário
        outro_jogador = 'O' if jogador_base == 'X' else 'X' # Cada um assume um

        # Verificar se o próximo movimento define o vencedor.
        if state.vencedor_atual == outro_jogador:
            return {
                'position': None, 
                'score': 1 * (state.numero_quadrados_vazios() + 1) if outro_jogador == usuario_principal else -1 * (state.numero_quadrados_vazios() + 1)
            }
        elif not state.quadrados_vazios():
            return {'position': None,'score': 0}
    
        if jogador_base == usuario_principal:
            melhor = {'position': None, 'score': -math.inf} # Cada pontuação vai maximizar
        else:
            melhor = {'position': None, 'score': math.inf} # Cada pontuação deve minimizar
        for possivel_movimento in state.movimentos_possiveis():
            state.faca_sua_jogada(possivel_movimento, jogador_base)
            pontuacao_sim = self.minimax(state,outro_jogador) # Simula o jogo depois de fazer aquele movimento.

            # Desfaz o movimento
            state.borda[possivel_movimento] = ' '
            state.vencedor_atual = None
            pontuacao_sim['position'] = possivel_movimento # Isso representa o próximo movimento ideal
        
            if jogador_base == usuario_principal: # X é o usuário
                if pontuacao_sim['score'] > melhor['score']:
                    melhor = pontuacao_sim
            else:
                if pontuacao_sim['score'] < melhor['score']:
                    melhor = pontuacao_sim
        return melhor

        
        