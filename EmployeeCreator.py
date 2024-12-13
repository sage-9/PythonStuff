class Employee:

    def __init__(self,firstName,lastName,salary):
        self.firstName=firstName
        self.lastName=lastName
        self.salary=salary
    
    def giveRaise(self,amount=5000):
        self.salary=int(amount+self.salary)
        

        