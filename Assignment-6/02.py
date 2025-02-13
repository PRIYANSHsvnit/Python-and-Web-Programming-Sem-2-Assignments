#Unit Converter

class Converter:
    unit = {
        'inch': 0.0254,
        'feet': 0.3048,
        'yard': 0.9144,
        'mile': 1609.34,
        'kilometer': 1000,
        'meter': 1,
        'centimeter': 0.01,
        'millimeter': 0.001
    }

    def __init__(self, num, unit):
        self.leninmeter = num * self.unit[unit]

    def inch(self):
        return self.leninmeter / self.unit['inch']

    def feet(self):
        return self.leninmeter / self.unit['feet']

    def yard(self):
        return self.leninmeter / self.unit['yard']

    def mile(self):
        return self.leninmeter / self.unit['mile']

    def kilometer(self):
        return self.leninmeter / self.unit['kilometer']

    def meter(self):
        return self.leninmeter / self.unit['meter']

    def centimeter(self):
        return self.leninmeter / self.unit['centimeter']

    def millimeter(self):
        return self.leninmeter / self.unit['millimeter']

a = float(input("Enter Number = \n"))
b = input("Enter Unit of Entered Number = \n").strip().lower()

obj = Converter(a,b)

d = input("Enter Unit in which you want output = \n").strip().lower()

match d:
    case 'inch':
        print(f"Output = {obj.inch()}\n")

    case 'feet':
        print(f"Output = {obj.feet()}\n")

    case 'yard':
        print(f"Output = {obj.yard()}\n")

    case 'mile':
        print(f"Output = {obj.mile()}\n")

    case 'kilometer':
        print(f"Output = {obj.kilometer()}\n")

    case 'meter':
        print(f"Output = {obj.meter()}\n")

    case 'centimeter':
        print(f"Output = {obj.centimeter()}\n")

    case 'millimeter':
        print(f"Output = {obj.millimeter()}\n")

    case _:
        print("Please Enter Correct Unit \n")