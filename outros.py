class Estado:
    """
    Classe padrão de estados.
    """
    def __init__(self, nome, numero, proximo=None):
        """
        Inicialização da classe estado.
        :param nome: String contendo o nome deste estado.
        :param numero: Integer contendo o número deste estado.
        :param proximo: String nomeando o próximo estado.
        """
        self.nome = nome
        self.numero = numero
        self.proximo = proximo

    def __str__(self):
        return self.nome

    def executa(self, **kwargs):
        """
        Executa o estado atual de acordo com parametros passados e retorna o próximo.
        :param kwargs: dicionário de parametros.
        :return:
        """
        pass

class Maquina:
    """
    Máquina de Estados.
    """
    def __init__(self, estados, inicial):
        """
        Estados deve ser um dicionário, inicial deve ser o primeiro estado.
        :param estados: lista de estados.
        :param inicial: estado inicial.
        """
        self.estados = self.inicializa(estados)
        self.atual = self.estados[inicial]

    def get_estado(self):
        return self.atual

    def set_estado(self, estado):
        self.atual = self.estados[estado]

    def get_proximo(self):
        proximo = self.atual.proximo
        if proximo:
            if proximo in self.estados:  # Se não existe o estado retorna nada. TODO: Subir erro?
                return self.estados[self.atual.proximo]
            else:
                print('Próximo estado: {}, não existe!!!'.format(proximo))
                return None
        return None

    def to_proximo(self):
        self.atual = self.get_proximo()

    @staticmethod
    def inicializa(estados):
        """
        Recebe uma lista de Estados e converte para um dicionário com o nome e objeto instanciado da classe.
        :param estados: lista ou dicionário de dados.
        :return: dicionario dos estados e nome.
        """
        if isinstance(estados, dict):
            return estados
        
        iniciados = dict()

        for estado in estados:
            obj = estado()
            nome = obj.nome
            iniciados[nome] = obj

        return iniciados

    def executa(self, **kwargs):
        """
        Executa o estado atual e vai para o próximo.
        :return: None.
        """
        self.atual.executa(**kwargs)

    def ciclo(self, **kwargs):
        """
        Percorre cada um dos estados, executa eles, até que o próximo seja None.
        :param kwargs:
        :return:
        """
        while self.atual is not None:
            self.executa(**kwargs)
            self.to_proximo()

def main():
    """
        Função principal da aplicação
    """
    
    print('inicializar algo')
    palavra = input("Digite ")

if __name__ == "__main__":
    main()


Python program for Finite Automata
Pattern searching Algorithm
 
NO_OF_CHARS = 256
 
def getNextState(pat, M, state, x):
    '''
    calculate the next state
    '''
 
    # If the character c is same as next character
      # in pattern, then simply increment state
 
    if state < M and x == ord(pat[state]):
        return state+1
 
    i=0
    # ns stores the result which is next state
 
    # ns finally contains the longest prefix
     # which is also suffix in "pat[0..state-1]c"
 
     # Start from the largest possible value and
      # stop when you find a prefix which is also suffix
    for ns in range(state,0,-1):
        if ord(pat[ns-1]) == x:
            while(i<ns-1):
                if pat[i] != pat[state-ns+1+i]:
                    break
                i+=1
            if i == ns-1:
                return ns
    return 0
 
def computeTF(pat, M):
    '''
    This function builds the TF table which
    represents Finite Automata for a given pattern
    '''
    global NO_OF_CHARS
 
    TF = [[0 for i in range(NO_OF_CHARS)]\
          for _ in range(M+1)]
 
    for state in range(M+1):
        for x in range(NO_OF_CHARS):
            z = getNextState(pat, M, state, x)
            TF[state][x] = z
 
    return TF
 
def search(pat, txt):
    '''
    Prints all occurrences of pat in txt
    '''
    global NO_OF_CHARS
    M = len(pat)
    N = len(txt)
    TF = computeTF(pat, M)   
 
    # Process txt over FA.
    state=0
    for i in range(N):
        state = TF[state][ord(txt[i])]
        if state == M:
            print("Pattern found at index: {}".\
                   format(i-M+1))
 
Driver program to test above function    