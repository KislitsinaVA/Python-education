def patience_info(**kwargs):
    return list(kwargs.values())


print(patience_info(name=input("Введите свое имя: "),
                    surname=input("Введите свою фамилию: "),
                    data=input("Введите дату рождения: "),
                    town=input("Введите город проживания: "),
                    email=input("Введите адрес электронной почты: "),
                    phone=input("Введите номер телефона: ")), end='')
					#данные о пациенте получились одним списком. Это корректно или важна именно строка?