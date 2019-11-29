from registradores import Registradores

registradores = Registradores([], [])
filepath = 'programa.txt'

def get_valor_registrador(operando):
	if operando[1] == 's':
		return registradores.getS(int(operando[2]));
	elif operando[1] ==	't':	
		return registradores.getT(int(operando[2]));

def set_valor_registrador(operando, valor):
	if operando[1] == 's':
		return registradores.setS(int(operando[2]), valor);
	elif operando[1] ==	't':	
		return registradores.setT(int(operando[2]), valor);

with open(filepath) as fp:
	line = fp.readline()
	cnt = 1
	while line:
		linha = line.strip().split(' ')
		if linha[0] == 'ADDI':
			destino = list(linha[1])
			set_valor_registrador(destino, linha[3])

		elif linha[0] == 'ADD':
			destino = list(linha[1])
			primeiro_operando_valor = int(get_valor_registrador(list(linha[2])))
			segundo_operando_valor = int(get_valor_registrador(list(linha[3])))
			set_valor_registrador(destino, primeiro_operando_valor + segundo_operando_valor)
			
		elif linha[0] == 'SUB':
			destino = list(linha[1])
			primeiro_operando_valor = int(get_valor_registrador(list(linha[2])))
			segundo_operando_valor = int(get_valor_registrador(list(linha[3])))
			set_valor_registrador(destino, primeiro_operando_valor - segundo_operando_valor)

		else:
			print('hello')

		line = fp.readline()
		cnt += 1
