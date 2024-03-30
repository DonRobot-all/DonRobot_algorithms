class Weapon:
    def __init__(self, name, material, strength=100) -> None:
        self.name = name
        self.material = material
        self.strength = strength
        print(f'Оружие {name} создано!')
    
    def __str__(self):
        return (
            f'Оружие — «{self.name}». ' 
            f'Создан из материала {self.material}, '
            f'прочность — {self.strength}.'
        )

class Melle(Weapon):
    
    def slashing_blow(self):
        self.strength -= 10
        return (f'Нанесён рубящий удар мечом {self.name}. '
                f'Радиус поражения: {self.blade_length}.')
    

    def piercing_strike(self):
        self.strength -= 5
        return (f'Нанесён пронзающий удар мечом {self.name}. '
                f'Рукоять {self.grip} мягко легла в руку.')

    def sharpen(self):
        self.strength = 100
        return (f'Меч "{self.name}" заточен,'
                f' {self.material} отлично поддалась обработке.') 
    
    def __str__(self):
        print('Это оружие ближнего боя')
        return super().__str__()
    

class Range(Weapon):
    def __init__(self, name, material, range, strength=100) -> None:
        super().__init__(name, material, strength)
        self.range = range


katana = Melle('Верный', 1.5,
               'под хват двумя руками')
print(katana)

bow = Range('Сокол', 'дерево', 150)
print(bow)