class Person:
    def __init__(self, name, sex, profession):
        # date members(instance variables)
        self.name = name
        self.sex = sex
        self.profession = profession
    
    # Behavior (instance methods) 
    def show(self):
        print('Name', self.name, 'Sex', self.sex, 'Profession', self.profession)
    
    # Behavior (instance methods)
    def work(self):
        print(self.name, 'working as a', self.profesison)
