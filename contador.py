# 1º Configurações iniciais
# importar as bibliotecas do flet para o nosso projeto
import flet as ft

# definir a função main()
def main(page: ft.Page):
    
    # 2º - Definir o título para a interface
    page.title = 'Contador'
    # Definir o alinhamento dos componentes na interface
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Definição da variável número como TextField
    numero = ft.TextField(value='0', width=100, text_align=ft.TextAlign.CENTER)

    # função subtrair()
    def subtrair(i):
        # Recebe o value do TextField, converte em INT, subtrai 1, converte em STR, devolve para o TextField
        numero.value=str(int(numero.value) - 1)
        numero.update()

    def somar(i):
        # Recebe o value do TextField, converte em INT, subtrai 1, converte em STR, devolve para o TextField
        numero.value=str(int(numero.value) + 1)
        numero.update()   

    # 3º Criar a área da página
    page.add(
        # 4º Criar uma linha para adicionar os elementos na página
        ft.Row(
            # 5º Adicionar o controle[] para receber: (-) número (+)
            # controle[] >> Permite adicionar funções/ações nos elementos da página
            controls=[
                # Adicionar os elementos
                # A função IconButton() executa a exibição do ícone REMOVE escolhido e armazenado em 'icons='
                # Criar a variável 'número', sendo um TextField >> Criar 'número' fora da page()
                ft.IconButton(icon=ft.icons.REMOVE, on_click=subtrair), numero, ft.IconButton(icon=ft.icons.ADD, on_click=somar),
                
    # 6º Criar o evento click e executar as funções subtrair() e somar ()  
    # Evento click >> adicionado após REMOVE e após ADD          
    # 7º Construir as funções subtrair() e somar()
    # Devem ser criadas fora da página(page)
            ]
              )
            )
    page.update()
ft.app(target=main)







