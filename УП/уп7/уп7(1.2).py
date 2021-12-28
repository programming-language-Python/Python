func = (lambda x, y=100, *args: str(x**y) + args[len(args)-1]
        )(15, 50, 'test', 'test1', 'test2')
print(func)
