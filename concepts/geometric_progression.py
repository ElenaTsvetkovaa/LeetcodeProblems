import math

def show_geometric_progression(base, max_value):
    print(f"\n📈 Геометрична прогресия с основа {base} до стойност {max_value}:")
    value = 1
    step = 0
    while value <= max_value:
        print(f"Стъпка {step}: {base}^{step} = {value}")
        value *= base
        step += 1

def show_logarithm(base, number):
    result = math.log(number, base)
    print(f"\n🧮 log_{base}({number}) = {result:.2f}")
    print(f"➡️ Това означава: {base}^{result:.2f} ≈ {number}")

# Настройки
base = 2
max_value = 64
number = 32

# Показване
show_geometric_progression(base, max_value)
show_logarithm(base, number)
