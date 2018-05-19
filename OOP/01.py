'''
定义一个学生类, 用来形容学生
'''
#定义一个空的类
class Student():
    pass

#定义一个对象
mingyue = Student()


#
class PythonStudent():
    #用none给不确定的值占位
    name = None
    age = 18
    course = "Python"
    
    def doHomework(self):
        print ("i am doing my homework")
        #推荐在函数末尾使用return语句
        return None

yueyue = PythonStudent()
print (yueyue.age)
print (yueyue.name)
yueyue.doHomework()
haha = PythonStudent()




    
        
