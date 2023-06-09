# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

def get_set(x):
    temp_set = set()
    for i in range(x):
        num = int(input('Введите числа для множества: '))
        temp_set.add(num)
    return temp_set

a = get_set(int(input('Введите число n: ')))
print(a)
b = get_set(int(input('Введите число m: ')))
print(b)
c = a.intersection(b)
print(c)

# Для того что бы не нагромождать два цикла for, создаем функцию, результат работы которой будет
# множеств temp_set.
# Даем название функции, передаем в нее переменную - она будет динамичная. В нашем случае - это х.
# Создаем пустой temp_set, который будет заполняться элементам, после возвращаться функцией и передаваться в нужные
# нам переменные - в нашем случае, это a и b.