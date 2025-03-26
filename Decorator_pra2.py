#裝飾器支援「帶參數的函式」與「多層裝飾器結構」

#1. 讓裝飾器可以裝「有參數的函式」Demo

def my_decorator(func):
    def wrapper(*arg, **kwargs):  #為什麼*arg, **kwargs要加在這裡? 因為再來執行的不會是greet()他只是裡面的內容物 要執行的是外面的包裝物
        print("執行前")
        func(*arg, **kwargs)
        print("執行後")
    return wrapper

def logger_dec(func):
    def show_log(*args, **kwargs):
        print("[LOG] 發動前")
        func(*args, **kwargs)
        print("[LOG] 發動後")
    return show_log

@my_decorator
def greet(name):
    print(f"Hello! {name}")

greet("Mantle")


@logger_dec
def start_engin(car):
    print(f"{car}發動囉")

start_engin("Tesla")


# Note
# *args	接收所有位置參數	1, 2, 3 → (1, 2, 3)	tuple
# **kwargs	接收所有命名參數	x=10, y=20 → {'x': 10, 'y': 20}	dict
# func(*args, **kwargs)	把參數原封不動還給函式	必備技巧


#==================================================================
#客製化寫法 ex@裝飾器(參數) 裝飾器本身帶參數

def log_decorator(level): #第1層: 裝飾器接收參數
    def decorator(func): #第2層:裝飾器包住原函式 傳入
        def wrapper(*args , **kwargs): #地3層: 實際執行+包裝
            print(f"[{level}] 呼叫 {func.__name__}")
            result = func(*args , **kwargs)
            print(f"[{level}] 結束 {func.__name__}")

            return result
        return wrapper
    return decorator

@log_decorator(level = "INFO")
def start_engin_version2(car):
    print(f"{car}發動了")


start_engin_version2("Toyota")

#note 裝飾器參數運作順序
# 1 @log_decorator(level="INFO")	呼叫「外層函式」，傳入參數
# 2 回傳一個裝飾器函式 decorator(func)	包住被裝飾的函式
# 3 呼叫 wrapper() 時才真的執行	加上你要的「特效行為」

#小結筆記
# 第1層	接收裝飾器的參數（如 level="DEBUG"）
# 第2層	接收被裝飾的原始函式
# 第3層	包裝邏輯、加上前後處理，並執行函式
