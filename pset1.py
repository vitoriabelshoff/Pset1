# IDENTIFICAÇÃO DO ESTUDANTE:
# Preencha seus dados e leia a declaração de honestidade abaixo. NÃO APAGUE
# nenhuma linha deste comentário de seu código!
#
#    Nome completo: Vitória Pizzol Belshoff
#    Matrícula: 202200875
#    Turma: CC3M
#    Email: vitoriapbelshoff@gmail.com
#
# DECLARAÇÃO DE HONESTIDADE ACADÊMICA:
# Eu afirmo que o código abaixo foi de minha autoria. Também afirmo que não
# pratiquei nenhuma forma de "cola" ou "plágio" na elaboração do programa,
# e que não violei nenhuma das normas de integridade acadêmica da disciplina.
# Estou ciente de que todo código enviado será verificado automaticamente
# contra plágio e que caso eu tenha praticado qualquer atividade proibida
# conforme as normas da disciplina, estou sujeito à penalidades conforme
# definidas pelo professor da disciplina e/ou instituição.
#


# Imports permitidos (não utilize nenhum outro import!):
import sys
import math
import base64
import tkinter
from io import BytesIO
from PIL import Image as PILImage

#Definindo uma função Kernel
#A fração garante a igualdade dos elementos de kernel
def kernelMaker(n):
    kernel = [[1 / (n**2) for i in range(n)] for i in range(n)]
    return kernel

# Classe Imagem:
class Imagem:
    def __init__(self, largura, altura, pixels):
        self.largura = largura
        self.altura = altura
        self.pixels = pixels

    def get_pixel(self, x, y):
        #Definindo o valor mínimo = 0 com a função "max"
        #Definindo o valor máximo de x e y, largura -1       
        x = max(0, min(x, self.largura - 1))
        y = max(0, min(y, self.altura - 1))
        return self.pixels[(x + y * self.largura)]

    def set_pixel(self, x, y, c):
        self.pixels[(x + y * self.largura)] = c

    def aplicar_por_pixel(self, func):
        resultado = Imagem.nova(self.largura, self.altura)
        for x in range(resultado.largura):
            nova_cor = ""
            y = ""
            for y in range(resultado.altura):
                cor = self.get_pixel(x, y)
                nova_cor = func(cor)
                resultado.set_pixel(x, y, nova_cor)
        return resultado

    def invertida(self):
        return self.aplicar_por_pixel(lambda c: 255 - c)

    def correlacao(self, n):
        #Len é usado para ter o tamanho do kernel
        kernelT = len(n)
        img = Imagem.nova(self.largura, self.altura)
        
        #Dois loops for, um para x e outro para y, são usados para percorrer todos os pixels da imagem
        for x in range(self.largura):
            for y in range(self.altura):
                #irá armazenar a soma da correlação
                Soma = sum(
                    #Multiplica cada elemento do kernel com o pixel correspondente na imagem
                    self.get_pixel(x - (kernelT // 2) + z, y - (kernelT // 2) + w) * n[z][w]
                    for z in range(kernelT)
                    for w in range(kernelT)
                )
                #Define o pixel na posição (x, y) como a soma da correlação
                img.set_pixel(x, y, Soma)
    
        return img
                    
    def borrada(self, n):
        #Gera um kernel a partir do parâmetro n e aplica a correlação
        kernel = self.correlacao(kernelMaker(n))
        #Normaliza os valores dos pixels no kernel resultante
        kernel.PixelNormal()
        #Retorna o kernel borrado
        return kernel
        
    def PixelNormal(self):
        #Percorre cada pixel da imagem
        for x in range(self.largura):
            for y in range(self.altura):
                analyzedPixel = self.get_pixel(x,y)

                #Condicional para impedir que os pixels tenham valores menores que 0
                if  analyzedPixel < 0:
                    analyzedPixel = 0
                    
                #Condicional para impedir que os pixels tenham valores maiores que 255
                elif analyzedPixel > 255:
                    analyzedPixel = 255
                
                #Arredonda o valor do pixel para um número inteiro, ja que os pixels não podem ter valores flutuantes
                analyzedPixel = round(analyzedPixel)
                
                #Atualiza o pixel na posição (x, y) com o valor analisado
                self.set_pixel(x,y, analyzedPixel)    


    def focada(self, n):
        # Obtém a imagem borrada usando o kernel n
        ImagemBorrada = self.borrada(n)
        #Cria uma nova imagem vazia com as mesmas dimensões
        img = Imagem.nova(self.largura, self.altura)
        
        #Percorre cada pixel da imagem
        for x in range(self.largura):
            for y in range(self.altura):
                #Calcula a fórmula para o pixel focado
                FocadaFormula = round(2 * self.get_pixel(x,y) - (ImagemBorrada.get_pixel(x, y)))
                #Define o pixel da imagem resultante com o valor calculado
                img.set_pixel(x, y, FocadaFormula)
        #Aplica a normalização dos pixels
        img.PixelNormal()
        return img

    def bordas(self):
        #Cria uma nova imagem vazia com as mesmas dimensões
        img = Imagem.nova(self.largura, self.altura)
        #Usa o Kernel Sobel para detecção de bordas na direção X e Y
        kernelSobelX = [[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]]

        kernelSobelY = [[-1, -2, -1],
                        [0, 0, 0],
                        [1, 2, 1]]
                        
        #Aplica a correlação do kernel Sobel X e Y na imagem
        AplicacaoX = self.correlacao(kernelSobelX)
        AplicacaoY = self.correlacao(kernelSobelY)


        for x in range(self.largura):
            for y in range(self.altura):
                #Usa o operador sobel pra calcular a borda
                Sobel = round(math.sqrt(AplicacaoX.get_pixel(x,y)**2 + AplicacaoY.get_pixel(x,y)**2))
                #Define o pixel da imagem resultante com o valor calculado
                img.set_pixel(x, y, Sobel)
        #Normaliza os valores dos pixels na imagem resultante
        img.PixelNormal()
        
        return img

    # Abaixo deste ponto estão utilitários para carregar, salvar e mostrar
    # as imagens, bem como para a realização de testes.

    def __eq__(self, other):
        return all(getattr(self, i) == getattr(other, i)
                   for i in ('altura', 'largura', 'pixels'))

    def __repr__(self):
        return "Imagem(%s, %s, %s)" % (self.largura, self.altura, self.pixels)

    @classmethod
    def carregar(cls, nome_arquivo):
        """
        Carrega uma imagem do arquivo fornecido e retorna uma instância dessa
        classe representando essa imagem. Também realiza a conversão para tons
        de cinza.

        Invocado como, por exemplo:
           i = Imagem.carregar('test_images/cat.png')
        """
        with open(nome_arquivo, 'rb') as guia_para_imagem:
            img = PILImage.open(guia_para_imagem)
            img_data = img.getdata()
            if img.mode.startswith('RGB'):
                pixels = [round(.299 * p[0] + .587 * p[1] + .114 * p[2]) for p in img_data]
            elif img.mode == 'LA':
                pixels = [p[0] for p in img_data]
            elif img.mode == 'L':
                pixels = list(img_data)
            else:
                raise ValueError('Modo de imagem não suportado: %r' % img.mode)
            l, a = img.size
            return cls(l, a, pixels)

    @classmethod
    def nova(cls, largura, altura):
        """
        Cria imagens em branco (tudo 0) com a altura e largura fornecidas.

        Invocado como, por exemplo:
            i = Imagem.nova(640, 480)
        """
        return cls(largura, altura, [0 for i in range(largura * altura)])

    def salvar(self, nome_arquivo, modo='PNG'):
        """
        Salva a imagem fornecida no disco ou em um objeto semelhante a um arquivo.
        Se o nome_arquivo for fornecido como uma string, o tipo de arquivo será
        inferido a partir do nome fornecido. Se nome_arquivo for fornecido como
        um objeto semelhante a um arquivo, o tipo de arquivo será determinado
        pelo parâmetro 'modo'.
        """
        saida = PILImage.new(mode='L', size=(self.largura, self.altura))
        saida.putdata(self.pixels)
        if isinstance(nome_arquivo, str):
            saida.save(nome_arquivo)
        else:
            saida.save(nome_arquivo, modo)
        saida.close()

    def gif_data(self):
        """
        Retorna uma string codificada em base 64, contendo a imagem
        fornecida, como uma imagem GIF.

        Função utilitária para tornar show_image um pouco mais limpo.
        """
        buffer = BytesIO()
        self.salvar(buffer, modo='GIF')
        return base64.b64encode(buffer.getvalue())

    def mostrar(self):
        """
        Mostra uma imagem em uma nova janela Tk.
        """
        global WINDOWS_OPENED
        if tk_root is None:
            # Se Tk não foi inicializado corretamente, não faz mais nada.
            return
        WINDOWS_OPENED = True
        toplevel = tkinter.Toplevel()
        # O highlightthickness=0 é um hack para evitar que o redimensionamento da janela
        # dispare outro evento de redimensionamento (causando um loop infinito de
        # redimensionamento). Para maiores informações, ver:
        # https://stackoverflow.com/questions/22838255/tkinter-canvas-resizing-automatically
        tela = tkinter.Canvas(toplevel, height=self.altura,
                              width=self.largura, highlightthickness=0)
        tela.pack()
        tela.img = tkinter.PhotoImage(data=self.gif_data())
        tela.create_image(0, 0, image=tela.img, anchor=tkinter.NW)

        def ao_redimensionar(event):
            # Lida com o redimensionamento da imagem quando a tela é redimensionada.
            # O procedimento é:
            #  * converter para uma imagem PIL
            #  * redimensionar aquela imagem
            #  * obter os dados GIF codificados em base 64 (base64-encoded GIF data)
            #    a partir da imagem redimensionada
            #  * colocar isso em um label tkinter
            #  * mostrar a imagem na tela
            nova_imagem = PILImage.new(mode='L', size=(self.largura, self.altura))
            nova_imagem.putdata(self.pixels)
            nova_imagem = nova_imagem.resize((event.largura, event.altura), PILImage.NEAREST)
            buffer = BytesIO()
            nova_imagem.save(buffer, 'GIF')
            tela.img = tkinter.PhotoImage(data=base64.b64encode(buffer.getvalue()))
            tela.configure(height=event.altura, width=event.largura)
            tela.create_image(0, 0, image=tela.img, anchor=tkinter.NW)

        # Por fim, faz o bind da função para que ela seja chamada quando a tela
        # for redimensionada:
        tela.bind('<Configure>', ao_redimensionar)
        toplevel.bind('<Configure>', lambda e: tela.configure(height=e.altura, width=e.largura))

        # Quando a tela é fechada, o programa deve parar
        toplevel.protocol('WM_DELETE_WINDOW', tk_root.destroy)


# Não altere o comentário abaixo:
# noinspection PyBroadException
try:
    tk_root = tkinter.Tk()
    tk_root.withdraw()
    tcl = tkinter.Tcl()


    def refaz_apos():
        tcl.after(500, refaz_apos)


    tcl.after(500, refaz_apos)
except:
    tk_root = None

WINDOWS_OPENED = False

if __name__ == '__main__':
    # O código neste bloco só será executado quando você executar
    # explicitamente seu script e não quando os testes estiverem
    # sendo executados. Este é um bom lugar para gerar imagens, etc.
   
    # Questão 2
    peixe = Imagem.carregar('test_images/bluegill.png')
    PeixeInvertido = peixe.invertida()
    Imagem.salvar(PeixeInvertido, 'imgs_respostas/peixe.png')
    
    # Questão 4
    kernel = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [1, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    porco = Imagem.carregar('test_images/pigbird.png')
    PorcoCorr = porco.correlacao(kernel)
    Imagem.salvar(PorcoCorr, 'imgs_respostas/porcopassaro.png')
    
    # Questão 5
    gato = Imagem.carregar('test_images/cat.png')
    GatoBorrado = gato.borrada(5)
    Imagem.salvar(GatoBorrado,'imgs_respostas/gato.png')


    python = Imagem.carregar('test_images/python.png')
    PythonFocada = python.focada(11)
    Imagem.salvar(PythonFocada,'imgs_respostas/python.png')
    
    # Questão 6:

    kernelSobelX = [[1, 0, -1],
                    [2, 0, -2],
                    [1, 0, -1]]

    kernelSobelY = [[1, 2, 1],
                    [0, 0, 0],
                    [-1, -2, -1]]

    Const = Imagem.carregar('test_images/construct.png')
    ConstSobelX = Const.correlacao(kernelSobelX)
    Imagem.salvar(ConstSobelX, 'imgs_respostas/construc_sobel_X.png')

    ConstSobelY = Const.correlacao(kernelSobelY)
    Imagem.salvar(ConstSobelY, 'imgs_respostas/construc_sobel_Y.png')

    BordasConst = Const.bordas()
    Imagem.salvar(BordasConst, 'imgs_respostas/construcao.png')

    pass

    Imagem.mostrar(PeixeInvertido)
    Imagem.mostrar(GatoBorrado)
    Imagem.mostrar(PorcoCorr)
    Imagem.mostrar(PythonFocada)
    Imagem.mostrar(BordasConst)

    
    # O código a seguir fará com que as janelas de Imagem.mostrar
    # sejam exibidas corretamente, quer estejamos executando
    # interativamente ou não:
    if WINDOWS_OPENED and not sys.flags.interactive:
        tk_root.mainloop()
