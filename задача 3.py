class IceCream:
    def __init__(self,dobavka):
        self.dobavka=dobavka
    def info_about_icecream(self):
        if self.dobavka=='Нет':
            print('Обычное мороженое')
        else:
            print(f'Мороженное {self.dobavka}')

Mor=IceCream('Нет')
Mor.info_about_icecream()
Mor2=IceCream('Черника')
Mor2.info_about_icecream()