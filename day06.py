# decorator
def document_info(f):
    def new_func(*args, **kwargs):
        print('실행중인 함수: ', f.__name__)
        print('위치 기반 인수들 : ', args)
        print('키워드 기반 인수들: ', kwargs)
        result = f(*args, **kwargs)
        print("실행 결과:", result)
        return result
    return new_func


@document_info  # decorator annotation 적용
def sub_int(x, y):
    return x - y


@document_info
def squares(x, y):
    return x**y


print(sub_int(7, 3), end="\n\n")
print(squares(5, 2))
