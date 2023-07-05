import PySimpleGUI as sg

class Interface:
	def __init__(self):
	
		layout = [
			[sg.Text('Produto desejado: ', size=(15, 0)), sg.Input(size=(60, 0), key='produto')],
			[sg.Text('Em quais sites você deseja pesquisar o produto?', size=(40, 0))],
		 	[
		 		sg.Checkbox('Mercado Livre', key='mercado_livre'), 
		 		sg.Checkbox('Amazon', key='amazon'), 
		 		sg.Checkbox('Shopee', key='shopee'), 
		 		sg.Checkbox('Magazine Luiza', key='magazine_luiza'),
	 		 	sg.Checkbox('Shein', key='shein')
			],
			[sg.Button('Enviar Dados')]
		]

		janela = sg.Window('Pesquise seu produto em diferentes sites: ', size=(550,130)).layout(layout)
	
		self.button, self.values = janela.Read()

tela = Interface()
tela.Iniciar()