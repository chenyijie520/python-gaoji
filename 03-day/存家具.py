class Home:

	def __init__(self, area):
		self.area = area 
		self.place = place
		self.price = price
	def __str__(self):
		msg = "当前房子可用面积为:" +str(self.area)
		if len(self.place) > 0:
			msg = msg + "容纳的物品:"
		for temp in self.place:
			msg = msg + temp.getName()+"+"
		msg = msg.strip(',')
		return msg
	def accommodateItem(self,item):

		needArea = item.getUsedArea()
		if self.area > needArea:
			self.containsItem.append(item)
			self.area -= needArea
			print("ok:已经存放到房间中")
		else:
			print("err:房间可用面积为:%d,但是当前要存放的物品需要的面积为%d"%(self.area, needArea)



class Amani():

	def __init__(self,price,name):
		self.price = price
		self.name = name
	def __str__(self):
me = Home(120,"北京东城区长安大街666号",1200,"三室二厅")

print(myHome)



ximengsi = Bed(40,"席梦思")

print(ximengsi)



benladeng = Light("本拉登")

print(benladeng)



myHome.addLight(benladeng)



for i in range(10):

	myHome.switch()

myHome.addBed(ximengsi)

myHome.addBed(ximengsi)

myHome.addBed(ximengsi)

myHome.addBed(ximengsi)

myHome.addBed(ximengsi)

myHome.addBed(ximengsi)

myHome.addBed(ximengsi)

myHome.addBed(ximengsi)

myHome.addBed(ximengsi)

myHome.addBed(ximengsi)

myHome.addBed(ximengsi)
		msg = "口红的品牌是%s数量是%d"
		return msg
	def getArea(self):
			return self.area
class Light():

	def __init__(self,name):
			self.name = name
			self.isopen = False
	def __str__(self):
			msg = "我叫%s灯"%self.name
			return msg

	def open(self):
			self.isopen = True
			print('灯亮了')
	def close(self):
			self.isopen = False
			print('灯灭了')

	def getIsopen(self):
			return self.isopen


