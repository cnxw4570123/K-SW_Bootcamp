def sort_by_hp(pks_list, pk_info):
    for idx in range(len(pks_list)):
        if pks_list[idx][1] < pk_info[1]:  # 크면 앞쪽에 삽입
            pks_list.insert(idx, pk_info)
            break
        elif pks_list[idx][1] == pk_info[1]:  # hp 값이 같으면 이름 비교
            if pks_list[idx][0] >= pk_info[0]:  # 이름이 크면
                pks_list.insert(idx, pk_info)  # 앞쪽에 저장
            else:  # 그렇지 않으면 뒤쪽에 저장
                pks_list.insert(idx + 1, pk_info)
            break
    else:
        pks_list.append(pk_info)
    print(pks_list)


if __name__ == "__main__":
    pokemons = [["라이츄", 200], ["피카츄", 100], ["파이리", 80], ["야도란", 50], ["잉어킹", 10]]

    print(pokemons)
    while True:
        pokemon = input("추가할 포켓몬 : ")
        if pokemon == "1":
            break
        hp = int(input("체력 : "))
        sort_by_hp(pokemons, [pokemon, hp])
