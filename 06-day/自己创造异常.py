class ShowError(Exception):
	def __init__(self,len,leastlen):
		self.len = len
		self.leastlen = leastlen

def main():
		try:
			s = input('请输入')
			if len(s)<3:
				raise ShowError(len(s),3)
		except ShowError as result:
			print('ShowError:输入的长度是%d,长度至少是%d'%(ret.len,ret.leastlen))
		else:
				print('没有异常发生')

main()
