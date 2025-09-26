from enum import Enum
import sys

# --- 1. PaymentMode Enum (remains the same) ---
class PaymentMode(Enum):
    PAYPAL = 1
    GOOGLEPAY = 2
    CREDITCARD = 3
    UNKNOWN = 99

# --- 2. Payment Strategy "Interface" (Implicit via Duck Typing) ---
# We no longer define an explicit abstract base class.
# Instead, any class that acts as a payment strategy must simply
# provide a 'process_payment(self, amount: float)' method.

# --- 3. Concrete Payment Strategies ---
class PayPalProcessor: # 
    """
    Concrete strategy for PayPal payments.
    """
    def process_payment(self, amount: float):
        # In a real application, this would call the PayPal API
        print(f"Processing PayPal payment of ${amount:.2f} via PayPal API...")
        # Example of returning a result (optional)
        # return {"status": "success", "transaction_id": "PP12345"}

class GooglePayProcessor: # No inheritance from ABC
    """
    Concrete strategy for GooglePay payments.
    """
    def process_payment(self, amount: float):
        # In a real application, this would call the GooglePay API
        print(f"Processing GooglePay payment of ${amount:.2f} via GooglePay API...")
        # Example of returning a result (optional)
        # return {"status": "success", "transaction_id": "GP67890"}

class CreditCardProcessor: # No inheritance from ABC
    """
    Concrete strategy for Credit Card payments.
    """
    def process_payment(self, amount: float):
        # In a real application, this would call a Credit Card gateway API
        print(f"Processing Credit Card payment of ${amount:.2f} via Credit Card Gateway...")
        # Example of returning a result (optional)
        # return {"status": "success", "transaction_id": "CC11223"}

# --- 4. Payment Context / Dispatcher ---
class PaymentProcessorContext:
    """
    The context class that uses a PaymentStrategy to process payments.
    This class orchestrates the payment flow.
    """
    # Map PaymentMode enum values to their corresponding strategy instances
    _strategies = {
        PaymentMode.PAYPAL: PayPalProcessor(),
        PaymentMode.GOOGLEPAY: GooglePayProcessor(),
        PaymentMode.CREDITCARD: CreditCardProcessor(),
        # New strategies are added here without modifying the checkout method.
    }

    @staticmethod
    def checkout(mode: PaymentMode, amount: float):
        """
        Processes a payment using the appropriate strategy based on the mode.
        """
        strategy = PaymentProcessorContext._strategies.get(mode)

        if strategy:
            try:
                strategy.process_payment(amount)
            except Exception as e:             
                print(f"Payment processing failed for {mode.name}: {e}", file=sys.stderr)
        else:
            print(f"Invalid payment mode selected: {mode.name}!")

# --- Example Usage ---
if __name__ == "__main__":
    amount = 150.75


    # Valid payments
    PaymentProcessorContext.checkout(PaymentMode.PAYPAL, amount)
    PaymentProcessorContext.checkout(PaymentMode.GOOGLEPAY, amount)
    PaymentProcessorContext.checkout(PaymentMode.CREDITCARD, amount)

    # Invalid payment mode
    PaymentProcessorContext.checkout(PaymentMode.UNKNOWN, amount)

