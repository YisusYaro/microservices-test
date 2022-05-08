class RegisterUserCommand(object):
    def __init__(self, name, email, age, password):
        self.name = name
        self.email = email
        self.age = age
        self.password = password
