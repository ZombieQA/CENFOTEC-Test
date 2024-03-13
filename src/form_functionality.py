class Form:
    def enter_name(self, name: str):
        if len(name) > 30:
            return 'name has more than 30 chars'
        elif len(name) < 3:
            return 'Invalid value'
        else:
            return "Your name is " + name

    def enter_age(self, age: str):
        if len(age) < 3:
            return 'Invalid value for field age'