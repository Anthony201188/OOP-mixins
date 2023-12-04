class Validationmixin: 
   
    def __init__(self, value) -> bool:
        self.value = value
    
    def validate(self, value):

        if value == str(value):
            print("Value is a valid string input")
            value = True
            return value

        
        else: 
            print("Value is of type other than string please try again")
            value = False
            return value

class User(Validationmixin):  # think this might be inherited and not mixed in! 
    def __init__(self,user_name) -> None:
        super().__init__(user_name)   # passing "user_name" to the mixin class parameter "value"
          
        self.user_name = user_name
        self.value = self.validate(user_name) #  we inherited the validate method from the mixin and then pass the "user_name" to it



##### test case 1 ######
# print()
# test = User("john")
# test2 = User(5)
# print()
# print(f"Test case 1 should be True and is [{test.value}]")
# print(f"This is becasue the following value [{test.user_name}] is/is not a valid string")
# print()
# print(f"Test case 2 should be False and is [{test2.value}]")
# print(f"This is becasue the following value [{test2.user_name}] is/is not a valid string")

# print() # note that the class needs to be instantiated to print the value attribute
# obj = Validationmixin(5)
# print(obj.value)

# print() # note that we need to pass the instance of the class to access the .validate method directly and trigger side effect print stat
# Validationmixin.validate(obj, 5)
# Validationmixin.validate(obj, "john")

######## test case 2 ######

obj2 = User(1114)
obj2 = User("john")
obj2.validate(552214)
obj2.validate("john")
