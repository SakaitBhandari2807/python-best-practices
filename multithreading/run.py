from concurrent.futures import ThreadPoolExecutor

def divide_number(a,b):
    return a/b
numbers = [(10,2), (10, 0), (10,5)]

with ThreadPoolExecutor(max_workers=2) as executor:
    futures = [executor.submit(divide_number, x, y) for x,y in numbers]

    for future in futures:
        try:
            result = future.result()
            print(result)
        except ZeroDivisionError:
            print("Tried to divide by zero")

