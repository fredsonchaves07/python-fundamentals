from threading import Lock, Thread
from time import sleep


# Option 1
class MyThread(Thread):
    def __init__(self, text, time):
        self.text = text
        self.time = time
        super().__init__()

    def run(self):
        sleep(self.time)
        print(self.text)


th1 = MyThread("Thread 1", 5)
th1.start()

th2 = MyThread("Thread 2", 3)
th2.start()

th2 = MyThread("Thread 3", 1)
th2.start()

for i in range(20):
    print(i)
    sleep(1)


# Option 2
def slow(text, time):
    sleep(time)
    print(text)


th = Thread(target=slow, args=("Hello Word!", 5))
th.start()

for i in range(10):
    print(i)
    sleep(0.5)


# Problemas ao utilizar Threads (Falta de sincronismo)
class TicketPass:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def buy(self, quant):
        self.lock.acquire()

        if self.estoque < quant:
            print("Não tem ingressos")
            self.lock.release()
            return

        sleep(1)

        print(f"Você comprou {quant} ingressos")
        self.estoque -= quant
        print(f"Ainda tem {self.estoque} ingressos")

        self.lock.release()


if __name__ == "__main__":
    ticket = TicketPass(10)

    for i in range(1, 20):
        th = Thread(target=ticket.buy, args=(i,))
        th.start()
