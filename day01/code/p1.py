a = 10
b = 20
c = a + b
s = 'hello'
# 注释
# 打印
print(c)
print(s)
# 条件语句
# 不及格 60 良好 90 优秀
# num = input()
# if int(num)<60:
#     #if成立执行的代码段
#     print("不及格")
# elif int(num)<90:
#     print("良好")
# else:
#     print("优秀")

# 导入模块
import time

# 函数
# 关键字 函数名（参数）：
#     函数体
def get_current_time():
    # 功能实现
    l_time = time.localtime()
    str_time = time.strftime('%Y-%m-%d',l_time)
    print(str_time)
#调用函数
get_current_time()
