import customtkinter as a
import math

janela = a.CTk()
a.set_appearance_mode("dark")

janela.title("calculadora")
janela.geometry("265x410")
janela.resizable(width=False, height=False)

# Configuração de Cores Modificada
cor_fundo_botoes = "#ffffff"    # Fundo branco para números, ., backspace e C
cor_texto_botoes = "#000000"    # Texto preto para os botões brancos
cor_operadores = "#ef4444"      # Vermelho para o resto dos botões
cor_texto_operadores = "#ffffff"# Texto branco para os botões vermelhos

valor_texto = a.StringVar()
todos_valores = ""

def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)

def inserir_parenteses():
    global todos_valores
    if todos_valores.count('(') > todos_valores.count(')'):
        todos_valores = todos_valores + ')'
    else:
        todos_valores = todos_valores + '('
    valor_texto.set(todos_valores)

def backspace():
    global todos_valores
    todos_valores = todos_valores[:-1]
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    try:
        expressao_ajustada = todos_valores
        expressao_ajustada = expressao_ajustada.replace('^', '**')
        
        if '✓' in expressao_ajustada:
            expressao_ajustada = expressao_ajustada.replace('✓', 'math.sqrt(')
            abertos = expressao_ajustada.count('(')
            fechados = expressao_ajustada.count(')')
            if abertos > fechados:
                expressao_ajustada += ')' * (abertos - fechados)

        resultado = eval(expressao_ajustada)
        valor_texto.set(str(resultado))
        todos_valores = str(resultado)
    except Exception:
        valor_texto.set("Erro")
        todos_valores = ""

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

frame_tela = a.CTkFrame(janela, width=265, height=60, corner_radius=0)
frame_tela.grid(row=0, column=0)

app_Label = a.CTkLabel(
    frame_tela, 
    textvariable=valor_texto, 
    width=245, 
    height=50, 
    anchor="e", 
    font=('Ivy', 22, 'bold')
)
app_Label.place(x=10, y=5)

frame_botoes = a.CTkFrame(janela, width=265, height=350, corner_radius=0)
frame_botoes.grid(row=1, column=0)

# Linha 1
b_1 = a.CTkButton(frame_botoes, command=limpar_tela, text="C", width=110, height=45, fg_color=cor_fundo_botoes, text_color=cor_texto_botoes, hover_color="#e5e5e5", font=('Ivy', 13, 'bold'))
b_1.place(x=10, y=10)

b_backspace = a.CTkButton(frame_botoes, command=backspace, text="←", width=50, height=45, fg_color=cor_fundo_botoes, text_color=cor_texto_botoes, hover_color="#e5e5e5", font=('Ivy', 13, 'bold'))
b_backspace.place(x=130, y=10)

b_2 = a.CTkButton(frame_botoes, command=lambda: entrar_valores('%'), text="%", width=50, height=45, fg_color=cor_operadores, text_color=cor_texto_operadores, hover_color="#dc2626", font=('Ivy', 13, 'bold'))
b_2.place(x=190, y=10)

# Linha 2
b_4 = a.CTkButton(frame_botoes, command=lambda: entrar_valores('7'), text="7", width=50, height=45, fg_color=cor_fundo_botoes, text_color=cor_texto_botoes, hover_color="#e5e5e5", font=('Ivy', 13, 'bold'))
b_4.place(x=10, y=62)

b_5 = a.CTkButton(frame_botoes, command=lambda: entrar_valores('8'), text="8", width=50, height=45, fg_color=cor_fundo_botoes, text_color=cor_texto_botoes, hover_color="#e5e5e5", font=('Ivy', 13, 'bold'))
b_5.place(x=70, y=62)

b_6 = a.CTkButton(frame_botoes, command=lambda: entrar_valores('9'), text="9", width=50, height=45, fg_color=cor_fundo_botoes, text_color=cor_texto_botoes, hover_color="#e5e5e5", font=('Ivy', 13, 'bold'))
b_6.place(x=130, y=62)

b_3 = a.CTkButton(frame_botoes, command=lambda: entrar_valores('/'), text="/", width=50, height=45, fg_color=cor_operadores, text_color=cor_texto_operadores, hover_color="#dc2626", font=('Ivy', 13, 'bold'))
b_3.place(x=190, y=62)

# Linha 3
b_8 = a.CTkButton(frame_botoes, command=lambda: entrar_valores('4'), text="4", width=50, height=45, fg_color=cor_fundo_botoes, text_color=cor_texto_botoes, hover_color="#e5e5e5", font=('Ivy', 13, 'bold'))
b_8.place(x=10, y=114)

b_9 = a.CTkButton(frame_botoes, command=lambda: entrar_valores('5'), text="5", width=50, height=45, fg_color=cor_fundo_botoes, text_color=cor_texto_botoes, hover_color="#e5e5e5", font=('Ivy', 13, 'bold'))
b_9.place(x=70, y=114)

b_10 = a.CTkButton(frame_botoes, command=lambda: entrar_valores('6'), text="6", width=50, height=45, fg_color=cor_fundo_botoes, text_color=cor_texto_botoes, hover_color="#e5e5e5", font=('Ivy', 13, 'bold'))
b_10.place(x=130, y=114)

b_7 = a.CTkButton(frame_botoes, command=lambda: entrar_valores('*'), text="*", width=50, height=45, fg_color=cor_operadores, text_color=cor_texto_operadores, hover_color="#dc2626", font=('Ivy', 13, 'bold'))
b_7.place(x=190, y=114)

# Linha 4
b_12 = a.CTkButton(frame_botoes, command=lambda: entrar_valores('1'), text="1", width=50, height=45, fg_color=cor_fundo_botoes, text_color=cor_texto_botoes, hover_color="#e5e5e5", font=('Ivy', 13, 'bold'))
b_12.place(x=10, y=166)

b_13 = a.CTkButton(frame_botoes, command=lambda: entrar_valores('2'), text="2", width=50, height=45, fg_color=cor_fundo_botoes, text_color=cor_texto_botoes, hover_color="#e5e5e5", font=('Ivy', 13, 'bold'))
b_13.place(x=70, y=166)

b_14 = a.CTkButton(frame_botoes, command=lambda: entrar_valores('3'), text="3", width=50, height=45, fg_color=cor_fundo_botoes, text_color=cor_texto_botoes, hover_color="#e5e5e5", font=('Ivy', 13, 'bold'))
b_14.place(x=130, y=166)

b_11 = a.CTkButton(frame_botoes, command=lambda: entrar_valores('-'), text="-", width=50, height=45, fg_color=cor_operadores, text_color=cor_texto_operadores, hover_color="#dc2626", font=('Ivy', 13, 'bold'))
b_11.place(x=190, y=166)

# Linha 5
b_16 = a.CTkButton(frame_botoes, command=lambda: entrar_valores('0'), text="0", width=110, height=45, fg_color=cor_fundo_botoes, text_color=cor_texto_botoes, hover_color="#e5e5e5", font=('Ivy', 13, 'bold'))
b_16.place(x=10, y=218)

b_17 = a.CTkButton(frame_botoes, command=lambda: entrar_valores('.'), text=".", width=50, height=45, fg_color=cor_fundo_botoes, text_color=cor_texto_botoes, hover_color="#e5e5e5", font=('Ivy', 13, 'bold'))
b_17.place(x=130, y=218)

b_15 = a.CTkButton(frame_botoes, command=lambda: entrar_valores('+'), text="+", width=50, height=45, fg_color=cor_operadores, text_color=cor_texto_operadores, hover_color="#dc2626", font=('Ivy', 13, 'bold'))
b_15.place(x=190, y=218)

# Linha 6
b_18 = a.CTkButton(frame_botoes, command=inserir_parenteses, text="()", width=50, height=45, fg_color=cor_operadores, text_color=cor_texto_operadores, hover_color="#dc2626", font=('Ivy', 13, 'bold'))
b_18.place(x=10, y=270)

b_19 = a.CTkButton(frame_botoes, command=lambda: entrar_valores('✓'), text="✓", width=50, height=45, fg_color=cor_operadores, text_color=cor_texto_operadores, hover_color="#dc2626", font=('Ivy', 13, 'bold'))
b_19.place(x=70, y=270)

b_20 = a.CTkButton(frame_botoes, command=lambda: entrar_valores('^'), text="^", width=50, height=45, fg_color=cor_operadores, text_color=cor_texto_operadores, hover_color="#dc2626", font=('Ivy', 13, 'bold'))
b_20.place(x=130, y=270)

b_21 = a.CTkButton(frame_botoes, command=calcular, text="=", width=50, height=45, fg_color=cor_operadores, text_color=cor_texto_operadores, hover_color="#dc2626", font=('Ivy', 13, 'bold'))
b_21.place(x=190, y=270)

janela.mainloop()
