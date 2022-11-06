"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name
        self.pay=""
        self.contractType=""
        self.comissionType=""
        self.contractHours=""
        self.payHourly=""
        self.payMonthly=""
        self.noOfContracts=""
        self.payContract=""
        self.bonus=""
        

    def get_pay(self):
        return self.pay

    def __str__(self):
        if(self.contractType=="monthly" and self.comissionType=="fixed"):
            return f'{self.name} works on a monthly salary of {self.payMonthly} and receives a bonus commission of {self.bonus}.  Their total pay is {self.pay}.'
        elif(self.contractType=="monthly" and self.comissionType=="bonus"):
            return f'{self.name} works on a monthly salary of {self.payMonthly} and receives a commission for {self.noOfContracts} contract(s) at {self.payContract}/contract.  Their total pay is {self.pay}.'
        elif(self.contractType=="hourly" and self.comissionType=="fixed"):
            return f'{self.name} works on a contract of {self.contractHours} hours at {self.payHourly}/hour and receives a bonus commission of {self.bonus}.  Their total pay is {self.pay}.'
        elif(self.contractType=="hourly" and self.comissionType=="bonus"):
            return f'{self.name} works on a contract of {self.contractHours} hours at {self.payHourly}/hour and receives a commission for {self.noOfContracts} contract(s) at {self.payContract}/contract.  Their total pay is {self.pay}.'
        elif(self.contractType=="hourly"):
            return f'{self.name} works on a contract of {self.contractHours} hours at {self.payHourly}/hour.  Their total pay is {self.pay}.'
        elif(self.contractType=="monthly"):
            return f'{self.name} works on a monthly salary of {self.pay}.  Their total pay is {self.pay}.'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.contractType="monthly"
billie.pay=4000

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.contractType="hourly"
charlie.contractHours=100
charlie.payHourly=25
charlie.pay=charlie.contractHours*charlie.payHourly
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.contractType="monthly"
renee.comissionType="bonus"
renee.payMonthly=3000
renee.noOfContracts=4
renee.payContract=200
renee.pay=renee.payMonthly+(renee.noOfContracts*renee.payContract)
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.contractType="hourly"
jan.comissionType="bonus"
jan.contractHours=150
jan.payHourly=25
jan.noOfContracts=3
jan.payContract=220
jan.pay=(jan.contractHours*jan.payHourly)+(jan.noOfContracts*jan.payContract)
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.contractType="monthly"
robbie.comissionType="fixed"
robbie.payMonthly=2000
robbie.bonus=1500
robbie.pay=robbie.payMonthly+robbie.bonus
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.contractType="hourly"
ariel.comissionType="fixed"
ariel.contractHours=120
ariel.payHourly=30
ariel.bonus=600
ariel.pay=(ariel.contractHours*ariel.payHourly)+ariel.bonus