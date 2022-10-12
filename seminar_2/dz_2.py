# Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z

print("x | y | z | ¬(X ∧ Y) v Z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = not (x and y) or z
            print(f"{x} | {y} | {z} |      {int(F)}")
