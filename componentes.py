# importar a biblioteca flet    
import flet as ft

# Definir a função main 
def main(page: ft.Page):
    # Define uma tela/interface vazia
    pass
    # armazenar o texto em uma variável
    texto = ft.Text(value='Técnico em Informática')

    # enviar o conteúdo de texto para a interface
    page.add(texto)

#fim da função main
ft.app(target=main)

