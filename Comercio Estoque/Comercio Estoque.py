import customtkinter as ctk
import json
import os
import os.path

#Gerencia as janelas abertas para garantir o menor uso de Memoria com janelas inativas.
class GerenciadorJanelas:

    def __init__(self):
        #Verifica a existencia das pastas essenciais, e garante a criação delas caso não existam.
        if os.path.exists('Base Fornecedores') == False:
            os.mkdir('Base Fornecedores')
        if os.path.exists('Base Itens') == False:
            os.mkdir('Base Itens')
        if os.path.exists('Base Histórico') == False:
            os.mkdir('Base Histórico')
        
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

            #Varviaveis Base
            fonte_padrao = ('Arial', 15, 'bold')
            posicao_x = 0.02
            posicao_y = 0.1
            teclas_numericas = [8,36,37,38,39,40,46,48,49,50,51,52,53,54,55,56,57,96,97,98,99,100,101,102,103,104,105]

            #funções
            #Responsavel por realizar o cadastro com segurança dos dados do Fornecedor
            def Cadastrar_Fornecedor():
                #verifica se todos os campos foram preenchidos
                if campo_nome_forn.get() != '' and campo_nome_repr.get() != '' and  campo_cnpj.get() != ''and len(campo_cnpj.get()) == 19:
                    #Verifica a existencia do arquivo .json responsavel por conter os registros de fornecedores.
                    if os.path.exists('Base Fornecedores/Fornecedores.json'):
                        forn_cadastrados = {}
                        fornecedor = [campo_nome_forn.get(), campo_nome_repr.get(), campo_cnpj.get()]
                        with open('Base Fornecedores/Fornecedores.json', 'r') as arquivo:
                            forn_cadastrados = json.load(arquivo)
                            cnpj_existente = False

                            #valida a existencia de dois fornecedores com o mesmo cnpj
                            for var_consul in forn_cadastrados:
                                if fornecedor[2] in forn_cadastrados[var_consul]:
                                    cnpj_existente = True
                                    break
                            if cnpj_existente:
                                titulo_resultado.configure(text='O CNPJ já foi cadastrado', text_color='Red')
                            else:
                                if isinstance(forn_cadastrados, str):
                                    forn_cadastrados = {}

                                forn_cadastrados[len(forn_cadastrados)+1] = fornecedor
                                try:
                                    with open('Base Fornecedores/Fornecedores.json', 'w') as arquivo:
                                        json.dump(forn_cadastrados, arquivo, indent=4)
                                        titulo_resultado.configure(text=f'Fornecedor foi Cadastrado com sucesso! Nº:{len(forn_cadastrados)}.', text_color='Green') 
                                except IOError as e:
                                    titulo_resultado.configure(text=f'Erro {e}', text_color='Red') 
                                apagar()
                    else:
                        forn_cadastrados = {}
                        fornecedor = [campo_nome_forn.get(), campo_nome_repr.get(), campo_cnpj.get()]
                        forn_cadastrados[len(forn_cadastrados)+1] = fornecedor
                        try:
                            with open('Base Fornecedores/Fornecedores.json', 'w') as arquivo:
                                json.dump(forn_cadastrados, arquivo, indent=4)
                        except IOError as e:
                            titulo_resultado.configure(text=f'Erro {e}', text_color='red')
                        titulo_resultado.configure(text=f'Fornecedor foi Cadastrado com sucesso! Nº:{len(forn_cadastrados)}.', text_color='Green')
                        apagar()
                elif len(campo_cnpj.get()) < 19:
                    titulo_resultado.configure(text='Por gentileza insira o CNPJ corretamente.', text_color='Red')
                else:
                    titulo_resultado.configure(text='Todos os campos devem estar preenchidos.', text_color='Red')

            #limpa os campos preenchidos
            def apagar():
                campo_nome_forn.delete(0,ctk.END)
                campo_nome_repr.delete(0, ctk.END)
                campo_cnpj.delete(0, ctk.END)

            #converte as letras minúsculas em letras maiúsculas
            def maiuscula(ferramenta):
                texto = ferramenta.widget.get()
                texto = texto.upper()
                ferramenta.widget.delete(0, ctk.END)
                ferramenta.widget.insert(0, texto)
            
            #define o padrão e limita a entrada de caracteres para apenas numericos.
            def modelo_cnpj(ferramenta):
                texto = str(ferramenta.widget.get())
                if ferramenta.keycode in teclas_numericas:
                    if len(texto) > 3 and texto.count('.') < 1:
                        texto = texto[0:3] + '.' + texto[3:19]
                        ferramenta.widget.delete(0, ctk.END)
                        ferramenta.widget.insert(0, texto)
                    
                    if len(texto) > 7 and texto.count('.') < 2:
                        texto = texto[0:7] + '.' + texto[7:19]
                        ferramenta.widget.delete(0, ctk.END)
                        ferramenta.widget.insert(0, texto)
                    
                    if len(texto) > 11 and texto.count('/') < 1:
                        texto = texto[0:11] + '/' + texto[11:19]
                        ferramenta.widget.delete(0, ctk.END)
                        ferramenta.widget.insert(0, texto)
                    
                    if len(texto) > 16 and texto.count('-') < 1:
                        texto = texto[0:16] + '-' + texto[16:19]
                        ferramenta.widget.delete(0, ctk.END)
                        ferramenta.widget.insert(0, texto)
                    
                    if len(texto) > 19:
                        texto = texto[0:19]
                        ferramenta.widget.delete(0, ctk.END)
                        ferramenta.widget.insert(0, texto)
                else:
                    texto = texto[0:texto.find(ferramenta.char)] + texto[texto.find(ferramenta.char)+1:20]
                    ferramenta.widget.delete(0, ctk.END)
                    ferramenta.widget.insert(0, texto)
    
            #titulos
            titulo_nome_forn = ctk.CTkLabel(self.janela, text='Nome do Fornecedor:', font=fonte_padrao)
            titulo_nome_repr = ctk.CTkLabel(self.janela, text='Nome do Representante de Vendas:', font=fonte_padrao)
            titulo_cnpj = ctk.CTkLabel(self.janela, text='CNPJ:', font=fonte_padrao)
            titulo_resultado = ctk.CTkLabel(self.janela, text='', font=fonte_padrao)
            #campos
            campo_nome_forn = ctk.CTkEntry(self.janela, placeholder_text='INSIRA O NOME DO FORNECEDOR.')
            campo_nome_repr = ctk.CTkEntry(self.janela, placeholder_text='INSIRA O NOME DO REPRESENTANTE.')
            campo_cnpj = ctk.CTkEntry(self.janela, placeholder_text='000.000.000/0000-00')
            #botoes
            botao_confirmar = ctk.CTkButton(self.janela, text='Confirmar', fg_color='#008080', font=fonte_padrao, command=Cadastrar_Fornecedor)
            botao_apagar = ctk.CTkButton(self.janela, text='Apagar', fg_color='#8b0000', font=fonte_padrao, command=apagar)

            #posicionamento
            titulo_nome_forn.place(relx=posicao_x, rely=posicao_y)
            campo_nome_forn.place(relx=posicao_x, rely=posicao_y * 2, relwidth=0.6)

            titulo_nome_repr.place(relx=posicao_x, rely=posicao_y * 3)
            campo_nome_repr.place(relx=posicao_x, rely=posicao_y * 4, relwidth=0.6)

            titulo_cnpj.place(relx=posicao_x, rely=posicao_y * 5)
            campo_cnpj.place(relx=posicao_x, rely=posicao_y * 6, relwidth=0.23)

            titulo_resultado.place(relx=posicao_x, rely=posicao_y * 7.25)

            botao_confirmar.place(relx=posicao_x, rely=posicao_y * 8.7)
            botao_apagar.place(relx=posicao_x * 13.7, rely=posicao_y * 8.7)

            #eventos
            campo_nome_forn.bind('<KeyRelease>', maiuscula)
            campo_nome_repr.bind('<KeyRelease>', maiuscula)
            campo_cnpj.bind('<KeyRelease>', modelo_cnpj)

            #exibi a janela ativa ocultando a janela menu
            self.abrir_janela()

    def cadastro_categoria(self):
        if self.janela is None:
            self.janela = ctk.CTk()
            self.janela.title('Comercio Estoque - Cadastro Categoria')
            self.janela.geometry('600x200')
            #chama a função fechar_janela quando o evento de fechar a jenala ativa for ativado.
            self.janela.protocol('WM_DELETE_WINDOW', self.fechar_janela)

            #Variaveis Base
            fonte_padrao = ('arial', 15, 'bold')
            posicao_x = 0.02
            posicao_y = 0.15
            
            #funções
            def maiuscula(ferramenta):
                texto = ferramenta.widget.get()
                texto = texto.upper()
                ferramenta.widget.delete(0, ctk.END)
                ferramenta.widget.insert(0, texto)

            def salvar_categoria():
                if campo_categoria.get() != '':
                    campo_categoria.get()
                    if os.path.exists(f'Base Categoria/Categorias.json'):
                        try:
                            with open('Base Categoria/Categorias.json', 'r') as arquivo:
                                cate_cadastradas = json.load(arquivo)
                                categoria_existente = False
                                for var_consul in cate_cadastradas:
                                    if campo_categoria.get() in cate_cadastradas[var_consul]:
                                        categoria_existente = True
                                        break
                            if categoria_existente:
                                titulo_resultado.configure(text='Não é possivel criar uma categoria já existente.', text_color='red')
                            else:
                                if isinstance(campo_categoria.get(), str):
                                    cate_cadastradas[len(cate_cadastradas) + 1] = [campo_categoria.get()]
                                    try:
                                        with open('Base Categoria/Categorias.json','w') as arquivo:
                                            json.dump(cate_cadastradas, arquivo, indent=4)
                                            titulo_resultado.configure(text=f'Categoria foi Cadastrada com sucessso! Nº:{len(cate_cadastradas)}', text_color='Green')
                                    except IOError as e:
                                        titulo_resultado.configure(text=f'Erro no salvamento da categoria. Erro: {e}', text_color='Red')
                                    apagar()
                        except IOError as e:
                            titulo_resultado.configure(text=f'Erro na leitura do arquivo existente. Error: {e}', text_color='Red')
                    else:
                        try:
                            with open(f'Base Categoria/Categorias.json', 'w') as arquivo:
                                cate_cadastradas = {}
                                cate_cadastradas[len(cate_cadastradas)+1] = [campo_categoria.get()]
                                json.dump(cate_cadastradas, arquivo, indent=4)
                                titulo_resultado.configure(text='Categoria criada com sucesso', text_color='green')
                                apagar()
                        except IOError as e:
                            titulo_resultado.configure(text=f'Erro {e}', text_color='red')
                else:
                    titulo_resultado.configure(text='Por Favor, informe o nome da categoria.', text_color='red')

            def apagar():
                campo_categoria.delete(0,ctk.END)

            #titulos
            titulo_categoria = ctk.CTkLabel(self.janela, text='Categoria:', font=fonte_padrao)
            titulo_resultado = ctk.CTkLabel(self.janela, text='', font=fonte_padrao)
            #campos
            campo_categoria = ctk.CTkEntry(self.janela, placeholder_text='INSIRA O NOME DA CATEGORIA')
            #botões
            botao_confirmar = ctk.CTkButton(self.janela, text='Confirmar', fg_color='#008080', font=fonte_padrao, command=salvar_categoria)
            botao_apagar = ctk.CTkButton(self.janela, text='Apagar', fg_color='#8b0000', font=fonte_padrao, command=apagar)

            #posicionamento
            titulo_categoria.place(relx=posicao_x, rely=posicao_y)

            campo_categoria.place(relx=posicao_x, rely=posicao_y * 2, relwidth=0.6)
            titulo_resultado.place(relx=posicao_x, rely=posicao_y * 3.25)

            botao_confirmar.place(relx=posicao_x, rely=posicao_y * 5.4)
            botao_apagar.place(relx=posicao_x * 13.7, rely=posicao_y * 5.4)

            #eventos
            campo_categoria.bind('<KeyRelease>', maiuscula)

            #exibi a janela ativa ocultando a janela menu
            self.abrir_janela()

    def cadastro_itens(self):
        if self.janela is None:
            self.janela = ctk.CTk()
            self.janela.title('Comercio Estoque - Cadastro Item')
            self.janela.geometry('600x475')
            self.janela.protocol('WM_DELETE_WINDOW', self.fechar_janela)

            #Variaveis Base
            fonte_padrao = ('Arial', 15, 'bold')
            posicao_x = 0.02
            posicao_y = 0.07
            teclas_numericas = [8,36,37,38,39,40,46,48,49,50,51,52,53,54,55,56,57,96,97,98,99,100,101,102,103,104,105]

            def maiuscula(ferramenta):
                texto = ferramenta.widget.get()
                texto = texto.upper()
                ferramenta.widget.delete(0, ctk.END)
                ferramenta.widget.insert(0, texto)

            def numerico(ferramenta):
                if not ferramenta.keycode in teclas_numericas:
                    texto = str(ferramenta.widget.get())
                    texto = texto[0:texto.find(ferramenta.char)]+ texto[texto.find(ferramenta.char)+1:]
                    ferramenta.widget.delete(0, ctk.END)
                    ferramenta.widget.insert(0, texto)

            def apagar():
                campo_descricao.delete(0, ctk.END)
                campo_ean.delete(0,ctk.END)
                campo_dun.delete(0,ctk.END)
                campo_fornecedor.delete(0,ctk.END)
                campo_shelflife_max.delete(0,ctk.END)
                campo_shelflife_min.delete(0,ctk.END)
                campo_custo.delete(0,ctk.END)
                validade_indef.deselect()
                
            def lista_categoria():
                retorno = ''
                if os.path.exists(f'Base Categoria/Categorias.json'):    
                    try:
                        with open(f'Base Categoria/Categorias.json', 'r') as arquivo:
                            lista_nomes = ['']
                            categorias = json.load(arquivo)
                            for nome in categorias:
                                lista_nomes.append(categorias[nome][0])
                    except FileNotFoundError:
                        retorno = 'A pasta "Base Categoria" não foi encontrada.'
                    except OSError as e:
                        retorno = f'Erro ao acessar a pasta Base Categoria: {e}'
                else:
                    retorno = 'Não existe categorias cadastradas.'
                return lista_nomes, retorno
            
            def lista_fornecedores():
                lista_nome_forn = ['']
                retorno = ''
                if os.path.exists(f'Base Fornecedores/Fornecedores.json'):
                    try:
                        with open(f'Base Fornecedores/Fornecedores.json', 'r') as arquivo:
                            fornecedores = json.load(arquivo)
                            for nome in fornecedores:
                                lista_nome_forn.append(fornecedores[nome][0])
                    except FileNotFoundError:
                        retorno = 'A pasta "Base Fornecedores" não foi encontrada'
                    except OSError as e:
                        retorno = f'Erro na tentativa de acessar a pasta Base Fornecedores: {e}'
                else:
                    retorno='Não existe fornecedores cadastrados.'
                return lista_nome_forn, retorno

            #titulos
            titulo_descricao = ctk.CTkLabel(self.janela, text='Descrição do Item:', font=fonte_padrao)
            titulo_ean = ctk.CTkLabel(self.janela, text='Código EAN:', font=fonte_padrao)
            titulo_dun = ctk.CTkLabel(self.janela, text='Código DUN:', font=fonte_padrao)
            titulo_categoria = ctk.CTkLabel(self.janela, text='Categoria:', font=fonte_padrao)
            titulo_fornecedor = ctk.CTkLabel(self.janela, text='Código Forn:', font=fonte_padrao)
            titulo_shelflife = ctk.CTkLabel(self.janela, text='Shelf-life:', font=fonte_padrao)
            titulo_ex_shelflife = ctk.CTkLabel(self.janela, text='Ex: 300', font=('Arial', 15), text_color='#b5b5b5')
            titulo_custo = ctk.CTkLabel(self.janela, text='Custo de Compra', font=fonte_padrao)
            titulo_resultado = ctk.CTkLabel(self.janela, text=lista_categoria()[1] + '\n' + lista_fornecedores()[1], font=fonte_padrao, text_color='red')
            #campos
            campo_descricao = ctk.CTkEntry(self.janela, placeholder_text='Insira a Descrição Resumida do item.')
            campo_ean = ctk.CTkEntry(self.janela, placeholder_text='Insira o EAN.')
            campo_dun = ctk.CTkEntry(self.janela, placeholder_text='Insira o DUN.')
            campo_fornecedor = ctk.CTkEntry(self.janela, placeholder_text='Nº Forn.')
            campo_shelflife_min = ctk.CTkEntry(self.janela, placeholder_text='Min')
            campo_shelflife_max = ctk.CTkEntry(self.janela, placeholder_text='Max')
            campo_custo = ctk.CTkEntry(self.janela, placeholder_text='Ex: 5.25.')
            #Lista
            campo_categoria = ctk.CTkComboBox(self.janela, values=lista_categoria()[0])
            campo_n_fornecedores = ctk.CTkComboBox(self.janela, values=lista_fornecedores()[0])
            #checkbox
            validade_indef = ctk.CTkCheckBox(self.janela, text='Validade Indefinida', font=fonte_padrao)
            #botoes
            botao_confirmar = ctk.CTkButton(self.janela, text='Confirmar', fg_color='#008080', font=fonte_padrao)
            botao_apagar = ctk.CTkButton(self.janela, text='Apagar', fg_color='#8b0000', font=fonte_padrao, command=apagar)
            
            #posicionamento
            titulo_descricao.place(relx=posicao_x, rely=posicao_y)
            campo_descricao.place(relx=posicao_x, rely=posicao_y * 2, relwidth=0.775)

            titulo_ean.place(relx=posicao_x, rely=posicao_y * 3)
            campo_ean.place(relx=posicao_x, rely=posicao_y * 4, relwidth=0.2)

            titulo_dun.place(relx=posicao_x * 13.7, rely=posicao_y * 3)
            campo_dun.place(relx=posicao_x * 13.7, rely=posicao_y * 4, relwidth=0.2)

            titulo_categoria.place(relx=posicao_x * 27.4, rely=posicao_y * 3)
            campo_categoria.place(relx=posicao_x * 27.4, rely=posicao_y * 4, relwidth=0.245)

            titulo_fornecedor.place(relx=posicao_x, rely=posicao_y * 5)
            campo_fornecedor.place(relx=posicao_x, rely=posicao_y * 6, relwidth=0.1)
            campo_n_fornecedores.place(relx=posicao_x * 9, rely=posicao_y * 6, relwidth = 0.615)

            titulo_shelflife.place(relx=posicao_x, rely=posicao_y * 7)
            titulo_ex_shelflife.place(relx=posicao_x * 6.85, rely = posicao_y * 7)
            campo_shelflife_min.place(relx=posicao_x, rely=posicao_y * 8, relwidth=0.1)
            campo_shelflife_max.place(relx=posicao_x * 6.85, rely=posicao_y * 8, relwidth=0.1)
            validade_indef.place(relx=posicao_x * 13, rely=posicao_y * 8.1 )

            titulo_custo.place(relx=posicao_x * 28, rely=posicao_y * 7)
            campo_custo.place(relx=posicao_x * 28, rely=posicao_y * 8)
            titulo_resultado.place(relx=posicao_x, rely=posicao_y * 9)

            botao_confirmar.place(relx=posicao_x, rely=posicao_y * 13.1)
            botao_apagar.place(relx=posicao_x * 13.7, rely=posicao_y * 13.1)

            #eventos
            campo_descricao.bind('<KeyRelease>', maiuscula)
            campo_dun.bind('<KeyRelease>', numerico)
            campo_ean.bind('<KeyRelease>', numerico)
            campo_fornecedor.bind('<KeyRelease>', numerico)

            #exibi a janela ativa ocultando a janela menu
            self.abrir_janela()

    def entrada_nf(self):
        if self.janela is None:
            #define as configurações iniciais da janela
            self.janela = ctk.CTk()
            self.janela.title('Comercio Estoque - Entrada de Notas')
            self.janela.geometry('600x600')
            self.janela.protocol('WM_DELETE_WINDOW', self.fechar_janela)

            fonte_padrao = ('Arial', 15, 'bold')
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

            fonte_padrao = ('Arial', 15, 'bold')
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

            fonte_padrao = ('Arial', 15, 'bold')
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