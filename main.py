import torch

print("CUDA 可用：", torch.cuda.is_available())
print("CUDA 版本：", torch.version.cuda)
print(torch.backends.cudnn.enabled)
print(torch.backends.cudnn.version())

# # 变量定义
# x = 10          # 整数
# y = 3.14         # 浮点数
# name = "Alice"   # 字符串
# is_active = True # 布尔值
#
# # 多变量赋值
# a, b, c = 1, 2, "three"
#
# # 查看数据类型
# print(type(x))        # <class 'int'>
# print(type(y))        # <class 'float'>
# print(type(name))     # <class 'str'>
# print(type(is_active)) # <class 'bool'>
# list = ['a', 'b', 'c']
# print(list * 2)