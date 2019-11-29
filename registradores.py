class Registradores(object):
	def __init__(self, t, s):
		self.t = [0, 0, 0, 0, 0, 0, 0, 0]
		self.s = [0, 0, 0, 0, 0, 0, 0, 0]
		
	def setT(self, posicao, valor):
		self.t[posicao] = valor

	def setS(self, posicao, valor):
		self.s[posicao] = valor

	def getS(self, posicao):
		return self.s[posicao]

	def getT(self, posicao):
		return self.t[posicao]

	def pretty_print(self):
		print("Registradores $t \t Registradores $s")
		for x in range(8):
			print('t{}: {} \t\t\t s{}: {}'.format(x, self.t[x], x, self.s[x])) 
