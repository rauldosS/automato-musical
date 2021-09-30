class Musica:
    instances = []
    def __init__(self, nome, letra):
        self.__class__.instances.append(self)
        self.nome = nome
        self.letra = letra
        
    def __str__(self):
        return self.nome

    def get_letras(self):
        pass

def registrar_musicas():
    import os

    pasta = 'musicas'

    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]

    txts = [arq for arq in arquivos if arq.lower().endswith(".txt")]

    for musica in txts:
        with open(musica, 'r') as letra:
            # print(arquivo.replace('.txt', ''))
            Musica(musica.replace('.txt', '').replace(f'{ pasta }\\', ''), letra.read().replace('\n', '').replace(',', '').split(' '))

def main():
    """
        Função principal da aplicação

        1ª Entrada
        2ª 
    """
    
    import os

    os.startfile('ameno.mp3')

    registrar_musicas()

    palavra = input("Digite uma palavra: ")

    print(Musica.instances)

    for musica in Musica.instances:
        print(f'Verificando a música "{ musica.nome }"...')

        print(f'A música "{ musica.nome }" { "contém" if palavra in musica else "não contem" } a palavra "{ palavra }" em sua letra!')

if __name__ == '__main__':
    
    main()


# def funcao_um:
#   funcao_dois(self, nome_da_musica)

# def funcao_dois:
#   funcao_tres()

# def funcao_tres:
#   funcao_um()