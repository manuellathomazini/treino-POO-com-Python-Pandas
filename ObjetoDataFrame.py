import pandas as pd

class Car:
    def __init__(self, brand, model, color, type, city, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.type = type
        self.city = city
        self.year = year
    def chars(self):
        return {
            "brand": self.brand,
            "model": self.model,
            "color": self.color,
            "type": self.type,
            "city": self.city,
            "year": self.year
        }

cars = []
for i in range(1, 4, 1):
    car = Car(
        input(f"Car{i}- brand: "),
        input(f"Car{i}- model: "),
        input(f"Car{i}- color: "),
        input(f"Car{i}- type: "),
        input(f"Car{i}- city: "),
        int(input(f"Car{i}- year: "))
    )
    cars.append(car.chars())
    print('------------------')

df = pd.DataFrame(cars)
print(df)

#################################################

def classificar(y):
    estado = lambda x: "novo" if x > 2022 else ("seminovo" if x > 2020 else ("usado"))
    return estado(y)

df["status"] = df['year'].apply(classificar)
print(df)