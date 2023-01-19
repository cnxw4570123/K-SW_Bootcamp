def sub_int(x, y):
    return x - y


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


print(sub_int(7, 3))
info_sub_int = document_info(sub_int)
info_sub_int(7, 3)
