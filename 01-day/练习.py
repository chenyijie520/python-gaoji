file_name = input('请输入文件的名字要带后缀名')
old_file = open(file_name,"r")
content = old_file.read()


position = file_name.rfind('.')
file_name[0:position:]
file_name[position:]

new_file = open(file_name+"复制"+'1.txt','w')
new_file.write(content)

old_file.close()
new_file.close()
