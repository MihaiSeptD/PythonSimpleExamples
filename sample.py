def generate_list(number: int) -> list:
    arr = []
    for i in range(1, number + 1):
        arr.append(i * 2)
    return arr


def multiply(vec: list) -> float:
    prod = 1
    for el in vec:
        prod = prod * el * 2
    return prod
    
    
if __name__ == '__main__':
    n = input("insert value ")
    n = int(n)

    if n < 0:
        print("n must be positive")
        exit(1)

    generated = generate_list(n)
    
    print("product = " + str(multiply(generated)))
    