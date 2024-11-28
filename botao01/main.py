import flet as ft
from flet_contrib.color_picker import ColorPicker

def main (page: ft.Page):
	page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
	
def atualizar_botao(e):
	botao_principal.text = texto_botao.value
	botao_principal.width = largura_botao.value
	botao_principal.height = altura_botao.value
	botao_principal.icon = icone_botao.value
	if estilo_botao.value == ‘Stadium Border’:
		botao_principal.style = ft.ButtonStyle(shape = ft.StadiumBorder())
	elif estilo_botao.value == ‘Rounded rectangle’:
		botao_principal.style = ft.ButtonStyle(shape = ft.Rounded rectangle())
	elif estilo_botao.value == ‘Circle’:
		botao_principal.style = ft.ButtonStyle(shape = ft.CircleBorder(), padding)


	page.update()

texto_botao = ft.TextField(
	label = “Texto do botão”,
	hint_text = “Clique aqui”,
	value = ‘Clique aqui’,
	on_change = atualizar_botao
)


largura_botao = ft.Slider(
	label = ‘{value}’,
	min = 100,
	max = 1000,
	value = 100,
	divisions = 10,
	on_change = atualizar_botao
)



	
altura_botao = ft.Slider(
	label = ‘{value}’,
	min = 40,
	max = 200,
	value = 100,
	divisions = 40,
	on_change = atualizar_botao
)


icone_botao = ft.DropDown(
	options = [
		ft.dropdown.Option (‘ADD_HOME’),
		ft.dropdown.Option (‘AUTO DELETE’’),
		ft.dropdown.Option (‘SAVE’’),
],

on_change = atualizar_botao,
value = ‘ADD HOME’,
),


estilo_botao = ft.RadioGroup(
	content = ft.Column([
		ft.Radio(label = ‘StadiumBorder’, value = ‘StadiumBorder’),
		ft.Radio(label = ‘Rounded rectangle’, value = Rounded rectangle),
		ft.Radio(label = Circle, value = Circle),
]),


on_change = atualizar_botao,
value = ‘StadiumBorder’,
)


def abrir_color_picker(e):
	page.dialog = dialogo_cor
	dialogo_cor.open  = True
	page.update()
def fechar_color_picker(e):
	dialogo_cor.open = False
	page.update()


cor_botao = ft.IconButton(
	icon = ft.icons.BRUSH,
	on_click = abrir_color_picker
)



color_picker  = ColorPicker(
	color = ‘#FF0000’,
	width = 300,
)


dialogo_cor = ft.AlertDialog(
	content = color_picker,
actions = [
	ft.TextButton(“Ok”, on_click = atualizar_botao),
	ft.TextButton(“Cancelar”, on_click = fechar_color_picker),
],



actions_aligment = ft.MainAxisAlignment.END,
)



botao_principal = ft.ElevatedButton(
	text = “Clique aqui”,
	bgcolor = “red”,
	color = “white”,
	elevation = 2,
	width = 100,
	height = 40,
)


page.add(
	botao_principal,
	texto_botao,
	ft.Row(controls=[ft.Text(‘Largura do botão:’), largura_botao]),
	ft.Row(controls=[ft.Text(‘Altura do botão:’), altura_botao]),
	ft.Row(controls=[ft.Text(Estilo do botão:’), estilo_botao]),
	ft.Row(controls=[ft.Text(‘Ícone do botão:’), icone_botao]),
	ft.Row(controls=[ft.Text(Cor de fundo do botão:’), cor_botao]),
)

atualizar_botao (None)


	



ft.app(target = main)

