""" Create two Mixins:
UsernameLengthMixin
UsernameAlphanumericMixin
The mixin should include a method called validate() that takes a value as an argument and checks if it meets certain criteria.

Create a User class with a method called set_username().
Then combine the User class with your Mixin in the following new classes:
UserWithLengthValidation 
UserWithAlphanumericValidation
This method should take a username as an argument, validate it using the validate() method from the mixin, and set it as the username attribute of the User class.
Hint:
You don't need to use the super() keyword. """


##### classes ######

class UsernameLengthMixin:

    def validate(self,value):
        return len(value) < 5
      
class UsernameAlphanumericMixin:

    def validate(self,value):
        return value.isalnum()
      
class User:

    def set_username(self, user_name):
        self.user_name = None
        
        
        if self.validate(user_name):
            self.user_name = user_name
             
        else:
             print("invalid")


##### mixins  ######

class UserWithLengthValidation (User, UsernameLengthMixin):
        """ Validating the length of username """

class UserWithAlphanumerivValidation(User, UsernameAlphanumericMixin):
        pass

##### test case #####
obj = UserWithLengthValidation()
obj.set_username("john") 
print(f"Username set to: {obj.user_name}")
print()
########
obj2 = UserWithAlphanumerivValidation()
obj2.set_username("john") 
print(f"Username set to: {obj2.user_name}")
print()
