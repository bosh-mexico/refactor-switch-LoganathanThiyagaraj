# payment_system/processors/creditcard_processor.py
# from payment_system.core.interfaces import PaymentStrategy # Uncomment if using ABC

class CreditCardProcessor: # Inherit from PaymentStrategy if using ABC
    def process_payment(self, amount: float):
        print(f"Processing Credit Card payment of ${amount:.2f} via Credit Card Gateway...")
