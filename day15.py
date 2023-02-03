def add_friends(friends_list, *friend_instance):
    # print(friend)
    for idx in range(len(friends_list)):  # 0번 idx부터 f_list 길이만큼 반복
        if friend_instance[1] >= friends_list[idx][1]:  # 해당 idx의 연락량이랑 추가되는 연락량 비교
            friends_list.insert(idx, friend_instance)
            break
    else:
        friends_list.append(friend_instance)


friends = [("다현", 200), ("정연", 150), ("쯔위", 90), ("사나", 40), ("지효", 15)]

while True:
    friend = input("추가할 친구 입력 > ")
    if friend == "0":
        break
    else:
        count = input("연락 횟수 : ")
        add_friends(friends, friend, int(count))
    print(friends)
