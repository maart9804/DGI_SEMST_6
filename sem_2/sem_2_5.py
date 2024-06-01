a = 1
def func1():
    b = 2
    def func2():
        c = 3
        print(a)
        print(b)
        print(c)
    func2()
func1()