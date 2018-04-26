f = open('xxx珍藏版.txt','w')
vf.write('在座的都是垃圾\n')
f.close()



f1 = open('xxx珍藏版.txt','r')
f2 = f1.read()
f1.close()

f3 = open ('xxx珍藏版复制.txt','w')
f3.write(f2)
f3.close()
