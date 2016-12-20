# -*- coding: utf-8 -*-
from UniversalAnalytics import Tracker
import functools

CUSTOMER_UNIQUE_ID = "tm8r_test"
TRACKING_CODE = "UA-XXXXXXXX-X"
tracker = Tracker.create(TRACKING_CODE, client_id=CUSTOMER_UNIQUE_ID)
EXD_FORMART = "{0} on {1}"


def before_tracking(hittype, *args, **kwargs):
    def receive_func(func):
        @functools.wraps(func)
        def wrapper(*wargs, **wkwargs):
            tracker.send(hittype, *args, **kwargs)
            print(hittype, args, kwargs)
            return func(*wargs, **wkwargs)

        return wrapper

    return receive_func


def after_tracking(hittype, *args, **kwargs):
    def receive_func(func):
        @functools.wraps(func)
        def wrapper(*wargs, **wkwargs):
            try:
                result = func(*wargs, **wkwargs)
                print("normal", hittype)
                tracker.send(hittype, *args, **kwargs)
                return result
            except Exception as e:
                exd = EXD_FORMART.format(e.message, func.__name__)
                print("exception", hittype, exd)
                tracker.send("exception", {'exd': exd}, *args, **kwargs)
                raise e
                return

        return wrapper

    return receive_func


def send(hittype, *args, **kwargs):
    tracker.send(hittype, *args, **kwargs)
