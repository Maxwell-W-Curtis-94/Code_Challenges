import threading
import time
from pprint import pprint


# blocking network
def network_request(number):
    time.sleep(1)
    return {"success": True, 'result': number ** 2}


def fetch_square(number):
    response = network_request(number=number)
    if response['success']:
        print("Result is: {}".format(response['result']))


# non blocking
def network_request_async(number, on_done):
    def callback():
        on_done(
            {"success": True, 'result': number ** 2}
        )

    timer = threading.Timer(1, callback)
    timer.start()


def fetch_square_async(number):
    def on_done(response):
        if response['success']:
            print("Result is: {}".format(response['result']))

    network_request_async(number=number, on_done=on_done)


# callback
def wait_and_print(msg):  # blocking
    time.sleep(1)
    print(msg)


def wait_and_print_async(msg):  # non blocking
    def callback():
        print(msg)

    timer = threading.Timer(1.0, callback)
    timer.start()


def driver():
    numb = [
        2, 3, 4, 5
    ]
    for i in numb:
        fetch_square_async(i)


if __name__ == '__main__':
    driver()
