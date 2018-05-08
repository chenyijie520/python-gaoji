class Father(object):

	def __init__(self,name):
		self.getGirl = 5
		self.name = name
	def getGirl(self):
		return self.__getGirl

	def getmoney(self):
		print('%s会挣钱')

	def sport(self):
		print('%s会为爱情鼓掌')

	def __girl(self):
		print('%s买了爱情三十六计')

	def askgirl(self):
		self.__girl()


class Son(Father):
	pass

yanzixiong = Son('闫子雄')
print(yanzixiong.getGirl())
yanzixiong.getmoney()
yanzixiong.sport()
yanzixiong.askgirl()		
