def foo():
    print('foo')


foo()  # foo


async def bar():
    print('bar')


ret = bar()
ret.send(None)  # print bar and StopIteration


class Foo:
    def __await__(self):
        yield 42


async def bar2():
    await Foo()


ret2 = bar2()
print(ret2.send(None))
print(ret2.send(None))  # StopIteration

