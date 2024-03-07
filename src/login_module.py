import re


class Login:
    email: str = ""
    password: str = ""

    def enter_user(self, email: str):
        self.email = email
        return self.validate_user()

    def enter_password(self, password: str):
        self.password = password

    def validate_user(self):
        message = ""
        if len(self.email) < 0:
            message = 'Email is mandatory'
        if self.email != "example@mail.com":
            message = 'Invalid credentials'
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, self.email):
            message = 'Valid email format'
        else:
            message = 'Invalid email'
        return message

    def validate_password(self):
        message = ""
        if len(self.password) < 0:
            message = 'password is mandatory'
        if self.password != "pass1234":
            message = 'Invalid password'
        else:
            message = "Valid password"
        return message

    def login(self):
        message1 = self.validate_user()
        message2 = self.validate_password()
        if message1 == "Valid email format" and message2 == "Valid password":
            return "Login success!"
        else:
            return  message1 + " " + message2
