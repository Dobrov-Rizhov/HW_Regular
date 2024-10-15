import re

from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

new_contacts = {}
for contacts in contacts_list:
    # Сортировка телефонов
    phones = contacts[5]
    if len(phones) == 11:
        phones = '7' + phones[1:]
    phones = re.sub(r'(\+7)\s(\(\d+\))\s(\d+)[-\s](\d+)[-\s](\d+)\sдоб.\s(\d+)', '+7\\2\\3-\\4-\\5 доб.\\6', phones)
    # print(phones)
    # phones = re.sub(r"(\+7)\s(\(\d+\))\s(\d+)[-\s](\d+)[-\s](\d+)\sдоб.\s(\d+)", "+7\\2\\3-\\4-\\5 доб.\\6", phones, 0, re.MULTILINE)  # изменение номера телефона к правильному виду
    # regex = r"(\+7)\s(\(\d+\))\s(\d+)[-\s](\d+)[-\s](\d+)\sдоб.\s(\d+)"
    # subst = "+7\\2\\3-\\4-\\5 доб.\\6"
    # result = re.sub(regex, subst, phones, 0, re.MULTILINE)

    print(phones)
    # if len(contacts[5].split()) > 1:
    #     phones += ' доб.' + contacts[5].split()[1]

    # # Сортировка пользователей
    # lastname = contacts[0]
    # if len(lastname) > 1:
    #   print(lastname)
    # else:
    #   lastname.split(' ')
    # firstname = contacts[1]
    # surname = contacts[2]
    # users = lastname, firstname, surname .split(',')


#     key = (lastname, firstname)
#     if key not in new_contacts:
#         new_contacts[key] = [lastname, firstname, surname, contacts[3], contacts[4], phones, contacts[6]]
#     else:
#         # Объединяем записи
#         new_contacts[key][3] = new_contacts[key][3] or contacts[3]
#         new_contacts[key][4] = new_contacts[key][4] or contacts[4]
#         new_contacts[key][5] = phones  # Сохраняем последний телефон
#
# # Преобразуем в список
# contacts_list = list(new_contacts.values())
#
#
# # TODO 2: сохраните получившиеся данные в другой файл
# # код для записи файла в формате CSV
# with open("phonebook.csv", "w", encoding="utf-8") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)
