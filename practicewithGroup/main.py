# from array import array

# arr1 = array('i', [1, 2, 3, 4, 5])

# # Print each element
# # for n in arr1:
# #     print(n)

# # Print the overall length of the array (Outputs: 5)
# print(len(arr1))

# # print the type of the array (Outputs: <class 'array.array'>)
# print(type(arr1))



class Account:
    def __init__(self, owner, balance=0):

        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


class SavingsAccount(Account):  # inherits
    pass

s = SavingsAccount("Almaz", 1500)
s.deposit(500)
print(s.balance) # 2000

# super 
class SavingsAccount(Account):
    def __init__(self, owner, balance, rate): 
        super().__init__(owner, balance) # parent
        self.rate = rate # extra
def add_interest(self):
    self.balance += self.balance * self.rate

   



