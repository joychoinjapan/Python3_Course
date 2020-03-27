class UserData:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def __repr__(self):
        return 'ID:{}'.format(self.id)+' '+'Name:{}'.format(self.name)

class NewUser(UserData):
    group = 'shiyanlou-louplus'
    def __init__(self,id,name):
        super().__init__(id,name)
    def set_name(self,value):
        self.name=value
    @classmethod
    def get_group(cls):
        return cls.group
    @staticmethod
    def format_userdata(id,name):
        return name+"'s id is "+str(id)

if __name__ == '__main__':
    print(NewUser.get_group())
    print(NewUser.format_userdata(109,'Lucy'))