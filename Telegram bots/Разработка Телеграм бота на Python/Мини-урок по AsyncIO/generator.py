import asyncio
from contextvars import ContextVar

# # * создали объект контекстной переменной

# * это генератор


# def generator(a, b,):
#     # * приостанавливает выполнение функции
#     while True:
#         yield a * b
#         a += 1


# # g = generator(2, 2)
# # print(next(g))
# # * если ещё раз вызвать то a увеличится на 1
# # print(next(g))


# async def async_function(a):
#     while True:
#         await a
#         a += 1
# # * async_function - это обычная функция,
# # * а если её вызвать async_function(1) то это уже coroutine.
# # * coroutine похожа на генераторы
# # print(async_function)
# # print(async_function(1))
# # * в асинхроннй функции можно выполнять синхронный и ансинхронный код,
# # * в синхронных функциях можно выполнять только синхронный код
# asyncio.sleep(1)  # * 1 секунду выполняются другие задачи


# async def count(counter):
#     print(f'Количестов записей в списке: {len(counter)}')

#     while True:
#         await asyncio.sleep(1 / 1000)
#         counter.append(1)


# async def print_every_one_sec(counter):
#     while True:
#         await asyncio.sleep(1)
#         print(f'- 1 секунда прошла. '
#               f'Количество записей в списке: {len(counter)}')


# async def print_every_5_sec():
#     while True:
#         await asyncio.sleep(5)
#         print(f'---- 5 секунд прошло.')


# async def print_every_10_sec():
#     while True:
#         await asyncio.sleep(10)
#         print(f'---------- 10 секунд прошло.')


# async def main():
#     counter = list()
#     # c = count(counter)
#     # p1 = print_every_one_sec(counter)
#     # p5 = print_every_5_sec()
#     # p10 = print_every_10_sec()

#     # # * создали задачу. Запланировали
#     # asyncio.create_task(c)
#     # asyncio.create_task(p1)
#     # asyncio.create_task(p5)
#     # asyncio.create_task(p10)
#     # await p10

#     # * ИЛИ
#     # * Все 4 coroutine выполняются конкурентно
#     tasks = [
#         count(counter),
#         print_every_one_sec(counter),
#         print_every_5_sec(),
#         print_every_10_sec()
#     ]
#     # * блокирует coroutine main() пока не дождётся
#     # * ответа результата выполнения функций
#     await asyncio.gather(*tasks)
# # * запускает coroutine
# asyncio.run(main())

# * ContextVar() - 1 аргумент название переменной,
# * 2 аргумент значение по умолчанию
MyCounter = ContextVar('counter', default=0)


async def increase():
    # * забираем контекстную переменную
    my_counter = MyCounter.get()

    my_counter += 1
    # * обновляем значение переменной
    MyCounter.set(my_counter)


async def count():
    while True:
        await increase()
        my_counter = MyCounter.get()
        print(f'Счетчик: {my_counter}')

        await asyncio.sleep(1 / 10)

asyncio.run(count())
