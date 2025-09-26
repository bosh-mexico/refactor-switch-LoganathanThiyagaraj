# payment_system/tests/test_payment_system.py
import pytest
import sys

# Import from the new module structure
from payment_system.core.enums import PaymentMode
from payment_system.core.Paymeny_processor import PaymentProcessorContext

@pytest.mark.parametrize(
    "mode, amount, expected_stdout, expected_stderr",
    [
        (PaymentMode.PAYPAL, 10.50, "Processing PayPal payment of $10.50 via PayPal API...\n", ""),
        (PaymentMode.GOOGLEPAY, 200.00, "Processing GooglePay payment of $200.00 via GooglePay API...\n", ""),
        (PaymentMode.CREDITCARD, 0.00, "Processing Credit Card payment of $0.00 via Credit Card Gateway...\n", ""),
        (PaymentMode.PAYPAL, 1234567.89, "Processing PayPal payment of $1234567.89 via PayPal API...\n", ""),
        (PaymentMode.UNKNOWN, 50.00, "Invalid payment mode selected: UNKNOWN!\n", ""),
    ]
)
def test_checkout_various_scenarios_modular(capsys, mode, amount, expected_stdout, expected_stderr):
    """
    Tests various payment modes and amounts using a single parametrized test
    for the modularized payment system.
    """
    PaymentProcessorContext.checkout(mode, amount)
    captured = capsys.readouterr()
    assert captured.out == expected_stdout
    assert captured.err == expected_stderr
