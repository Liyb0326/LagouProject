import logging


def use_logging(func):
    def wrapper():
        logging.warning("%s is running" % func.__name__)
        return func()

    return wrapperht5q


@use_logging
def foo():
    print("i am foo")


foo()
