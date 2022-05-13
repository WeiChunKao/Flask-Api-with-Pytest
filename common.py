import json
from flask import request
from typing import Any
from functools import wraps
class Base():
    @staticmethod
    def getheader():
        return {"Content-Type": "application/json",
                'Connection': 'close',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST',
                'Access-Control-Allow-Headers': 'x-requested-with,content-type'
                }

    @staticmethod
    def transferTemplate():
        return {
            "currencies": {
                "TWD": {
                    "TWD": 1,
                    "JPY": 3.669,
                    "USD": 0.03281
                },
                "JPY": {
                    "TWD": 0.26956,
                    "JPY": 1,
                    "USD": 0.00885
                },
                "USD": {
                    "TWD": 30.444,
                    "JPY": 111.801,
                    "USD": 1
                }
            }
        }

def apiLoginProcess(func: Any) -> Any:
    """[summary]
    處理驗證
    Args:
        func ([type]): 方法
    Returns:
        Any: 回傳、狀態碼、Header
    """
    @wraps(func)
    def wrapper(*args: tuple, **kwargs: dict) -> Any:
        print(f"args:{args}")
        print(f"kwargs:{kwargs}")
        print(request.json)
        #return func(*args, **kwargs)
    return wrapper