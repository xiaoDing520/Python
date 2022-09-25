"""
    Number
        int         对比 Java 是 Long,在python没有限制大小
        float       浮点数,有效位 17 位
        complex     复数，有实数和虚数组成
"""
a = 10
b = 2.3
# 在混合运算中,整数会被转换为 浮点数
print(type(a + b))
# 删除对象引用,可删除多个,使用 , 隔开
# del a
# print(a)


"""
    数据类型转换
        强制类型转换（可能会发生丢失精度的问题）
            int()
            float()
            complex(x)
            complex(x,y)
        隐式转换
            python 自动帮我们转换   
            在混合运算中,会将整数转换成浮点数
            和 Java 有些不一样
            a = 1
            b = 2.3
            b = a //数据类型是 int
                     
"""
b = a
print(type(b))