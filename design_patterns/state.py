from abc import ABC, abstractmethod


class Order:
    def __init__(self):
        self.state = PaymentPending(self)

    def pending(self):
        self.state.pending()

    def approve(self):
        self.state.approve()

    def reject(self):
        self.state.reject()


class OrderState(ABC):
    def __init__(self, order):
        self.order = order

    @abstractmethod
    def pending(self):
        pass

    @abstractmethod
    def approve(self):
        pass

    @abstractmethod
    def reject(self):
        pass


class PaymentPending(OrderState):
    def __init__(self, order):
        self.order = order

    def pending(self):
        print("Payment pending...")

    def approve(self):
        self.order.state = PaymentApprove(self.order)
        print("Payment in approved!")

    def reject(self):
        self.order.state = PaymentReject(self.order)
        print("Payment reject!")


class PaymentApprove(OrderState):
    def __init__(self, order):
        self.order = order

    def pending(self):
        self.order.state = PaymentPending(self.order)
        print("Payment pending")

    def approve(self):
        print("Payment approved")

    def reject(self):
        self.order.state = PaymentReject(self.order)
        print("Payment reject")


class PaymentReject(OrderState):
    def __init__(self, order):
        self.order = order

    def pending(self):
        print("Payment reject")

    def approve(self):
        print("Payment reject")

    def reject(self):
        print("Payment reject")


if __name__ == "__main__":
    order = Order()
    order.pending()
