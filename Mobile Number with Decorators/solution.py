def wrapper(f):
    # I implemented only this funcion
    def fun(l):
        numbers_list = []
        for num in l:
            numbers_list.append(f'+91 {num[-10:-5]} {num[-5::]}')
        f(numbers_list)
    return fun

# given by the problem
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

# also given by the problem
if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 