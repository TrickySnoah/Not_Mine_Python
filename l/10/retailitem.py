class RetailItem:
    def __init__(self,name,amount,price):
        self.name=name
        self.amount=amount
        self.price=price
    def __str__(self):
        return(f"{self.name}\n{self.amount}\n{self.price}\n")
    def name(self):
        return f"{self.name}"
    def amount(self):
        return f"{self.amount}"
    def price(self):
        return f"{self.price}"