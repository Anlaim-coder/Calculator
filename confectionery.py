def print_pack_report(count_of_cake):
    if count_of_cake % 3 == 0 and count_of_cake % 5 == 0:
        print(f"{count_of_cake} - расфасуем по 3 или по 5")
    elif count_of_cake % 3 == 0:
        print(f"{count_of_cake} - расфасуем по 3")
    elif count_of_cake % 5 == 0:
        print(f"{count_of_cake} - расфасуем по 5")
    else:
        print(f"{count_of_cake} - не заказываем!")

count_of_cake = int(input())
print_pack_report(count_of_cake)