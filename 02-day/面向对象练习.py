class Pig:
	def eat(self):
		print('猪饲料')
	def sleep(self):
		print('雪曼哼哼叫')
	def intorduce(self):
		print('我是%s年龄%d颜色%s'%(self.name,self.age,self.color))



cuiliyan = Pig()
cuiliyan.name = '崔丽艳'
cuiliyan.age = 17
cuiliyan.color = '黄色'
cuiliyan.eat()
cuiliyan.sleep()
cuiliyan.intorduce()



louxueman = Pig()
louxueman.name = '娄雪嫚'
louxueman.age = 17
louxueman.color = '白色'
louxueman.eat()
louxueman.sleep()
louxueman.intorduce()



zhangxuanxuan = Pig()
zhangxuanxuan.name = '张轩轩'
zhangxuanxuan.age = 20
zhangxuanxuan.color = '黑色'
zhangxuanxuan.sleep()
zhangxuanxuan.intorduce()
