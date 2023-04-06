#Для онлайн-конференции необходимо написать программу, которая будет подсчитывать общую стоимость билетов. Программа должна работать следующим образом:
# 1. В начале у пользователя запрашивается количество билетов, которые он хочет приобрести на мероприятие.
ticket_count = None
ticket_eligible = 3
ticket_discount = 0.1
print("Введите количество билетов, которые Вы хотите приобрести на мероприятие")
print(f"За {ticket_eligible}+ билета - скидка {ticket_discount*100}%!")
try:
    ticket_count = int(input())
except Exception as NumberExpected:
    print("Ошибка! Вводите число!")

# 2. Далее для каждого билета запрашивается возраст посетителя, в соответствии со значением которого выбирается стоимость:
ticket_price = dict()
price = 0
age = 0
i = 1
while i <= ticket_count:
    print(f"Пожалуйста введите возраст {i} посетителя из {ticket_count}:")

    try:
        age = int(input())
    except Exception as NumberExpected:
        print("Ошибка! Вводите число!")
    # Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
    # От 18 до 25 лет — 990 руб.
    # От 25 лет — полная стоимость 1390 руб.
    if age < 18:
        price = 0
    if 18 <= age < 25:
        price = 990
    if 25 <= age:
        price = 1390
    ticket_price[i] = price
    i += 1
# цикл завершен
# 3. В результате программы выводится сумма к оплате. При этом, если человек регистрирует больше трёх человек
# на конференцию, то дополнительно получает 10% скидку на полную стоимость заказа.
# наведем красоту.
payment = sum(ticket_price.values())
print("Билетов: ", ticket_count)
print("Стоимость: ", payment)
if ticket_count > ticket_eligible:
    print("Вы получили скидку {:0.2f}".format(ticket_discount*100), "%!")
    print("Ваша скидка: {:0.2f}".format(payment*ticket_discount))
    payment = sum(ticket_price.values()) * (1-ticket_discount)
else:
    payment = sum(ticket_price.values())
print("К оплате: {:0.2f}".format(payment))

# Для проверки загрузите полученное решение на GitHub и прикрепите ссылку.
