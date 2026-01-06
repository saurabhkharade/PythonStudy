class Father:
    def show_father(self):
        print("This is Father")
class Mother():
    def show_mother(self):
        print("This is Mother")
class Son(Father,Mother):
    def show_son(self):
        print("This is Son")

son = Son()
son.show_father()
son.show_mother()
son.show_son()
