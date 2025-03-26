#什麼是 functools.wraps

# 當你使用裝飾器時，Python 會把原本的函式包在另一個函式（通常叫 wrapper）裡面。

# 這樣會導致：

# @my_decorator
# def greet():
#     """打招呼函式"""
#     print("Hello")

# print(greet.__name__)   # ❌ 輸出：wrapper
# print(greet.__doc__)    # ❌ 輸出：None
# 因為函式被包起來，__name__ 和 __doc__ 都被蓋掉了。

#解決辦法：使用 functools.wraps
#Demo

from functools import wraps

def my_decorator(func):
    @wraps(func) #關鍵!!　保留原本函式資訊
    def wrapper(*args, **kwargs):
        print("執行前")
        result = func(*args, **kwargs)
        print("執行後")

        return result
    return wrapper

@my_decorator
def greet():
    """打招呼函式"""
    print("Hello!")


print(greet.__name__) #greet
print(greet.__doc__)#打招呼函式


#Note
# docstring 能寫在函式內多個地方嗎？	❌ 不行，只能寫在第一行
# 不是第一行的 """ 會怎樣？	會被當作普通字串，沒作用
# 除了函式，還能用在哪？	類別、模組的第一行

#=========================================================

#多層裝飾器（疊加） 你可以在一個函式上套用多個裝飾器：

#Demo
def log(func):
    def wrapper(*args , **kwargs):
        print("開始記錄~~~~")
        return func(*args, **kwargs)
    return wrapper

def auth(func):
    def wrapper(*args , **kwargs):
        print("權限檢查中~~~~")
        return func(*args, **kwargs)
    return wrapper

@auth #最外層先執行
@log  #第二層第二執行
def run_task():  #最內層 最後執行
    print("執行任務")

run_task()


#Note
# functools.wraps(func): 保留原函式的名字與 docstring , @wraps(func)
# 多層裝飾器:同時套用多個功能，@A, @B 疊加，從下往上套用