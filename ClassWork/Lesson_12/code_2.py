def benchmark(iters):
    def decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start_time = time.time()
                return_value = func(*args, **kwargs)
                end_time = time.time()
                total = total + (end_time - start_time)

            print("The avarage of exec:", total/iters)
            return return_value
        return wrapper
    return decorator

@benchmark(iters = 10)
def fetch_webpage(url):
    a = "URL: " + url
    return a

webpage = fetch_webpage('https://google.com')
print(webpage)

# def connection(ip: str, port: int):
#     def make_connection(printer_function):
#         def wrapper(model: str, color: str):
#             print('*' * 10)
#             print("Connection on IP", ip)
#             print("Connection on PORT", port)
#             print(model, 'Connection')
#             printer_function(model, color)
#             print('*' * 10)
#         return wrapper
#     return make_connection

# @connection('192.168.10.2', 5432)
# def hp_printer(model: str, color: str):
#     print('Model:', model)
#     print('Color:', color)

# @connection('192.168.9.1', 4321)
# def samsung_printer(model: str, color: str):
#     print('Model:', model)
#     print('Color:', color)

# if __name__ == "__main__":
#     # ! printer_models = ['hp', 'samsung']
#     hp = hp_printer
#     hp('HP', 'red')
#     print('-'*20)
#     sm = samsung_printer
#     sm('SAMSUNG', 'black')
    
