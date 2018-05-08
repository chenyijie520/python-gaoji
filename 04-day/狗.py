class  Dog():

	def __init__(self,age):
		self.age = 0


	def wark(self):
		print('汪汪叫')

	def setAge(self,age):
		if age <= 0:
			print('传入年龄有误')
		else:
			self.__age = age

	def getAge(self):
		return self.__age

	def __str__(self):
		return'狗的年龄是%d'%self.__age



xiaohuang = Dog()
xiaohuang.setAge(10)
xiaohuang.__age()
print(xiaohuang.getAge())
print(xiaohuang)
xiaohuang.walk()
