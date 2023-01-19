# Prob 9.3
def test(f):
    def start_end(*args):
        print('start')
        result = f(*args)
        print(result)
        print('end')
        return result
    return start_end


@test
def multiply(n1, n2):
    return n1 * n2


multiply(2, 4)
