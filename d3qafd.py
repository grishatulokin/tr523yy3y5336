def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def main():
    try:
        user_input = input("Введите числа через пробел: ")
        numbers = [int(x) for x in user_input.split()]
        even_numbers = filter_even_numbers(numbers)
        if even_numbers:
            print(f"Четные числа: {even_numbers}")
        else:
            print("Четных чисел нет.")
    except ValueError:
        print("Ошибка! Введите только числа.")

if __name__ == "__main__":
    main()