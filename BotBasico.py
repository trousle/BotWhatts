webbrowser.open("https://web.whatsapp.com") # abrir whatsap no navegador
sleep(10) # espera um tempo determinado para continuar a execução do cód
pyautogui.hotkey("ctrl", "w")

workbook = openpyxl.load_workbook("contatos.xlsx") # fazer a leitura da planilha
pagina_contato = workbook["Página1"] # pegar pagina da planilha 

nome = ("Bielzito")
tel = 5541996584056
msg = f"Olá {nome}, métrica proxima a bater em jogo do {time1} vs {time2}" # mensagem automatizada
link = f"https://web.whatsapp.com/send?phone={tel}&text={quote(msg)}" # link para colocar a msg na conversa. 
webbrowser.open(link) # abrir o link com a mensagem
sleep(18)

#seta = pyautogui.locateCenterOnScreen("seta.png") # carregando arquivo de imagem 
#pyautogui.click(seta[0],seta[1]) # mostrando as coodenadas para clicar na imagem

pyautogui.hotkey("enter")
sleep(5)
pyautogui.hotkey("ctrl", "w") # usado para fechar a aba 
sleep(5) # tempo para recomeçar o cód  
             
# fechar navegador 
navegador.close()
navegador.switch_to.window(id_principal)
