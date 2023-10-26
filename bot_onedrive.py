from pynput.keyboard import Key, Controller as KeyboardController
#from pynput.mouse import Button, Controller as MouseController #NÃO PRECISOU USAR
from pynput.keyboard import Key 
import time #AUXILIAR PARA DAR TEMPO DE CARREGAR O CONTEUDO DO ONEDRIVE E PARA O LOOP
import pyautogui # BIBLIOTECA PARA TIRAR SCREENSHOT
import cv2 #ABRIR A IMAGEM
import pytesseract #TRANSFORMAR IMAGEM EM TEXTO

#Controle do Teclado
keyboard = KeyboardController()

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
time.sleep(1)

#CHAMANDO A BIBLIOTECA PYAUTOGUI PARA PRINT
screen = pyautogui.screenshot()
#TIRANDO SCREENSHOT
screen.save('C:/Users/onedrive.png')
#ABRINDO IMAGEM 
time.sleep(1)
img = cv2.imread('C:/Users/onedrive.png')
#LOCAL DO ARQUIVO TESSERACT
pytesseract.pytesseract.tesseract_cmd = 'Q:/Infraestrutura/_COMUM_/Base de Conhecimento/Codigos_Bot_Automação/OneDrive_bot/Tesseract-OCR/tesseract.exe'
#SALVANDO TEXTO DA IMAGEM NUMA VARIAVEL
texto = pytesseract.image_to_string(img)
print(texto)

time.sleep(2)

#VARIAVEL PARA VALIDAR IF
#IF PARA CANCELAR LOOP
ok = False
if "Documentos" in texto:
	ok = True
if ok == False:
	#LOOP PARA FICAR ABRINDO ONEDRIVE
	while True:
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
		time.sleep(1)
		
		#CHAMANDO A BIBLIOTECA PYAUTOGUI PARA PRINT
		screen = pyautogui.screenshot()
		#TIRANDO SCREENSHOT
		screen.save('C:/Users/onedrive.png')
		#ABRINDO IMAGEM 
		time.sleep(1)
		img = cv2.imread('C:/Users/onedrive.png')
		#LOCAL DO ARQUIVO TESSERACT
		pytesseract.pytesseract.tesseract_cmd = 'C://Program Files/Tesseract-OCR/tesseract.exe'
		#SALVANDO TEXTO DA IMAGEM NUMA VARIAVEL
		texto = pytesseract.image_to_string(img)
		print(texto)

		time.sleep(2)
		
		#TEMPO PARA USUARIO LOGAR
		if "Documentos" in texto:
			ok = True
			break

		time.sleep(2)
		
		#TECLA WINDOWS
		keyboard.press(Key.cmd)
		keyboard.release(Key.cmd)
		
		time.sleep(1)
		
		#DIGITANDO BLOCO DE NOTAS NO PROCURAR DO WINDOWS
		for char in "Bloco de notas":
			keyboard.press(char)
			keyboard.release(char)
			time.sleep(0.12)
			
		#TECLA ENTER PARA ABRIR BLOCO DE NOTAS
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		
		time.sleep(1)
		
		#DIGITANDO TEXTO NO BLOCO DE NOTAS
		for char in "POR FAVOR, LOGAR NO ONEDRIVE!!":
			keyboard.press(char)
			keyboard.release(char)
			time.sleep(0.17)
		
		time.sleep(60)
		
