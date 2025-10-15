import customtkinter as ctk
from conexao import conectar

def abrir_tela_cadastro():
    ctk.set_appearance_mode('dark')

    def abrir_login():
        telaCadastro.destroy()
        from tela_login import abrir_tela_login
        abrir_tela_login()
    
    def abrir_principal():
        telaCadastro.destroy()
        from tela_principal import abrir_tela_principal
        abrir_tela_principal()

    def cadastrarUsuario():
        conexao = conectar()
        banco = conexao.cursor()

        perfil = combobox_perfil.get()
        perfil_id = 2
        if perfil=='Admin':
            perfil_id = 1
        else:
            perfil_id = 2
        nome = campo_nome.get()
        senha = campo_senha.get()
        telefone = campo_telefone.get()
        email = campo_email.get()
        dataNasc = campo_dataNasc.get()

        if not nome or not senha or not telefone or not email or not dataNasc or perfil == '--selecione--':
            label_resultado.configure(text='Falha no cadastro: preencha todos os campos', text_color='red')
            return
        
        banco.execute("""
        SELECT * FROM usuarios 
        WHERE nome = %s OR email = %s OR telefone = %s""", (nome, email, telefone))
        resultado = banco.fetchone()
        if resultado:
            label_resultado.configure(text='Usuário já cadastrado!', text_color='red')
            conexao.close()
            return

        sql = "INSERT INTO usuarios (perfil_id, nome, senha, telefone, email, dataNasc) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (perfil_id, nome, senha, telefone, email, dataNasc)
        banco.execute(sql, valores)
        conexao.commit()
        conexao.close()
        botao_continuar.grid(row=8, column=0, columnspan=3, pady=10, padx=10)


    telaCadastro = ctk.CTk()
    telaCadastro.title('Cadastro de Usuário')
    telaCadastro.geometry('460x500')

    label_perfil = ctk.CTkLabel(telaCadastro,text='Perfil da conta:')
    label_perfil.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    combobox_perfil = ctk.CTkComboBox(telaCadastro, values=['Admin','Usuário'], width=280)
    combobox_perfil.set('--selecione--')
    combobox_perfil.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

    label_nome = ctk.CTkLabel(telaCadastro,text='Usuário:')
    label_nome.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    campo_nome = ctk.CTkEntry(telaCadastro,placeholder_text='Digite seu usuário', width=280)
    campo_nome.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

    label_email = ctk.CTkLabel(telaCadastro,text='Email:')
    label_email.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    campo_email = ctk.CTkEntry(telaCadastro,placeholder_text='Digite seu email', width=280)
    campo_email.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

    label_telefone = ctk.CTkLabel(telaCadastro,text='Telefone:')
    label_telefone.grid(row=3, column=0, padx=10, pady=10, sticky="e")

    campo_telefone = ctk.CTkEntry(telaCadastro,placeholder_text='Digite seu telefone (99 99999-9999)', width=280)
    campo_telefone.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

    label_dataNasc = ctk.CTkLabel(telaCadastro,text='Data de Nascimento:')
    label_dataNasc.grid(row=4, column=0, padx=10, pady=10, sticky="e")

    campo_dataNasc = ctk.CTkEntry(telaCadastro,placeholder_text='Digite sua data de nascimento (AAAA-MM-DD)', width=280)
    campo_dataNasc.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

    label_senha = ctk.CTkLabel(telaCadastro,text='Senha:')
    label_senha.grid(row=5, column=0, padx=10, pady=10, sticky="e")

    campo_senha = ctk.CTkEntry(telaCadastro,placeholder_text='Digite sua senha',show='*', width=280)
    campo_senha.grid(row=5, column=1, columnspan=2, padx=10, pady=10)

    botao_login = ctk.CTkButton(telaCadastro,text='Já possui cadastro?',command=abrir_login, fg_color='#343638', hover_color='#565b5e')
    botao_login.grid(row=6, column=0, columnspan=2, pady=10, padx=10, sticky='e')
    botao_cadastrar = ctk.CTkButton(telaCadastro,text='Cadastrar',command=cadastrarUsuario)
    botao_cadastrar.grid(row=6, column=2, padx=10, pady=10)

    label_resultado = ctk.CTkLabel(telaCadastro,text='')
    label_resultado.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    botao_continuar = ctk.CTkButton(telaCadastro, text='Continuar', command=abrir_principal)

    telaCadastro.mainloop()