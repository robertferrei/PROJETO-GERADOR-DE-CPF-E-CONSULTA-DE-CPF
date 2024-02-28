from PySimpleGUI import PySimpleGUI as sg
from tkinter import messagebox
import random

# Layout da tela de login
sg.theme('Reddit')  # Tema

layout = [
    [sg.Text("Usuário"), sg.Input(key="usuario", size=(20, 1))],
    [sg.Text("Senha"), sg.Input(key="senha", password_char="*", size=(20, 1))],
    [sg.Checkbox("Salvar login?")],
    [sg.Button("Entrar")]
]

# Layout da tela de consulta de CPF
layoutCpf = [
    [sg.Text("CPF"), sg.Input(key="validarccpf", size=(20, 1))],
    [sg.Button("Consultar")]
]

layoutGerador = [
    [sg.Button("Gerar")]
]

# Janela de login
janela = sg.Window("Tela de Login", layout)


# Ler eventos da janela
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == "Entrar":
        # Verificar se o usuário e a senha estão corretos
        if valores["usuario"] == "robert" and valores["senha"] == "12345":
            # JANELA PARA GERAR CPF ALEATORIO
            janela_gerador_cpf = sg.Window("Gere um cpf", layoutGerador)
            while True:
                eventoGerador, valorGerador = janela_gerador_cpf.read()
                if eventoGerador == sg.WINDOW_CLOSED:
                    break
                if eventoGerador == "Gerar":
                    # FOR NOVE DIGITOS
                    nove_digitos = ''
                    for i in range(9):
                        nove_digitos += str(random.randint(0, 9))

# SOMA DE DIGITOS PARA VALIDAÇÃO ALEATORIA
                    primeiroDigitoG = 0
                    somaGer = 0

                    for i in range(9):
                        somaGer += int(nove_digitos[i]) * (10 - i)

                    somaSegundoG = somaGer
                    restoG = somaGer % 11

                    # passando os valores de vereficação
                    primeiroDigitoG = 0 if restoG > 9 else 11 - restoG  # <- primeiro digito

                    # soma do segundo digito
                    somaSegundoG += primeiroDigitoG * 2

                    # resto do segundo digito
                    restoSegundoG = somaSegundoG % 11

                    # segundo digito
                    segundo_digitoG = 0 if restoSegundoG <= 9 else 11 - restoSegundoG

                    cpfGeradoG = f"{nove_digitos}{
                        primeiroDigitoG}{segundo_digitoG}"
                    print(cpfGeradoG)

                    sg.popup(f"CPF Gerado:{cpfGeradoG}")

# JANELA PARA A VALIDAÇÃO DO CPF
# Abrir a janela de consulta de CPF

            janelaCpf = sg.Window("Consulta de CPF", layoutCpf)
            while True:
                eventosCpf, valoresCpf = janelaCpf.read()
                if eventosCpf == sg.WINDOW_CLOSED:
                    break
                if eventosCpf == "Consultar":
                    # Pegar o valor do CPF inserido
                    cpf = valoresCpf["validarccpf"]
                    noveDigitos = cpf[:9]
                    # Calcular o primeiro dígito verificador
                    soma = 0
                    for i in range(9):
                        soma += int(cpf[i]) * (10 - i)
                    resto = soma % 11
                    primeiroDigito = 0 if resto > 9 else 11 - resto  # <- primeiro digito

                    # Calcular o segundo dígito verificador
                    somaSegundo = soma + primeiroDigito * 2
                    restoSegundo = somaSegundo % 11
                    segundo_digito = 0 if restoSegundo <= 9 else 11 - restoSegundo

                    cpfGerado = f"{noveDigitos}{
                        primeiroDigito}{segundo_digito}"

                    print(cpfGerado)
                    print(f'{primeiroDigito} {segundo_digito}')
                    if cpf == cpfGerado:
                        sg.popup("CPF VALIDO")
                    else:
                        sg.popup("CPF INVALIDO")

            janelaCpf.close()  # Fechar a janela de consulta de CPF

janela.close()  # Fechar a janela de login
