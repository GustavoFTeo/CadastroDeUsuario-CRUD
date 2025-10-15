import customtkinter as ctk

def abrir_tela_principal(usuario_logado):
    ctk.set_appearance_mode('dark')

    def sair_conta():
        usuario_logado.clear
        telaPrincipal.destroy()
        from tela_login import abrir_tela_login
        abrir_tela_login()

    telaPrincipal = ctk.CTk()
    telaPrincipal.title('Inicio')
    telaPrincipal.geometry('320x300')

    label_mensagem = ctk.CTkLabel(telaPrincipal, text=f"Olá {usuario_logado['nome']}, seja bem vindo!", width=310)
    label_mensagem.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

    if usuario_logado['perfil_id'] == 1:
        label_admin = ctk.CTkLabel(telaPrincipal, text=f'Você é um administrador', width=310)
        label_admin.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        botao_gerenciar = ctk.CTkButton(telaPrincipal, text='Gerenciar usuários')
        botao_gerenciar.grid(row=2, column=1, padx=10, pady=10)
        
        botao_editar = ctk.CTkButton(telaPrincipal, text='Editar conta')
        botao_editar.grid(row=3, column=1, padx=10, pady=10)
        
        botao_sair = ctk.CTkButton(telaPrincipal, text='Sair da contar', command=sair_conta)
        botao_sair.grid(row=4, column=1, padx=10, pady=10)
    
    elif usuario_logado['perfil_id'] == 2:
        
        botao_editar = ctk.CTkButton(telaPrincipal, text='Editar conta')
        botao_editar.grid(row=3, column=1, padx=10, pady=10)
        
        botao_sair = ctk.CTkButton(telaPrincipal, text='Sair da contar', command=sair_conta)
        botao_sair.grid(row=4, column=1, padx=10, pady=10)

    telaPrincipal.mainloop()