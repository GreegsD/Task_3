import random
print("Вітаємо у грі! Правила прості: спробуйте відгадати число.")
a = random.randint(1, 100)
b = 0
while True:
    c = int(input("Введіть свій варіант числа: "))
    b += 1
    if c == a:
        print(f"Вітаємо, ви вгадали! Загадане число: {a}")
        print(f"Кількість спроб: {b}")
        break
    elif c < a:
        print("Більше!")
    else:
        print("Менше!")
print("Гра завершена. Дякуємо за участь!")
