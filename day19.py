def dec_to_bin(n):
    if n < 2:
        return n
    else:
        return f"{dec_to_bin(n // 2)}{n%2}"


def dec_to_oct(n):
    if n < 8:
        return n
    else:
        return f"{dec_to_oct(n // 8)}{n%8}"


def dec_to_hex(n):
    rep_chr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    rep_chr += ["a", "b", "c", "d", "e", "f"]
    if 10 <= n < 16:
        return f"{rep_chr[n]}"
    else:
        return f"{dec_to_hex(n//16)}{rep_chr[n%16]}"


print(dec_to_bin(65535))
print()
print(dec_to_oct(65535))
print(dec_to_hex(65535))
