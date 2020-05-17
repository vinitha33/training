def eval_loop():
    while True:
        a = input()
        if a != "done":
            s = eval(a)
            print(s)
        else:
            print(s)

print(eval_loop())
