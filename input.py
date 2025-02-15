import flet as ft

def main(page: ft.Page):

    # Definições de variáveis
    titulo = ft.Text(value='CADASTRO DE CLIENTES')
    textoIdade = ft.Text(value='Digite a sua idade:')
    idade = ft.TextField(value='0')
    
    #cor do background
    page.bgcolor = 'grey'

    # centralizar o texto na interface
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    

    #título na aplicação
    page.title='Input'
    
    #função soma() e sub()
    def soma(e):
        idade.value = str(int(idade.value) + 1)
        idade.update()

    def sub(e):
        idade.value = str(int(idade.value) - 1)
        idade.update()


    page.add(
            #add uma linha para conter o controle
        ft.Row(
            #interligar os 3 elementos
            controls=[
                #add ícone (-)
                ft.IconButton(icon=ft.icons.REMOVE, on_click=sub),
                #add o campo de idade:
                idade, 
                #add ícone (+)
                ft.IconButton(icon=ft.icons.ADD, on_click=soma),
            ]
        )
    )
    # Atualiza a página
    page.update()

    #page.add(titulo,textoIdade)
    
ft.app(target=main)