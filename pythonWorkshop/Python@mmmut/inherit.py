class account(object):
    def get_balance(self):
        print  "get balance"
    def debit(self,amt):
        print ("debit")

class current_account(account):
    def current_config(self):
        print ("current")
    def debit(self,amt):
        print ("you cannot debit before maturity")



obj = current_account()
obj.get_balance()
obj.debit(90)

            
