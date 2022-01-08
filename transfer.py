from typing import Tuple
from common import Base
import sys
import traceback


class Transfer:
    def transferSouceToTarget(self, source: str, target: str, amount: int) -> Tuple[dict, int, dict]:
        try:
            jsonTemplate = Base.transferTemplate()
            currencies = jsonTemplate["currencies"]
            sourceCurrencies = currencies[source]
            targetCurrencies = sourceCurrencies[target]
            transferAmount = f"{amount * targetCurrencies:,.2f}"
            return {'Result': transferAmount, 'Reason': ''}, 200, Base.getheader()
        except Exception as e:
            error_class = e.__class__.__name__  # 取得錯誤類型
            detail = e.args[0]  # 取得詳細內容
            cl, exc, tb = sys.exc_info()  # 取得Call Stack
            lastCallStack = traceback.extract_tb(tb)[-1]  # 取得Call Stack的最後一筆資料
            fileName = lastCallStack[0]  # 取得發生的檔案名稱
            lineNum = lastCallStack[1]  # 取得發生的行號
            funcName = lastCallStack[2]  # 取得發生的函數名稱
            return {'Result': 'NG', 'Reason': f'{funcName} erro'}, 400, Base.getheader()
