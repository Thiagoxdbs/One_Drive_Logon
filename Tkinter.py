import tkinter as tk #USADO PARA CRIAR A INTERFACE DO APP
from tkinter import messagebox #CAIXA DE ALERTA DO APP
from pynput.keyboard import Key, Controller as KeyboardController#CONTROLE DO MOUSE/TECLADO
from pynput.mouse import Button, Controller as MouseController #CONTROLE DO MOUSE/TECLADO
import time #AUXILIAR PARA DAR TEMPO DE CARREGAR O CONTEUDO DO ONEDRIVE E PARA O LOOP
import pyautogui # BIBLIOTECA PARA TIRAR SCREENSHOT
import cv2 #ABRIR A IMAGEM
import pytesseract #TRANSFORMAR IMAGEM EM TEXTO


# Realize a automação do teclado e mouse aqui
keyboard = KeyboardController()
mouse = MouseController()

def login():
	username = entry_username.get()
	#password = entry_password.get()

	if username:
		# Aqui você pode adicionar o código para autenticar o usuário no OneDrive
		# messagebox.showinfo("Login", f"Username: {username}\nPassword: {password}")
		window.quit()
				


		# Simule as ações do teclado e mouse
		#TECLA WINDOWS
		keyboard.press(Key.cmd)
		keyboard.release(Key.cmd)
		time.sleep(1)

		#DIGITANDO ONEDRIVE NO PROCURAR DO WINDOWS
		for char in "onedrive":
			keyboard.press(char)
			keyboard.release(char)
			time.sleep(0.12)
			
		#TECLA ENTER PARA ABRIR PASTA
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)

		#TEMPO PARA PRINTAR PASTA DO ONEDRIVE
		time.sleep(2)

		#Clicando no campo do e-mail
		keyboard.press(Key.ctrl.value)
		keyboard.press('a')
		keyboard.release('a')
		keyboard.release(Key.ctrl.value)	

		time.sleep(1)

		#Digitando e-mail
		for c in username:
			keyboard.press(c)
			keyboard.release(c)
			time.sleep(0.12)
			
		#TECLA ENTER PARA PROXIMA ETAPA DE LOGIN
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		
		time.sleep(10)
		
		#TECLA ENTER PARA PROXIMA ETAPA
		i = 0
		while i<6:
			keyboard.press(Key.enter)
			keyboard.release(Key.enter)
			i= i + 1
			time.sleep(3)
	else:
		messagebox.showwarning("Login", "Por favor, preencha todos os campos!")

# Cria a janela principal
window = tk.Tk()
window.title("Login no OneDrive")

# Impede o fechamento da janela clicando no "X"
window.protocol("WM_DELETE_WINDOW", lambda: None)

# Cria os rótulos e campos de entrada
label_username = tk.Label(window, text="OneDrive \n Digite seu e-mail Moriah/Life:")
label_username.pack()
entry_username = tk.Entry(window)
entry_username.pack()

#label_password = tk.Label(window, text="Senha:")
#label_password.pack()
#entry_password = tk.Entry(window, show="*")  # A senha será ocultada por asteriscos
#entry_password.pack()

# Cria o botão de login
button_login = tk.Button(window, text="Login", command=login)
button_login.pack()

# Inicia o loop principal da aplicação
window.mainloop()

