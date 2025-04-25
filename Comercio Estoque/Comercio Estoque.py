import customtkinter as ctk

#Gerencia as janelas abertas para garantir o menor uso de Memoria com janelas inativas.
class GerenciadorJanelas:

    def __init__(self):
        
        #Gerando a janela de menu inicial
        self.menu = ctk.CTk()
        self.menu.title('Comercio Estoque - Menu Inicial')
        self.menu.geometry('600x600')

        #variaveis de posição padrão
        posicao_botaox = 0.02
        posicao_botaoy = 0.3
        tamanho_botao = 0.27

        #adcionando os botões para as demais janelas.
        cad_fornecedor_botao = ctk.CTkButton(self.menu, text='Cadastro de Fornecedor', command=self.cadastro_fornecedor)
        cad_categoria_botao = ctk.CTkButton(self.menu, text='Cadastro de Categoria', command=self.cadastro_categoria)
        cad_item_botao = ctk.CTkButton(self.menu, text='Cadastro de Itens', command=self.cadastro_itens)
        ent_item_botao = ctk.CTkButton(self.menu, text='Entrada de NF')
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
            self.janela.geometry('600x300')
            #chama a função fechar_janela quando o evento de fechar a jenala ativa for ativado.
            self.janela.protocol('WM_DELETE_WINDOW', self.fechar_janela)

            fonte_padrao = ('arial', 15, 'bold')
            posicao_x = 0.02
            posicao_y = 0.1
    
            #titulos
            titulo_nome_forn = ctk.CTkLabel(self.janela, text='Nome do Fornecedor:', font=fonte_padrao)
            titulo_nome_repr = ctk.CTkLabel(self.janela, text='Nome do Representante de Vendas:', font=fonte_padrao)
            titulo_cnpj = ctk.CTkLabel(self.janela, text='CNPJ:', font=fonte_padrao)
            #campos
            campo_nome_forn = ctk.CTkEntry(self.janela, placeholder_text='Insira o Nome do Fornecedor.')
            campo_nome_repr = ctk.CTkEntry(self.janela, placeholder_text='Insira o Nome do Representante.')
            campo_cnpj = ctk.CTkEntry(self.janela, placeholder_text='insira o CNPJ.')
            #botoes
            botao_confirmar = ctk.CTkButton(self.janela, text='Confirmar', fg_color='#008080', font=fonte_padrao)
            botao_apagar = ctk.CTkButton(self.janela, text='Apagar', fg_color='#8b0000', font=fonte_padrao)

            #posicionamento
            titulo_nome_forn.place(relx=posicao_x, rely=posicao_y)
            campo_nome_forn.place(relx=posicao_x, rely=posicao_y * 2, relwidth=0.6)

            titulo_nome_repr.place(relx=posicao_x, rely=posicao_y * 3)
            campo_nome_repr.place(relx=posicao_x, rely=posicao_y * 4, relwidth=0.6)

            titulo_cnpj.place(relx=posicao_x, rely=posicao_y * 5)
            campo_cnpj.place(relx=posicao_x, rely=posicao_y * 6, relwidth=0.23)

            botao_confirmar.place(relx=posicao_x, rely=posicao_y * 8.7)
            botao_apagar.place(relx=posicao_x * 13.7, rely=posicao_y * 8.7)

            #exibi a janela ativa ocultando a janela menu
            self.abrir_janela()

    def cadastro_categoria(self):
        if self.janela is None:
            self.janela = ctk.CTk()
            self.janela.title('Comercio Estoque - Cadastro Categoria')
            self.janela.geometry('600x200')
            #chama a função fechar_janela quando o evento de fechar a jenala ativa for ativado.
            self.janela.protocol('WM_DELETE_WINDOW', self.fechar_janela)

            fonte_padrao = ('arial', 15, 'bold')
            posicao_x = 0.02
            posicao_y = 0.15

            #titulos
            titulo_categoria = ctk.CTkLabel(self.janela, text='Categoria:', font=fonte_padrao)
            
            #campos
            campo_categoria = ctk.CTkEntry(self.janela, placeholder_text='Insira o Nome da Categoria.')

            #botões
            botao_confirmar = ctk.CTkButton(self.janela, text='Confirmar', fg_color='#008080', font=fonte_padrao)
            botao_apagar = ctk.CTkButton(self.janela, text='Apagar', fg_color='#8b0000', font=fonte_padrao)

            #posicionamento
            titulo_categoria.place(relx=posicao_x, rely=posicao_y)

            campo_categoria.place(relx=posicao_x, rely=posicao_y * 2, relwidth=0.6)

            botao_confirmar.place(relx=posicao_x, rely=posicao_y * 5.4)
            botao_apagar.place(relx=posicao_x * 13.7, rely=posicao_y * 5.4)


            #exibi a janela ativa ocultando a janela menu
            self.abrir_janela()

    def cadastro_itens(self):
        if self.janela is None:
            self.janela = ctk.CTk()
            self.janela.title('Comercio Estoque - Cadastro Item')
            self.janela.geometry('600x475')
            self.janela.protocol('WM_DELETE_WINDOW', self.fechar_janela)

            fonte_padrao = ('arial', 15, 'bold')
            posicao_x = 0.02
            posicao_y = 0.07

            
            #titulos
            titulo_descricao = ctk.CTkLabel(self.janela, text='Descrição do Item:', font=fonte_padrao)
            titulo_ean = ctk.CTkLabel(self.janela, text='Código EAN:', font=fonte_padrao)
            titulo_dun = ctk.CTkLabel(self.janela, text='Código DUN:', font=fonte_padrao)
            titulo_categoria = ctk.CTkLabel(self.janela, text='Categoria:', font=fonte_padrao)
            titulo_fornecedor = ctk.CTkLabel(self.janela, text='Código Forn:', font=fonte_padrao)
            titulo_shelflife = ctk.CTkLabel(self.janela, text='Shelf-life:', font=fonte_padrao)
            titulo_ex_shelflife = ctk.CTkLabel(self.janela, text='Ex: 300', font=('Arial', 15), text_color='#b5b5b5')
            titulo_custo = ctk.CTkLabel(self.janela, text='Custo de Compra', font=fonte_padrao)
            

            #campos
            campo_descricao = ctk.CTkEntry(self.janela, placeholder_text='Insira a Descrição Resumida do item.')
            campo_ean = ctk.CTkEntry(self.janela, placeholder_text='Insira o EAN.')
            campo_dun = ctk.CTkEntry(self.janela, placeholder_text='Insira o DUN.')
            campo_categoria = ctk.CTkComboBox(self.janela)
            campo_fornecedor = ctk.CTkEntry(self.janela, placeholder_text='Nº Forn.')
            campo_shelflife_min = ctk.CTkEntry(self.janela, placeholder_text='Min')
            campo_shelflife_max = ctk.CTkEntry(self.janela, placeholder_text='Max')
            campo_custo = ctk.CTkEntry(self.janela, placeholder_text='Ex: 5.25.')
            
            #checkbox
            validade_indef = ctk.CTkCheckBox(self.janela, text='Validade Indefinida', font=fonte_padrao)

            #botoes
            botao_confirmar = ctk.CTkButton(self.janela, text='Confirmar', fg_color='#008080', font=fonte_padrao)
            botao_apagar = ctk.CTkButton(self.janela, text='Apagar', fg_color='#8b0000', font=fonte_padrao)
            

            #posicionamento
            titulo_descricao.place(relx=posicao_x, rely=posicao_y)
            campo_descricao.place(relx=posicao_x, rely=posicao_y * 2, relwidth=0.763)

            titulo_ean.place(relx=posicao_x, rely=posicao_y * 3)
            campo_ean.place(relx=posicao_x, rely=posicao_y * 4, relwidth=0.2)

            titulo_dun.place(relx=posicao_x * 13.7, rely=posicao_y * 3)
            campo_dun.place(relx=posicao_x * 13.7, rely=posicao_y * 4, relwidth=0.2)

            titulo_categoria.place(relx=posicao_x * 27.4, rely=posicao_y * 3)
            campo_categoria.place(relx=posicao_x * 27.4, rely=posicao_y * 4)

            titulo_fornecedor.place(relx=posicao_x, rely=posicao_y * 5)
            campo_fornecedor.place(relx=posicao_x, rely=posicao_y * 6, relwidth=0.1)

            titulo_shelflife.place(relx=posicao_x, rely=posicao_y * 7)
            titulo_ex_shelflife.place(relx=posicao_x * 6.85, rely = posicao_y * 7)
            campo_shelflife_min.place(relx=posicao_x, rely=posicao_y * 8, relwidth=0.1)
            campo_shelflife_max.place(relx=posicao_x * 6.85, rely=posicao_y * 8, relwidth=0.1)
            validade_indef.place(relx=posicao_x * 13, rely=posicao_y * 8.1 )

            titulo_custo.place(relx=posicao_x * 28, rely=posicao_y * 7)
            campo_custo.place(relx=posicao_x * 28, rely=posicao_y * 8)

            botao_confirmar.place(relx=posicao_x, rely=posicao_y * 13.1)
            botao_apagar.place(relx=posicao_x * 13.7, rely=posicao_y * 13.1)

            #exibi a janela ativa ocultando a janela menu
            self.abrir_janela()

    #função para abrir janelas
    def abrir_janela(self):
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