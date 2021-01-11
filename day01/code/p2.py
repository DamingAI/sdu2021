# 面向对象

# 类封装 飞机 坐标 宽高 移动
class Plane():
    # 必须定义构造方法
    def __init__(self,x,y,width,height):
        #super(Plane,self).__init__()
        self.x = x
        self.y = y
        self.w = width
        self.h = height
    # 功能方法
    def move(self,step):
        self.x = self.x + step

# 对象
p1 = Plane(0,0,100,100)
for item in range(10):
    p1.move(10)
    print(p1.x)

# 继承
# 定义 敌机 继承 飞机
class Emey(Plane):
    def __init__(self,x,y,width,height):
        #调用父类构造方法
        super(Emey,self).__init__(x,y,width,height)
    #发射子弹
    def shoot(self):
        print("射击")

e = Emey(10,10,100,100)
print(e.x)
e.move(1000)
print(e.x)
e.shoot()