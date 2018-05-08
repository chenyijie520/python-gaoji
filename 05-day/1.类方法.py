class Dog(object):
	count = 1
	def __init__(self,name):
		self.name = name
		
	
	def jiao(self):
		print("汪汪叫")

	@classmethod
	def test(cls):
	
		return cls.count

taidi = Dog('泰迪')
print(taidi.name)
taidi.jiao()
print(taidi.test())

