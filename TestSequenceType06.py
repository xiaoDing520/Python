# 字符串序列相加
str01 = "HelloWord"
print(str01 + "0111")

# 字符串序列相乘
str02 = str01*3
str03 = "w3c"*3
print(str02)
print(str03)

# list 序列 + 和 *
list01 = [None]*5
print(list01)
print(type(None))

"""
    序列 +
        拼接序列类型，但是左右两边的数据类型都一样
    序列 *
        可以初始化序列值 或 配合序列变量使用
        重复序列内容    
    序列切片和索引参考 HelloWord01.py    
        
        
        
    可配合 成员运算符使用    
        
    None 
        在不知道赋予变量什么值的时候可以使用
        当变量不在需要时，可赋值为 None，原先对象由于没有被对象引用，会被垃圾回收机制收回
"""

# tuple 序列 + 和 *
tuple01 = ("a","b","c","d")
tuple02 = ("A")*3
print(tuple01 + tuple(("e")))
print(tuple02)