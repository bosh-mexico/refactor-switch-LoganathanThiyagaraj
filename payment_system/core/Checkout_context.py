# payment_system/core/context.py
import sys

from payment_system.core.enums import PaymentMode
from payment_system.processors.paypal_processor import PayPalProcessor
from payment_system.processors.googlepay_processor import GooglePayProcessor
from payment_system.processors.creditcard_processor import CreditCardProcessor

class PaymentProcessorContext:
    _strategies = {
        PaymentMode.PAYPAL: PayPalProcessor(),
        PaymentMode.GOOGLEPAY: GooglePayProcessor(),
        PaymentMode.CREDITCARD: CreditCardProcessor(),
    }

    @staticmethod
    def checkout(mode: PaymentMode, amount: float):
        strategy = PaymentProcessorContext._strategies.get(mode)

        if strategy:
            try:
                strategy.process_payment(amount)
            except Exception as e:
                print(f"Payment processing failed for {mode.name}: {e}", file=sys.stderr)
        else:
            print(f"Invalid payment mode selected: {mode.name}!")



if __name__ == "__main__":
    amount = 150.75

    print("--- Extensible Payment System (Modular) Example ---")

    PaymentProcessorContext.checkout(PaymentMode.PAYPAL, amount)
    PaymentProcessorContext.checkout(PaymentMode.GOOGLEPAY, amount)
    PaymentProcessorContext.checkout(PaymentMode.CREDITCARD, amount)
    PaymentProcessorContext.checkout(PaymentMode.UNKNOWN, amount)
