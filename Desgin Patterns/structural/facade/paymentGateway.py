"""When integrating with multiple payment gateways in an e-commerce system, you can use a Payment Gateway Facade to
provide a unified interface for processing payments. The facade abstracts away the differences between various
payment gateways and provides a consistent set of methods that clients can use to initiate payments,
handle responses, and retrieve transaction information. """


class PaymentGatewayFacade:
    def __init__(self, gateway):
        self.gateway = gateway

    def initiate_payment(self, amount):
        self.gateway.connect()
        self.gateway.authenticate()
        transaction_id = self.gateway.process_payment(amount)
        self.gateway.disconnect()
        return transaction_id

    def get_transaction_status(self, transaction_id):
        self.gateway.connect()
        status = self.gateway.check_status(transaction_id)
        self.gateway.disconnect()
        return status


# Usage
class PayPalGateway:
    def connect(self):
        print("Connecting to PayPal")

    def authenticate(self):
        print("Authenticating with PayPal")

    def process_payment(self, amount):
        print(f"Processing payment of {amount} via PayPal")
        return "PAYPAL-12345"

    def check_status(self, transaction_id):
        print(f"Checking transaction status with PayPal for ID: {transaction_id}")
        return "SUCCESS"


facade = PaymentGatewayFacade(PayPalGateway())
transaction_id = facade.initiate_payment(100)
status = facade.get_transaction_status(transaction_id)
print("Transaction Status:", status)

"""In this example, the PaymentGatewayFacade provides methods (initiate_payment() and get_transaction_status()) to 
initiate a payment and retrieve the transaction status, respectively. The facade interacts with the underlying 
payment gateway (PayPalGateway in this case) to perform the necessary operations. """
