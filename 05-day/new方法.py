class A(object):

	def __init__(self):
		print('这是init方法')

	def __new__(cls):
		print('这是new方法')
		return object.__new__(cls)

	def __str__(self):
		return 'str方法'

	def __del__(self):
		print('del方法')


a = A()
print(a)

