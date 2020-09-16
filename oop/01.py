'''
定义一个学生类，用来形容学生
'''
# 定义一个空类
class Student():
    # pass一个占位符，表示直接跳过
    pass

# 定义一个对象
mingyue = Student()

# 定义一个描述学习python的学生
class PythonStudent():
    # 用None表示不确定的赋值
    name = None
    age = 18
    course = "python"

    def doHomework(self):
        print("I 在做作业")
        #推荐使用return语句
        return None
# 实例化一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)

