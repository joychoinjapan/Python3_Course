class UserData:
    def __init__(self,id,name):
        self.id=id
        self.name=name

class NewUser(UserData):
    def __init__(self,id,name):
        super().__init__(id,name)
    def __call__(self):
        print(self.name+"'s"+' id is '+str(self.id))

if __name__ == '__main__':
    user = NewUser(101, 'Jack')
    user()