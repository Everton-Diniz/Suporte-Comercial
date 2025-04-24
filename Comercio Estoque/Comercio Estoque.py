import customtkinter as ctk

#Gerencia as janelas abertas para garantir o menor uso de Memoria com janelas inativas.

class GerenciadorJanelas:
    def __init__(self):

        #variaveis de posição padrão
        
        posicao_botaox = 0.02
        posicao_botaoy = 0.3
        tamanho_botao = 0.27
        
        #Gerando a janela de menu inicial

        self.menu = ctk.CTk()
        self.menu.title('Comercio Estoque - Menu Inicial')
        self.menu.geometry('600x600')

        #adcionando os botões para as demais janelas.

        cad_fornecedor_botao = ctk.CTkButton(self.menu, text='Cadastro de Fornecedor')
        cad_categoria_botao = ctk.CTkButton(self.menu, text='Cadastro de Categoria')
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

    
    def run(self):
        self.menu.mainloop()

if __name__ == '__main__':
    ctk.set_appearance_mode('dark')
    gerenciador = GerenciadorJanelas()
    gerenciador.run()