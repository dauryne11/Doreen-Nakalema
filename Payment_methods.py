

# Payment Details

# Parent class for Payment Methods
class PaymentMethod:
    def __init__(self, name):
        self.name = name

# Debit Card subclass
class DebitCard(PaymentMethod):
    def __init__(self, name, card_number):
        super().__init__(name)
        if len(card_number) != 16 or not card_number.isdigit():
            print("Error: Debit card number must be 16 digits.")
        else:
            self.card_number = card_number

# Credit Card subclass
class CreditCard(PaymentMethod):
    def __init__(self, name, card_number):
        super().__init__(name)  # Call the parent class initializer
        if len(card_number) != 12 or not card_number.isdigit():
            print("Error: Credit card number must be 12 digits.")
        else:
            self.card_number = card_number

# PayPal subclass
class Paypal(PaymentMethod):
    def __init__(self, name, email):
        super().__init__(name)
        if "@" not in email or "." not in email:
            print("Error: Invalid email address for PayPal.")
        else:
            self.email = email

# Invoice subclass
class Invoice(PaymentMethod):
    def __init__(self, name, email, address):
        super().__init__(name)
        if not name or not email or not address:
            print("Error: All fields (name, email, and address) are required for an invoice.")
        else:
            self.email = email
            self.address = address

#Testing Usage
debit = DebitCard("Doreen", "2349048629874456")
print(debit)
Paypal = Paypal("Jane", "jane.123@gmx.com")
print(Paypal)
invoice = Invoice("Alex","alesx@alex.com","Munich")
print(invoice)
