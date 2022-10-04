# 单行注释
"""
    多行注释
"""
'''
    多行注释
'''

"""
    可变数据
        List（列表）
        Dictionary（字符串）
        Set（集合）
    不可变数据类型    
        Number 数字
        String 字符串
        Tuple（元组）
    
"""


"""
    变量定义
        变量名 = 值
        变量名1,变量名2  = 值1,值2
"""


# 字符串
# 不是真正的换行
print("A"
      "B")
# 转义字符换行
print("A\nB")
# 无视转义字符
print(r"无视转义字符\n")


# 字符串截取
str02="ABCDEFGHIJKLMN"
# 只打印索引所在位置的字符
print(str02[0])
# 取前几位
print(str02[:3])
# 从起始索引开始，一直打印到最后
print(str02[0:])
# 前包后不包
print(str02[0:5])
#  使用步长
print(str02[0:13:2])


# 程序输入
x=input("请输入内容\n")
print(x)
print(type(x))
print("========================================")


# python 以回车作为结束符,一行如何多个代码使用 ; 来间隔,不推荐一行多个代码
number01=2; number02=3;
print(number01)
print(number02)


# 向 if、while、for 等语句，通过 : 表示下面还有代码，当前代码块没有结束
if True:
    print("A")
else :
    print("B")


# 打印输出不换行
x="1"
y="2"
print(x,end=" ")
print(y)


"""
    导入模块
        import  模块              导入整个模块
        from 模块 import 函数名    某个模块导入某个函数,函数可以导入多个使用 , 区分
        from 模块 import *        导入某个模块所有函数
"""


# 命令行参数 python -h 参数说明
