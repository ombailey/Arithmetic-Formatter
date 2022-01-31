class Category:
    
    def __init__(self,name):
        self.name = name
        self.funds = 0
        self.ledger = []

    def deposit(self,amount, description = ''):
        self.amount = amount
        self.description = description
        self.ledger.append({'amount': self.amount, 'description': self.description})
        self.funds = self.funds + self.amount

    def withdraw (self,amount, description):
        self.amount = amount
        self.description = description
        if self.amount > self.funds:
            return False
        if self.amount <= self.funds:
            self.ledger.append({'amount': -self.amount, 'description': self.description})
            self.funds = self.funds - self.amount
            return True
        
    def getbalance (self):
        return self.funds

    def transfer (self, amount, category):
        self.amount = amount
        self.category = category

        if self.amount > self.funds:
            return False
        else:
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True

    def check_funds(self, amount):
        self.amount = amount
        if self.amount > self.funds:
            return False
        else:
            return True

    def __str__(self):
        data = [str(self.name).title().center(30, '*')]

        for item in self.ledger:
            descrip = item['description'][:23]
            data.append(f'{descrip:<23} {item["amount"]:>7.2f}')
        
        data.append(f'Total: {self.funds :.2f}')
        return ('\n'.join(data))

    def spent(self):
        money = 0
        for item in self.ledger:
            if item['amount'] < 0:
                money += item['amount']
        return money

def create_spend_chart(lst):
    print ('Percentage spent by category')
    totalspent = 0
    spending = []
    bargraph = []
    for category in lst:
        spending.append(category.spent())

    totalspent = sum(spending)
    
    for num in range (0,10):
        level = 100 - (10*num)
        line = f'{level:<3}| '
        for category in lst:
            if ((category.spent() / totalspent) * 100 )>= level:
                line += 'o  '     
            else:
                line += '   '
        bargraph.append(line)
    
    bargraph.append(f'    {"-" * (len(line) -4)}')

    names = [category.name for category in lst]
    longestname = max(map(len, names))
    
    for num in range(longestname):
        line = '    '
        for name in names:
            if len(name) > num:
                line += ' ' + name[num]
            else:
                line += '  '
            line += ' '

        bargraph.append(line)

    return('\n'.join(bargraph))