#什麼是裝飾器（Decorator）?
#裝飾器是一種可以「在不改變原本函式的情況下，額外加上功能」的語法工具。
# 你可以把它想成「幫函式加上濾鏡或特效」。

#為什麼要用裝飾器？
# 不用修改原本的函式

# 可以抽出重複功能（如登入檢查、log 紀錄）

# 常被用在：Flask、FastAPI、Django、pytest 等框架中

# 你可以把「裝飾器」想像成：

# 🔧「一個可以改造函式的加工廠」
# 你把原本的函式放進去，它幫你包裝好新的行為再交回來。


#Demo
#先寫一個函式
def say_hello():
    print("Hello!")

#然後幫他寫一個裝飾器
def my_decorator(func):
    def wrapper():
        print("執行前的事情")
        func() #執行原本的函示
        print("執行後的事情")

    return wrapper #回傳函式本體，不加括號！

## 把裝飾器包在函式外（等同於 @my_decorator）
say_hello = my_decorator(say_hello)
# ▶️ 呼叫被裝飾過的函式
say_hello()

#也可以用簡化寫法
@my_decorator
def say_hi():
    print("Hi there!")

say_hi()

#Note:
# 函式中定義函式	在 Python 中合法，稱為「巢狀函式」
# 為什麼這樣寫？	讓你可以做封裝、延遲執行、產生閉包（closure）
# return wrapper	回傳函式本體給外層使用
# return wrapper()	會立刻執行 wrapper，只傳回執行結果，不再是裝飾器了 ❌


#pra
def log_decorator(func):
    def show_log():
        print("[LOG] 開始執行 greet")
        func()
        print("[LOG] 執行結束 greet")
    return show_log

@log_decorator
def greet():
    print("Hi! I'm Mantle.")

greet()
