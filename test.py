import asyncio

def run_concurrent_burgers():
    # Осуществляется управление этими очередями
    menu = asyncio.Queue()
    routin = asyncio.Queue()


    # Выполняем все задачи с использованием стандартного цикла событий asyncio
    print('Мы в run_cuncurrent')
    asyncio.gather(show_menu(),do_something())
# Объявляем задачи asyncio с использованием конструкции async def
async def show_menu():
    print('мы в шоу меню')
    while True:
        print('1 - start')
        print('2 - stop')
        ans=input()
        if ans == '1':
            await do_something()
        else:
            pass
async def do_something():
    while True:
        print('!')
        await asyncio.sleep(1)
run_concurrent_burgers()
