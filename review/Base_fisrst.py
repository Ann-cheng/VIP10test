# 1-5:变量
#     标识符使用规则:由数字、字⺟、下划线组成
#                 不能数字开头
#                 不能使⽤内置关键字
#                 严格区分⼤⼩写
#     数据类型:
#             整型：int
#             浮点型：float
#             字符串：str
#             布尔型：bool
#             元组：tuple
#             集合：set
#             字典：dict
# 1-6:输出
#     格式化输出:
#         %s: 字符串
#         %d:有符号的⼗进制整数
#         %f:浮点数
#             tips:%06d，表示输出的整数显示位数，不⾜以0补全，超出当前位数则原样输出
#                  %.2f，表示⼩数点后显示的⼩数位数。
#     转义字符:\n：换⾏。
#            \t:制表符,一个tab键,四个空格的距离
#     结束符:print('内容',end="")
# 1-7:input('提示信息')
#     特点:1)一般把input存储到变量,方便处理
#         2)会把接收到的任意⽤户输⼊的数据都当做字符串处理。
# 1-8:字符串转换类型
#     int()
#     float()
#     str()
#     list()
#     tuple()
#     eval()
# 1-9:运算符

age=18
name='eom'
print('my age is',age)
print('my age is %d' %age)
print(f'my age is {age}')


