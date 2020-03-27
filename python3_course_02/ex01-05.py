#私有属性和方法
#在 Python 中约定在属性方法名前添加 __ （两个下划线 _）来拒绝外部的访问。
class Shiyanlou:
    __private_name = 'shiyanlou'
    def __get_private_name(self):
        return self.__private_name

s = Shiyanlou()
print(s._Shiyanlou__get_private_name())
print(s._Shiyanlou__private_name)

