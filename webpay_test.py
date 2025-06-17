from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.common.options import WebpayOptions
from transbank.common.integration_type import IntegrationType

options = WebpayOptions(
    commerce_code="597055555532",
    api_key="0208F3F6A8D5A3F6A8D5A3F60208F3F6",
    integration_type=IntegrationType.TEST
)
tx = Transaction(options)
try:
    response = tx.create("orden123", "session123", 1000, "https://www.google.com")
    print(response)
except Exception as e:
    print(f"Error: {e}") 