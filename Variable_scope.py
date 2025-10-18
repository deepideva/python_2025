# Local Variable --> Enclosing Variables --> Global Variables --> Built-in Variable

#Local variable
'''def order():
    food="Idly"
    print("Your Food is : ", food)
order()'''

#Enclosing Variable
'''def cart():
    discount=10

    def checkout():
        print("Your Discounted % is : ",discount)
    checkout()
cart() '''

#Global Variable
'''user="DeepiDeva"
def homepage():
    print("Welcome to HomePage: ",user)
def page1():
    print("Welcome to Page1: ",user)
homepage()
page1() '''

#Built-In Variables
print(__file__)

