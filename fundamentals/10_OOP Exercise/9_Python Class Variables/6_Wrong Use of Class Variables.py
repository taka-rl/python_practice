'''
In Python, we should properly use the class variable because all objects share the same copy. 
Thus, if one of the objects modifies the value of a class variable, then all objects start referring to the fresh copy.

'''

class Player:
    # class variables
    club = "Chelsea"
    sport = "Football"
    
    def __init__(self, name):
        # Instance variable
        self.name = name
        
    def show(self):
        print("Player:", "Name:", self.name, "Club:", self.club, "Sports:", self.sport)

p1 = Player("John")

# wrong use of class variable
p1.club = "FC"
p1.show()

p2 = Player("Emma")
p2.sport = "Tennis"
p2.show()

Player.club = "FC"
Player.sport = "Tennis"

# actual class variable value
print("Club:", Player.club, "Sport:", Player.sport)

'''
In the above example, the instance variable name is unique for each player. 
The class variable team and sport can be accessed and modified by any object.
Because both objects modified the class variable, a new instance variable is created for that particular object with the same name as the class variable, which shadows the class variables.
In our case, for object p1 new instance variable club gets created, and for object p2 new instance variable sport gets created.
So when you try to access the class variable using the p1 or p2 object, it will not return the actual class variable value.
To avoid this, always modify the class variable value using the class name so that all objects gets the updated value. Like this

Player.club = 'FC'
Player.sport = 'Tennis'

'''
