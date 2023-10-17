from abc import ABC, abstractmethod

class PaymentMethodProvider(ABC):
    @abstractmethod
    def pay(self, total:float):
        pass
