from abc import ABC, abstractmethod

class MenuComponent(ABC):
    @abstractmethod
    def add(self, component):
        pass

    @abstractmethod
    def remove(self, component):
        pass

    @abstractmethod
    def display(self):
        pass

class MenuItem(MenuComponent):
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def add(self, component):
        print("Cannot add to a MenuItem.")

    def remove(self, component):
        print("Cannot remove from a MenuItem.")

    def display(self):
        print(f"{self.name} - {self.description}, {self.price} €")

class Menu(MenuComponent):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.menu_components = []

    def add(self, component):
        self.menu_components.append(component)

    def remove(self, component):
        if component in self.menu_components:
            self.menu_components.remove(component)

    def display(self):
        print(f"\n{self.name}: {self.description}\n")
        for component in self.menu_components:
            component.display()

if __name__ == "__main__":
    burgeris = MenuItem("Burgeris", "Mėsingas mėsainis su sūriu ir daržovėmis", 9.99)
    bulvės = MenuItem("Bulvės", "Traškios aukso spalvos bulvytės", 3.99)
    gazuotas_gėrimas = MenuItem("Gazuotas gėrimas", "Atgaivinantis gazuotas gėrimas", 1.99)

    derinio_menu = Menu("Derinio meniu", "Skaniu deriniu su nuolaida")
    derinio_menu.add(burgeris)
    derinio_menu.add(bulvės)
    derinio_menu.add(gazuotas_gėrimas)

    vegetarinių_patiekalų_menu = Menu("Vegetarinių patiekalų meniu", "Sveiki ir skanūs vegetarinių patiekalų pasirinkimai")
    vegetarinių_patiekalų_menu.add(MenuItem("Salotos", "Šviežios daržovės su padažu", 7.99))
    vegetarinių_patiekalų_menu.add(MenuItem("Vegetariškas suktinukas", "Įvairios daržovės suvyniotos į tortiliją", 6.99))

    pagrindinis_menu = Menu("Pagrindinis meniu", "Sveiki atvykę į mūsų restoraną!")
    pagrindinis_menu.add(derinio_menu)
    pagrindinis_menu.add(vegetarinių_patiekalų_menu)

    pagrindinis_menu.display()
