class IterMusica(type):
    def __iter__(cls):
        return iter(cls.instances)

class Musica(metaclass=IterMusica):
    instances = []
    def __init__(self, nome, letra):
        self.__class__.instances.append(self)
        self.nome = nome
        self.letra = letra
        
    def __str__(self):
        return self.nome

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
        2ª Verificação se a string digitada está na letra
    """
    
    import os


    registrar_musicas()

    palavra = input("Digite uma palavra: ")

    for musica in Musica:
        print(f'Verificando a música "{ musica.nome }"...')

        if palavra in musica.letra:
            print(f'A música "{ musica.nome }" contém a palavra "{ palavra }" em sua letra!')

            print('Reproduzindo a música...')
            os.startfile(f'mp3\\{ musica.nome }.mp3')
        else:
            print(f'A música "{ musica.nome }" não contém a palavra "{ palavra }" em sua letra!')

if __name__ == '__main__':
    
    main()