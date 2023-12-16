def generate_list(number: int) -> list:
    arr = []
    for i in range(1, number + 1):
        arr.append(i * 2)
    return arr


def multiply(vec: list) -> float:
    prod = 1
    for el in vec:
        prod = prod * el
    return prod
    
    
if __name__ == '__main__':
    n = input("insert value ")
    n = int(n)
    generated = generate_list(n)
    
    print("product = " + str(multiply(generated)))
    