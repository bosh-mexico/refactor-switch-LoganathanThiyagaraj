# payment_system/processors/paypal_processor.py
# from payment_system.core.interfaces import PaymentStrategy #

class PayPalProcessor: # Inherit from PaymentStrategy if using ABC
    def process_payment(self, amount: float):
        print(f"Processing PayPal payment of ${amount:.2f} via PayPal API...")
