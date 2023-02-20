from operator import itemgetter


def make_index(array, position):
    """

    :param array:
    :param position:
    :return:
    """
    before_array = [(book[position], idx) for idx, book in enumerate(array)]

    sorted_array = sorted(before_array, key=itemgetter(0))
    return sorted_array


def search_book(array, f_data):
    position = -1
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if f_data == array[mid][0]:
            return array[mid][1]
        elif f_data > array[mid][0]:
            start = mid + 1
        else:
            end = mid - 1

    return position


book_array = [
    ["어린왕자", "쌩떽쥐베리"],
    ["이방인", "까뮈"],
    ["부활", "톨스토이"],
    ["신곡", "단테"],
    ["돈키호테", "세르반테스"],
    ["동물농장", "조지오웰"],
    ["데미안", "헤르만헤세"],
    ["파우스트", "괴테"],
    ["대지", "펄벅"],
    ["이것이 자바다", "신용권"],
]
name_index = []
auth_index = []

print("책장의 도서 ==>", book_array)
name_index = make_index(book_array, 0)
print("도서명 색인표 ==>", name_index)
auth_index = make_index(book_array, 1)
print("작가명 색인표 ==>", auth_index)

find_name = "신곡"
find_position = search_book(name_index, find_name)
if find_position != -1:
    print(f"{find_name}의 작가는 {book_array[find_position][1]}입니다.")
else:
    print(f"{find_name} 책은 없습니다.")

find_name = "괴테"
find_position = search_book(auth_index, find_name)
if find_position != -1:
    print(f"{find_name}의 도서는 {book_array[find_position][0]}입니다.")
else:
    print(f"{find_name} 작가는 없습니다.")
