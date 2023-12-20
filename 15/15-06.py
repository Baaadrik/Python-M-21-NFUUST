def print_document(pages):
    for i in pages:
        if "Секрет" in i:
            print("Дальнейшие материалы засекречены")
            return
        print(i)
    print('Напечатано без купюр')
