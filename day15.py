def insert_data(idx, pokemon):
    if idx < 0 or idx > len(pokemons):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    pokemons.append(None)  # 빈칸 추가

    for i in range(len(pokemons) - 1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon  # 지정한 위치에 친구 추가


def delete_data(idx):
    if idx < 0 or idx > len(pokemons):
        print("Out of range!")
        return

    p_count = len(pokemons)
    pokemons[idx] = None

    # for i in range(idx + 1, p_count):
    #     pokemons[i] = None

    for i in range(idx, p_count):
        pokemons.pop()


if __name__ == "__main__":
    pokemons = ["피카츄", "라이츄", "파이리", "꼬부기", "버터플"]

    print(pokemons)
    # insert_data(2, "야도란")
    delete_data(4)
    # # insert_data(6, "피존투")
    print(pokemons)
    delete_data(1)
    print(pokemons)


# pokemons = list()
#
#
# def add_pokemon(pokemon):
#     pokemons.append(None)
#     pokemons[-1] = pokemon
#
#
# add_pokemon("피카츄")
# add_pokemon("라이츄")
# add_pokemon("파이리")
# add_pokemon("꼬부기")
# add_pokemon("버터플")
#
# print(pokemons)
