# payment_system/processors/googlepay_processor.py
# from payment_system.core.interfaces import PaymentStrategy # Uncomment if using ABC

class GooglePayProcessor: # Inherit from PaymentStrategy if using ABC
    def process_payment(self, amount: float):
        print(f"Processing GooglePay payment of ${amount:.2f} via GooglePay API...")
