import customtkinter as ctk

#Gerencia as janelas abertas para garantir o menor uso de Memoria com janelas inativas.

#variaveis de posição padrão
        
posicao_botaox = 0.02
posicao_botaoy = 0.3
tamanho_botao = 0.27

class GerenciadorJanelas:

    def __init__(self):


        
        #Gerando a janela de menu inicial

        self.menu = ctk.CTk()
        self.menu.title('Comercio Estoque - Menu Inicial')
        self.menu.geometry('600x600')

        #adcionando os botões para as demais janelas.

        cad_fornecedor_botao = ctk.CTkButton(self.menu, text='Cadastro de Fornecedor', command=self.cadastro_fornecedor)
        cad_categoria_botao = ctk.CTkButton(self.menu, text='Cadastro de Categoria', command=self.cadastro_categoria)
        cad_item_botao = ctk.CTkButton(self.menu, text='Cadastro de Itens')
        ent_item_botao = ctk.CTkButton(self.menu, text='Entrada de Item')
        con_estq_botao = ctk.CTkButton(self.menu, text='Consulta de Estoque')
        venda_botao = ctk.CTkButton(self.menu, text='Venda de Itens')

        cad_fornecedor_botao.place(relx=posicao_botaox, rely=posicao_botaoy, relwidth=tamanho_botao)
        cad_categoria_botao.place(relx=posicao_botaox, rely=posicao_botaoy + 0.055 * 1, relwidth=tamanho_botao)
        cad_item_botao.place(relx=posicao_botaox, rely=posicao_botaoy+ 0.055 * 2, relwidth=tamanho_botao)
        ent_item_botao.place(relx=posicao_botaox, rely=posicao_botaoy+ 0.055 * 3, relwidth=tamanho_botao)
        con_estq_botao.place(relx=posicao_botaox, rely=posicao_botaoy+ 0.055 * 4, relwidth=tamanho_botao)
        venda_botao.place(relx=posicao_botaox, rely=posicao_botaoy+ 0.055 * 5, relwidth=tamanho_botao)

        #cria variavel que recebera o valor de uma janela em execução
        self.janela = None

    
    #Criação de janelas 
    def cadastro_fornecedor(self):
        if self.janela is None:
            self.janela = ctk.CTk()
            self.janela.title('Comercio Estoque - Cadastro Fornecedor')
            self.janela.geometry('600x600')
            #chama a função fechar_janela quando o evento de fechar a jenala ativa for ativado.
            self.janela.protocol('WM_DELETE_WINDOW', self.fechar_janela)

            botao_teste = ctk.CTkButton(self.janela, text='Teste Fornecedor')
            botao_teste.place(relx=posicao_botaox, rely=posicao_botaoy, relwidth=tamanho_botao)
            
            #exibie a janela ativa ocultando a janela menu
            self.janela.deiconify()
            self.menu.withdraw()

    def cadastro_categoria(self):
        if self.janela is None:
            self.janela = ctk.CTk()
            self.janela.title('comercio Estoque - Cadastro Categoria')
            self.janela.geometry('600x600')
            #chama a função fechar_janela quando o evento de fechar a jenala ativa for ativado.
            self.janela.protocol('WM_DELETE_WINDOW', self.fechar_janela)

            botao_teste = ctk.CTkButton(self.janela, text='Teste Categoria')
            botao_teste.place(relx=posicao_botaox, rely=posicao_botaoy, relwidth=tamanho_botao)

            #exibie a janela ativa ocultando a janela menu
            self.janela.deiconify()
            self.menu.withdraw()





    #função de encerramento de janela e liberação de memoria
    def fechar_janela(self):
        if self.janela:
            self.janela.destroy()
            self.janela = None
        
        self.menu.deiconify()
    
    
    #função para iniciar a janela inicial (essencial para as demais janelas)
    def run(self):
        self.menu.mainloop()

if __name__ == '__main__':
    ctk.set_appearance_mode('dark')
    gerenciador = GerenciadorJanelas()
    gerenciador.run()