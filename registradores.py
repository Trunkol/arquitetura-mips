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
