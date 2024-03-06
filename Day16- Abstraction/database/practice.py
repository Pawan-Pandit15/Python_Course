class RBI:               # Parent class
    def interest_rate(self):
        pass

class SBI(RBI):          # child class
    def interest_rate(self):
        print("SBI interest rate is 7%")    # here SBI interest rate implement

class HDFC(RBI):          # child class
    def interest_rate(self):
        print("HDFC interest rate is 6%")    # here HDFC interest rate implement

# obj=SBI()
# obj.interest_rate()
# obj=HDFC()
# obj.interest_rate()