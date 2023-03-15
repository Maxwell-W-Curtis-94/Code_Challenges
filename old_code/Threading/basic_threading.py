import logging
import threading
import time


# https://realpython.com/intro-to-python-threading/
# q27cwuisihonb8807n5typ api key 
def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    # daemon threads end when the main thread ends, regardless if the daemon was still running
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    x.join()
    # join will what for all threads before continuing
    logging.info("Main    : all done")
