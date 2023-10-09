class DataBase:
    pf = 1
    title = "классы и объекты"
    author = "Сергей Балакирев"
    views = 14356
    comments = 12


a = DataBase()
setattr(a, 'title', 'новый аргумент экземпляра класса')
hasattr(a, 'title')
print(hasattr(a, 'title'))
print(a.title)


class Goods:
    title = "Ice Cream"
    weight = 154
    tp = "Food"
    price = 1024


setattr(Goods, 'price', 2048)
setattr(Goods, 'infiltration', 100)

print(Goods.__dict__)


class Car:
    model = "Audi"
    color = "Black"
    number = "12345"


col = Car()
col.color = "Black"
print(col.__dict__)


class Notes:
    uid = 1005435
    title = "Joke"
    author = "John"
    pages = 2


print(getattr(Notes, 'author'))


class Dictionary:
    rus = "ПАйтон"
    eng = "Python"


a = getattr(Dictionary, 'rus_word', False)
print(a)


class TravelBlog:
    total_blogs = 0


tb1 = TravelBlog()
tb1.name = "Франция"
setattr(tb1, 'days', 6)
setattr(TravelBlog(), 'total_blogs', 1)

tb2 = TravelBlog()
tb2.name = "Италия"
setattr(tb2, 'days', 5)
setattr(TravelBlog(), 'total_blogs', 2)

print(tb1.__dict__)


class Figure:
    type_fig = 'circle'
    color = 'red'


fig = Figure()
fig.start_pt = (10, 5)
fig.end_pt = (100, 20)
fig.color = 'black'

del fig.color

print(fig.__getattribute__('start_pt'), fig.__getattribute__('end_pt'))


class Person:
    name = "John"
    job = "Programmer"
    city = "New York"

p1 = Person()

print(hasattr(p1, 'job'))
