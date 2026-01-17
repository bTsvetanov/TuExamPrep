import random

while True:
    try:
        n = int(input("Въведете цяло число n (10 < n < 50): "))
        if 10 < n < 50:
            break
        else:
            print("Числото трябва да е в интервала (10, 50).")
    except:
        print("Моля, въведете валидно цяло число.")

a = random.randint(-2500, -1299)
b = random.randint(1111, 4445)
print(f"Интервалът е: ({a}; {b})")

mylst_1 = []
print(f"Въведете {n} цели числа в интервала ({a}; {b}):")
for i in range(n):
    while True:
        try:
            x = int(input(f"Елемент {i}:"))
            if a < x <= b:
                mylst_1.append(x)
                break
            else:
                print(f"Числото трябва да бъде в интервала ({a}; {b}).")
        except:
            print("Моля, въведете валидно цяло число.")

count_neg = 0
for num in mylst_1:
    if num < 0:
        tens_digit = abs(num) // 10 % 10
        if tens_digit % 4 == 0 or tens_digit % 5 == 0:
            count_neg += 1

print(f"Броя отрицателните числа с цифра на десетиците кратна на 4 или 5:{count_neg}")

two_digit_even_count = 0
sum =0 

for x in mylst_1:
    if 10 <= abs(x) <= 99 and x % 2 == 0:
        two_digit_even += 1
        sum += x

if two_digit_even:
    avg = sum / two_digit_even_count

else:
    avg = "Няма такива елементи"

print("Средно аритметично на двуцифрените четни числа:", avg)

mylst_2 = []
for x in mylst_1:
    if 100 <= abs(x) <= 999 and x % 3 == 0:
        mylst_2.append(x)
print("mylst_2:", mylst_2)

count_odd_even_index = 0
for idx, val in mylst_2:
    if idx % 2 == 0 and val % 2 != 0:
        count_odd_even_index += 1

print("Брой нечетни елементи на четни индекси в mylst_2:", count_odd_even_index)


for i in range(len(mylst_2)):
    if mylst_2[i] % 2 != 0:
        mylst_2[i] = 13

print("mylst_2 след замяна:", mylst_2)

if len(mylst_1) != len(mylst_2):
    if len(mylst_1) > len(mylst_2):
        if len(mylst_1) > 1:
            del mylst_1[0]
            del mylst_1[-1]
    else:
        if len(mylst_2) > 1:
            del mylst_2[0]
            del mylst_2[-1]

print("Краен mylst_1:", mylst_1)
print("Краен mylst_2:", mylst_2)
