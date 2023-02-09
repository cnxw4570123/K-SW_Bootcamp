import tkinter as tk

memos = [None for _ in range(100)]  # 전역 리스트ㅡ
memos[0], memos[1] = 0, 1


def fact_recu(n):
    if n == 1:
        return 1
    else:
        return n * fact_recu(n - 1)


def fibo_memo_recu(n):
    if n <= 1:
        return memos[n]

    if memos[n] is not None:  # 전역 메모리 memos에 이전에 계산한 결과 값이 존재하면
        return memos[n]

    memos[n] = fibo_memo_recu(n - 2) + fibo_memo_recu(n - 1)  # 처음 방문하는 n이면
    return memos[n]


def fact_input():
    lbl_result.config(text=f"팩토리얼 계산결과: {fact_recu(int(en_num_input.get()))}")


def fibo_input():
    lbl_result.config(text=f"피보나치 계산결과: {fibo_memo_recu(int(en_num_input.get()))}")


win = tk.Tk()
win.title("Calculator")
win.geometry("300x150")

en_num_input = tk.Entry()  # 텍스트 입력상자
lbl_result = tk.Label(text="계산결과")
btn_fact = tk.Button(text="팩토리얼", command=fact_input)
btn_fibo = tk.Button(text="피보나치", command=fibo_input)

en_num_input.pack()
lbl_result.pack()
btn_fact.pack(fill="x")
btn_fibo.pack(fill="x")
win.mainloop()
