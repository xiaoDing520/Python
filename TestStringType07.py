# 字符串切片和案例参考 HelloWord01.py

"""
    转义字符串
        具有提出含义的字符,通过 \ 来表示,\ 也可去除转义字符

"""
# \ 续行符,当一行写不下可用于换行写
print("你好\
HelloWord")

# \ 本身就是转义字符,也可用过 \ 来转义字符
print("\\")

# 蜂鸣器响铃响铃
print("\a")

# 打印单引号和双引号
print('\'')
print("\"")

# 退格，消除一个空格
print("Hello \bWorld!")

# 空
print("\000")

# 换行
print("A\nB")

# 纵向制表符
print("Hello\vWorld!")
# 横向制表符
print("Hello\tWord")

# 回车,将 \r 后面的字符替换至 \r 前面的字符,全部替换
print("Hello\rWord")
print('google runoob taobao\r123456')

# 换页
print("Hello \f Word")

# 八进制数表示字符 \yyy y 表示 0 ~ 7 的字符
print("\110\145\154\154\157\40\127\157\162\154\144\41")

# 十六进制数表示字符 \xyy 以 x 开头, y 代表字符
print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")

# 其它的字符以普通格式输出
print("AAA\otherB\tB")
print()

"""
    字符串运算符
        + * [] [ : ] in %
        
    格式化符号   
        更多参照 w3c  
"""
# %c  将 ACSII 码转换成对应的值
str01 = '69'
print("%c" %(int(str01)))

# %s 占位符,%d 格式化为整形,%f 保留小数,可指定位数
num01 = 2.56
num02 = 3.562
print("字符串 %s,数字 %d,保留小数 %.2f" %(num01,num02,num02))


"""
    python 2.6 新增 format 方法,通过 {} 来代替参数,可指定名称赋值
    format 不限制参数数量
    如 {} 多个,参数一个则必须使用索引指定参数
    如 {} 多个,参数多个可指定也可不指定
    如传递传来的不是字符串向 list、tuple 或 字段,{} 指定获取参数之后,如想获取参数里面的某个值则必须根据参数原本类型的获取方式来获取,否则就是全部打印
    数字格式化参考 w3c
"""
print("你好{},欢迎加入{}".format("小明","w3c学堂"))
print("我是:{name},来自:{city}".format(name="小明",city="上海"))
# format 里面的参数可以使字符串、数字、List、字典、元组
list01 = ["AAA", "BBBB"]
tuple01 = ("我是","元组")
set = {"H", "L"}

print("{0[0]},{0[1]}".format(list01))
print("{0[0]},{0[1]}".format(tuple01))
print("{0},{0}".format(num02))
print("{0}".format(set))

# 字符串常用方法
# capitalize 首字母小写,其字母大小
print("AA".capitalize())

# center(with) 使用空格填充 with 长度,并将字符串居中
print("AAA".center(7))

# count(str,start,end)
# 判断字符在字符串里面出现的位置,如指定范围则在指定范围内查找
# 前包后包
str02="ajsdhfasds你好"
print(str02.count("s",0,len(str02)))

# 对字符串进行编码和解码
str_gbk = str02.encode("GBK")
str_utf_8 = str02.encode("UTF-8")
print(str_gbk)
print(str_utf_8)
print(str_gbk.decode("GBK"))
print(str_utf_8.decode("UTF-8"))

# 判断字符串是否以什么开头,可指定范围
print(str02.startswith("a"))
# 判断字符串是否以什么结尾,可指定范围
print(str02.endswith("s"))