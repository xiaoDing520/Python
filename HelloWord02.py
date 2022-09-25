# 定义斐波那契数列
a=0
b=1
while b<10:
    c=a
    a=b+a
    b=c
    print(str(a) + "," + str(b))
print("===========================")


# end 表示不换行,可定义字符串相隔内容
a,b=0,1
while b < 1024:
    print(b,end=",")
    a,b=b,a+b


## 使用 if 条件控制
print()
age=int(input("请输入你的年龄：\n"))
if age < 0:
    print("请输入正确的年龄")
elif age == 1:
    print("相当于 14 岁的人")
elif age == 2:
    print("相当于 22 岁的人")
elif age > 2:
    print("对应人的年龄：", (22 + (age - 2) * 5))


