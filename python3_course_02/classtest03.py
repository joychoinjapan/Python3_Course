class UserData:
    def __init__(self,id,name):
        self.id=id
        self.name=name

class NewUser(UserData):
    group = 'shiyanlou-louplus'
    def __init__(self,id,name):
        super().__init__(id,name)

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        if len(value)>3 and isinstance(value,str):
            self.__name=value
        else:
            print('Error')
    # @classmethod
    # def get_group(cls):
    #     return cls.group
    # @staticmethod
    # def format_userdata(id,name):
    #     return name+"'s id is "+str(id)

if __name__ == '__main__':
    user1 = NewUser(101, 'Jack')
    user1.name = 'Lou'
    user1.name = 'Jackie'
    user2 = NewUser(102, 'Louplus')
    print(user1.name)
    print(user2.name)