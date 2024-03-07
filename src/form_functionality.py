class Form:
    def enter_name(self, name: str):
        if len(name) > 30:
            return 'name has more than 30 chars'
        else:
            if len(name) < 3:
                return 'Invalid value'
        return "Your name is " + name

    def enter_age(self, age: str):
        if len(age) < 3:
            return 'Invalid value for field age'
