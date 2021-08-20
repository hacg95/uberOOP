from payment import Payment

class Credit(Payment):
    cardNumber = int
    cvv = int
    cardName = str

    def __init__(self, id, cardNumber, cvv, cardName):
        super().__init__(id)
        self.cardName = cardName
        self.cardNumber = cardNumber
        self.cvv = cvv