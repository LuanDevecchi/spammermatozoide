import re
import sys

mensagem_arg = """ 
    ____ ___  ____ _  _ _  _ ____ ____ _  _ ____ ___ ____ ___  ____ _ ___  ____ 
    [__  |__] |__| |\/| |\/| |___ |__/ |\/| |__|  |  |  |   /  |  | | |  \ |___ 
    ___] |    |  | |  | |  | |___ |  \ |  | |  |  |  |__|  /__ |__| | |__/ |___ 
                                                                                

                       ____      Codado por: Natanael Antonioli
       ______     ___.'  o `.    "Esse software tá uma porra"
      /~----,\___/,--.   ,_ |    https://twitter.com/_natanael666
            `-----'   `---'`     https://github.com/NatanaelAntonioli/spammermatozoide

 """

mensagem_inicial = """
    ____ ___  ____ _  _ _  _ ____ ____ _  _ ____ ___ ____ ___  ____ _ ___  ____ 
    [__  |__] |__| |\/| |\/| |___ |__/ |\/| |__|  |  |  |   /  |  | | |  \ |___ 
    ___] |    |  | |  | |  | |___ |  \ |  | |  |  |  |__|  /__ |__| | |__/ |___ 
                                                                                

                       ____      Codado por: Natanael Antonioli
       ______     ___.'  o `.    "Esse software tá uma porra"
      /~----,\___/,--.   ,_ |    https://twitter.com/_natanael666
            `-----'   `---'`     https://github.com/NatanaelAntonioli/spammermatozoide

    1)Selecione todo o texto que deseja filtrar (CTRL+A em navegadores)
    2)Salve-o em um arquivo no mesmo diretório do script.
    3)Digite o nome do arquivo e pressione enter.
    4)O resultado final será enviado para "list-parsed.txt".
        """



# Parse Function
def parse_txt(txt_str):
	count = 0
	line = tr = open(txt_str, 'r').read() 
	match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
	try:
		f = open('list-parsed.txt', 'w')
		for i in match:
		    i = i.lower()
		    count+=1
		    f.write(i + '\n')
		f.close()
		print('[*] {} Email(s) encontrados.'.format(count))
	except Exception:
		print('[X] Arquivo inválido.')

# Arg-Check Function
def check_if_arg():
	try:
		if len(sys.argv[1]) > 0:
			print(mensagem_arg)
			print('Parsing {}'.format(sys.argv[1]))
			parse_txt(sys.argv[1])
			exit()
		else:
			print (mensagem_inicial)
	except Exception:
			print (mensagem_inicial)


# Main func
if __name__ == "__main__":
	check_if_arg()
	set_file = input("[+] Digite o nome do arquivo: ")
	try:
		parse_txt(set_file)
	except Exception:
		print('[X] Arquivo não encontrado.')
