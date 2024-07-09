#class UserManager:
#    def __init__(self, user):
#        self.user = user

#    def change_user_name(self, user_name):
#       self.user.user_name = user_name

#   def save_user(self):
#       file = open("users.txt", "a")
#       file.write(self.user.user_name + "\n")
#       file.close()

class User():
    def __init__(self, user):
        self.user = user


class UserNameChanger():
    def __init__(self):
        self.user = user

    def change_name(self, new_name):
        self.user = new_name


class SaveUser():
    def __init__(self, user):
        self.user = user

    def save(self):
        file = open("users.txt", "a")
        file.write(self.user)
        file.close()
