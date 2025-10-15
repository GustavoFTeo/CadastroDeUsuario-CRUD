import customtkinter as ctk
from conexao import conectar

usuario_logado = {}

def abrir_tela_login():
    ctk.set_appearance_mode('dark')

    def validar_login():
        conexao = conectar()
        banco = conexao.cursor()
        
        usuario = campo_usuario.get()
        senha = campo_senha.get()

        banco.execute('SELECT * FROM usuarios WHERE nome=%s AND senha=%s', (usuario, senha))
        resultado = banco.fetchone()

        if resultado:
            label_resultado.configure(text='Login feito com sucesso!')
            usuario_logado.clear()
            usuario_logado.update({
                'id': resultado[0],
                'perfil_id': resultado[1],
                'nome': resultado[2],
                'senha': resultado[3],
                'telefone': resultado[4],
                'email': resultado[5],
                'dataNasc': resultado[6],
                'data_cadastro': resultado[7]
            })
            botao_continuar.grid(row=3, column=1, pady=10, padx=10)
        else:
            label_resultado.configure(text='Login incorreto', text_color='red')
        conexao.commit()
        conexao.close()

    def abrir_principal():
        print(usuario_logado)
        telaLogin.destroy()
        from tela_principal import abrir_tela_principal
        abrir_tela_principal(usuario_logado)

    def abrir_cadastro():
        telaLogin.destroy()
        from tela_cadastro import abrir_tela_cadastro
        abrir_tela_cadastro()

    telaLogin = ctk.CTk()
    telaLogin.title('Login')
    telaLogin.geometry('320x300')

    # Widgets
    label_usuario = ctk.CTkLabel(telaLogin, text='Usuário:')
    label_usuario.grid(row=0, column=0, pady=10, padx=10)
    campo_usuario = ctk.CTkEntry(telaLogin, placeholder_text='Digite seu usuário')
    campo_usuario.grid(row=0, column=1, pady=10, padx=10)

    label_senha = ctk.CTkLabel(telaLogin, text='Senha:')
    label_senha.grid(row=1, column=0, pady=10, padx=10)
    campo_senha = ctk.CTkEntry(telaLogin, placeholder_text='Digite sua senha', show='*')
    campo_senha.grid(row=1, column=1, pady=10, padx=10)

    botao_login = ctk.CTkButton(telaLogin, text='Login', command=validar_login)
    botao_login.grid(row=2, column=0, pady=10, padx=10)

    botao_cadastrar = ctk.CTkButton(telaLogin, text='Não possui cadastro?', command=abrir_cadastro,fg_color='#343638', hover_color='#565b5e')
    botao_cadastrar.grid(row=2, column=1, pady=10, padx=10)

    label_resultado = ctk.CTkLabel(telaLogin, text='')
    label_resultado.grid(row=3, column=0, pady=10, padx=10)

    botao_continuar = ctk.CTkButton(telaLogin, text='Continuar', command=abrir_principal)

    telaLogin.mainloop()

abrir_tela_login()