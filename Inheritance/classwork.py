class Cats():
    lapki = 4  #параметр класса, птм неизменяемый

    def __init__(self, name, color):  #  init - конструкто, свойства экзепляра
        self.name = name  # устанавливаем параметры экземпляра self - свойство, указатель на текущий обьект класса
        self.color = color

    def dream(self, duration): #метод
        print("Я много сплю")


Luca = Cats("Люся", "белая") # экзепляр, указываем все параметры, которые есть
Luca.dream(4)