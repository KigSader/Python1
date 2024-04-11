# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.
class exersize:
    def __init__(self, dl, sh) -> None:
        self.dl = dl
        self.sh = sh
    def per_():
        return (self.dl + self.sh) * 2
    def pl_():
        return self.dl * self.sh
    
object_1 = exersize(int(input()))

if len(object_1) == 1:
    print(f'{"Квадрат", {object_1.per_}, {object_1.pl_} }')
    
elif len(object_1) == 2:
    print(f'{"Прямоуголник", {object_1.per_}, {object_1.pl_} }')


        