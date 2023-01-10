
class Renter:
    def __init__(self, name, length_of_stay):
        self.name = name
        self.length_of_stay = length_of_stay

    def calculate_cost(self):
        return 119*self.length_of_stay*1.15

class LongTermRenter(Renter):
    def __init__(self, name, length_of_stay, package):
        super().__init__(name, length_of_stay)
        self.package = package

    def calculate_cost(self):
        base_cost = super.calculate_cost()
        if self.package == 1:
            return base_cost*0.70 + 25
        elif self.package == 2:
            return base_cost*0.70 + 75
        else:
            return base_cost*0.70

    def get_info_string(self):
        string = str(self.length_of_stay)+" day stay"
        if self.package == 1:
            string = string + "(Basic)"
        elif self.package == 2:
            string = string + "(Premium)"
        return string

class ShortTermRenter(Renter):
    def __init__(self, name, length_of_stay, breakfast):
        super().__init__(name, length_of_stay)
        self.breakfast = False
        if breakfast == "y":
            self.breakfast = True

    def calculate_cost(self):
        base_cost = super.calculate_cost()
        if self.breakfast:
            return base_cost+5.99*self.length_of_stay

    def get_info_string(self):
        string = str(self.length_of_stay)+" day stay"
        if self.breakfast:
            string = string + "(Breakfast Plan)"
        return string
