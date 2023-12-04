Create a mixin called ValidationMixin that adds validation functionality to a class. 
The mixin should include a method called validate() that takes a value as an argument and checks if it meets certain criteria.

Create a class called User that inherits from the ValidationMixin and includes a method called set_username(). 
This method should take a username as an argument, validate it using the validate() method from the mixin, and set it as the username attribute of the User class.