import datetime
import time
import random
class Воины:
    жизни=1000
    атака=50
# игрок1 - Воин Света
# игрок2 - Воин Тьмы
игрок1=Воины() # экземпляр класса Воины()
игрок2=Воины() # экземпляр класса Воины()
while True:
    d=datetime.datetime.today()
    s=d.second
    #print('секунды',s)
    h=d.hour
    #print('часы',h)
    # Переход от одного игрока к другому осуществляется случайным образом.
    input('Нажмите Enter для перехода следущего игрока')
    arr=[1,2]
    rand=random.choices(arr)
    #print(rand)
    # В зависимости от времени суток каждый игрок владеет волшебным мечом, дающим силу удара +150. 
    if 6<=h<=18:
        игрок1.атака=200
        if игрок2.атака==200:
            игрок2.атака=50
    elif h>=19 or h<=5:
        игрок2.атака=200
        if игрок1.атака==200:
            игрок1.атака=50
    # В зависимости от того, какая сейчас секунда, войны наносят друг-другу удары: четная - ход Светлого, нечетная - ход Темного. 
    if rand==[1] and s%2==0:
        игрок2.жизни-=игрок1.атака
        time.sleep(3) # через какое время продолжит выполнять код
        print('Воин Света атаковал, у Воина Тьмы осталось',игрок2.жизни,'здоровья.')
        print(игрок1.атака)
    elif rand==[2] and s%2!=0:
        игрок1.жизни-=игрок2.атака
        time.sleep(3)
        print('Воин Тьмы атаковал, у  Воина Света осталось',игрок1.жизни,'здоровья.')
        print(игрок2.атака)
    if игрок1.жизни<=0:
        print('Воин Тьмы выиграл!!!')
        break
    elif игрок2.жизни<=0:
        print('Воин Света выиграл!!!')
        break