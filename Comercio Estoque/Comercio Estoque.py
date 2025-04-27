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
        ent_item_botao = ctk.CTkButton(self.menu, text='Entrada de NF', command=self.entrada_nf)
        con_estq_botao = ctk.CTkButton(self.menu, text='Consulta de Estoque', command=self.consulta_estoque)
        venda_botao = ctk.CTkButton(self.menu, text='Venda de Itens', command=self.vendas)

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

    def entrada_nf(self):
        if self.janela is None:
            #define as configurações iniciais da janela
            self.janela = ctk.CTk()
            self.janela.title('Comercio Estoque - Entrada de Notas')
            self.janela.geometry('600x600')
            self.janela.protocol('WM_DELETE_WINDOW', self.fechar_janela)

            fonte_padrao = ('arial', 15, 'bold')
            posicao_x = 0.02
            posicao_y = 0.04

            #titulos
            titulo_nf = ctk.CTkLabel(self.janela, text='Numero da Nota:', font=fonte_padrao)
            titulo_n_forn = ctk.CTkLabel(self.janela, text='Nº Forn:', font=fonte_padrao)
            titulo_nome_forn = ctk.CTkLabel(self.janela, text='Fornecedor:', font=fonte_padrao)
            titulo_cnpj = ctk.CTkLabel(self.janela, text='CNPJ do Emitente:', font=fonte_padrao)
            titulo_item = ctk.CTkLabel(self.janela, text='Código do item:', font=fonte_padrao)
            titulo_desc_item = ctk.CTkLabel(self.janela, text='Descrição:', font=fonte_padrao)
            titulo_ean = ctk.CTkLabel(self.janela, text='Código EAN:', font=fonte_padrao)
            titulo_dun = ctk.CTkLabel(self.janela, text='Código Dun:', font=fonte_padrao)
            titulo_qtd = ctk.CTkLabel(self.janela, text='Qtd:', font=fonte_padrao)
            titulo_lista = ctk.CTkLabel(self.janela, text='Itens Adicionados:', font=fonte_padrao)
            #campos
            campo_nf = ctk.CTkEntry(self.janela, placeholder_text='Numero NF.')
            campo_n_fornecedor = ctk.CTkEntry(self.janela, placeholder_text='N. Forn.')
            campo_nome_forne = ctk.CTkEntry(self.janela, placeholder_text='Nome do Fornecedor.')
            campo_cnpj = ctk.CTkEntry(self.janela, placeholder_text='000.000.000/0000-00')
            campo_item = ctk.CTkEntry(self.janela, placeholder_text='Cód. Item.')
            campo_descricao = ctk.CTkEntry(self.janela, placeholder_text='Descrição do Item.')
            campo_ean = ctk.CTkEntry(self.janela, placeholder_text='Insira o EAN.')
            campo_dun = ctk.CTkEntry(self.janela, placeholder_text='Insira o DUN.')
            campo_qtd = ctk.CTkEntry(self.janela)
            campo_lista = ctk.CTkFrame(self.janela, width=575, height=317, fg_color='white')
            #botôes
            botao_confirmar = ctk.CTkButton(self.janela, text='Confirmar', fg_color='#008080', font=fonte_padrao)
            botao_apagar = ctk.CTkButton(self.janela, text='Apagar', fg_color='#8b0000', font=fonte_padrao)

            titulo_nf.place(relx=posicao_x, rely=posicao_y)
            campo_nf.place(relx=posicao_x, rely=posicao_y * 2)
            titulo_cnpj.place(relx=posicao_x * 13.7, rely=posicao_y)
            campo_cnpj.place(relx=posicao_x * 13.7, rely=posicao_y * 2)
            titulo_n_forn.place(relx=posicao_x * 27.4, rely=posicao_y)
            campo_n_fornecedor.place(relx=posicao_x * 27.4, rely=posicao_y * 2, relwidth=0.1)
            titulo_nome_forn.place(relx=posicao_x, rely=posicao_y * 3)
            campo_nome_forne.place(relx=posicao_x, rely=posicao_y * 4, relwidth=0.96)
            titulo_item.place(relx=posicao_x, rely=posicao_y * 5)
            campo_item.place(relx=posicao_x, rely=posicao_y * 6)
            titulo_ean.place(relx=posicao_x * 13.7, rely=posicao_y * 5)
            campo_ean.place(relx=posicao_x * 13.7, rely=posicao_y * 6, relwidth=0.18)
            titulo_dun.place(relx=posicao_x * 23.7, rely=posicao_y * 5)
            campo_dun.place(relx=posicao_x * 23.7, rely=posicao_y * 6, relwidth=0.19)
            titulo_qtd.place(relx=posicao_x * 34.2, rely=posicao_y * 5)
            campo_qtd.place(relx=posicao_x * 34.2, rely=posicao_y * 6, relwidth=0.095)
            titulo_desc_item.place(relx=posicao_x, rely=posicao_y * 7)
            campo_descricao.place(relx=posicao_x, rely=posicao_y * 8, relwidth=0.96)
            titulo_lista.place(relx=posicao_x, rely=posicao_y * 9)
            campo_lista.place(relx=posicao_x, rely=posicao_y * 10)
            botao_confirmar.place(relx=posicao_x, rely=posicao_y * 23.4)
            botao_apagar.place(relx=posicao_x * 13.7, rely=posicao_y * 23.4)

            self.abrir_janela()

    def consulta_estoque(self):
        if self.janela is None:
            self.janela = ctk.CTk()
            self.janela.title('Comercio Estoque - Consulta de Estoque')
            self.janela.geometry('600x600')
            self.janela.protocol('WM_DELETE_WINDOW', self.fechar_janela)

            fonte_padrao = ('arial', 15, 'bold')
            posicao_x = 0.02
            posicao_y = 0.04

            #titulos
            titulo_cod_item = ctk.CTkLabel(self.janela, text='Código:', font=fonte_padrao)
            titulo_descricao = ctk.CTkLabel(self.janela, text='Descrição:', font=fonte_padrao)
            titulo_categoria = ctk.CTkLabel(self.janela, text='Categória:',font=fonte_padrao)
            titulo_fornecedor = ctk.CTkLabel(self.janela, text='Fornecedor:', font=fonte_padrao)
            titulo_consulta = ctk.CTkLabel(self.janela, text='Consulta:', font=fonte_padrao)
            #campos
            campo_cod_item = ctk.CTkEntry(self.janela, placeholder_text='Cód.')
            campo_descricao = ctk.CTkEntry(self.janela, placeholder_text='Insira a descrição do item.')
            campo_categoria = ctk.CTkComboBox(self.janela)
            campo_fornecedor = ctk.CTkComboBox(self.janela)
            campo_consulta = ctk.CTkFrame(self.janela, width=575, height=412, fg_color='white')
            #botao
            botao_confirmar = ctk.CTkButton(self.janela, text='Confirmar', fg_color='#008080', font=fonte_padrao)
            botao_apagar = ctk.CTkButton(self.janela, text='Apagar', fg_color='#8b0000', font=fonte_padrao)
            botao_pesquisar = ctk.CTkButton(self.janela, text='Pesquisar', fg_color='#008080', font=fonte_padrao)

            titulo_cod_item.place(relx=posicao_x, rely=posicao_y)
            campo_cod_item.place(relx=posicao_x, rely=posicao_y * 2)
            titulo_descricao.place(relx=posicao_x * 13.7, rely=posicao_y)
            campo_descricao.place(relx=posicao_x * 13.7, rely=posicao_y * 2, relwidth=0.707)
            titulo_fornecedor.place(relx=posicao_x, rely=posicao_y * 3)
            campo_fornecedor.place(relx=posicao_x, rely=posicao_y * 4)
            titulo_categoria.place(relx=posicao_x * 17, rely=posicao_y * 3)
            campo_categoria.place(relx=posicao_x * 17, rely=posicao_y * 4)
            botao_pesquisar.place(relx=posicao_x * 33, rely=posicao_y * 4)
            titulo_consulta.place(relx=posicao_x, rely=posicao_y * 5)
            campo_consulta.place(relx=posicao_x, rely=posicao_y * 6)
            botao_confirmar.place(relx=posicao_x, rely=posicao_y * 23.4)
            botao_apagar.place(relx=posicao_x * 13.7, rely=posicao_y * 23.4)

            self.abrir_janela()

    def vendas(self):
        if self.janela is None:
            self.janela = ctk.CTk()
            self.janela.title('Comercio Estoque - Vendas')
            self.janela.geometry('600x600')
            self.janela.protocol('WM_DELETE_WINDOW', self.fechar_janela)

            fonte_padrao = ('arial', 15, 'bold')
            posicao_x = 0.02
            posicao_y = 0.04

            #titulos
            titulo_cod = ctk.CTkLabel(self.janela, text='Código:', font=fonte_padrao)
            titulo_qtd = ctk.CTkLabel(self.janela, text='Qtd:', font=fonte_padrao)
            titulo_iten_vend = ctk.CTkLabel(self.janela, text='Itens Vendidos', font=fonte_padrao)
            titulo_total = ctk.CTkLabel(self.janela, text='Total:', font=fonte_padrao)
            resultado_total = ctk.CTkLabel(self.janela, text='R$ 00,00', font=('Arial', 15), text_color='#b5b5b5')
            titulo_pago = ctk.CTkLabel(self.janela, text='Total Pago:', font=fonte_padrao)
            resultado_pago = ctk.CTkLabel(self.janela, text='R$ 00.00', font=('Arial',15), text_color='#b5b5b5')
            #campo
            campo_cod = ctk.CTkEntry(self.janela, placeholder_text='Cod EAN/DUN/Interno.')
            campo_qtd = ctk.CTkEntry(self.janela, placeholder_text='Unidades.')
            campo_itens_vend = ctk.CTkFrame(self.janela, width=+575, height=412, fg_color='white')
            #botao
            botao_proximo = ctk.CTkButton(self.janela, text='Adcionar', fg_color='#008080', font=fonte_padrao)
            botao_confirmar = ctk.CTkButton(self.janela, text='Confirmar', fg_color='#008080', font=fonte_padrao)
            botao_apagar = ctk.CTkButton(self.janela, text='Apagar', fg_color='#8b0000', font=fonte_padrao)

            titulo_cod.place(relx=posicao_x, rely=posicao_y)
            campo_cod.place(relx=posicao_x, rely=posicao_y * 2,  relwidth=0.24)
            titulo_qtd.place(relx=posicao_x * 14.5, rely=posicao_y)
            campo_qtd.place(relx=posicao_x * 14.5, rely=posicao_y * 2)
            botao_proximo.place(relx=posicao_x * 32, rely=posicao_y * 2)
            titulo_iten_vend.place(relx=posicao_x, rely=posicao_y * 3)
            campo_itens_vend.place(relx=posicao_x, rely=posicao_y * 4)
            titulo_total.place(relx=posicao_x, rely=posicao_y * 21.5)
            resultado_total.place(relx=posicao_x * 5.5, rely=posicao_y * 21.5)
            titulo_pago.place(relx=posicao_x * 15.4,rely=posicao_y * 21.5)
            resultado_pago.place(relx=posicao_x * 23.25, rely=posicao_y * 21.5)
            botao_confirmar.place(relx=posicao_x, rely=posicao_y * 23.4)
            botao_apagar.place(relx=posicao_x * 13.7, rely=posicao_y * 23.4)

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