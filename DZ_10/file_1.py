import re
from itertools import zip_longest


#1.
# def regex_string_split(text):
#     pattern = r"[\w'-]+"
#     split_text = re.findall(pattern, text)
#     repeat_result = {}
#     for word in split_text:
#         repeat_result[word.lower()] = repeat_result.get(word.lower(), 0) + 1
#     return f"{split_text}\n{repeat_result}"
#
# user_text = input("Enter your text: ")
# regex_result = regex_string_split(user_text)
# print(regex_result)

#2.
# def regex_contacts_data(file):
#     try:
#         with open(file, "r", encoding="utf-8") as f_start:
#             with open("filter_file.txt", "a", encoding="utf-8") as f_end:
#                 pattern_birthday = r"\d{2}\.\d{2}\.\d{2,4}"
#                 pattern_phone = r"\+?\d{10,12}"
#                 pattern_email = r"[\w.-]+@[\w.-]+\.[a-z]+"
#                 for line in f_start:
#                     temp_list = []
#                     regex_pattern_birthday = re.search(pattern_birthday, line)
#                     regex_pattern_phone = re.search(pattern_phone, line)
#                     regex_pattern_email = re.search(pattern_email, line, flags=re.IGNORECASE)
#
#                     temp_list.append(regex_pattern_birthday.group(0) if regex_pattern_birthday else "No information")
#                     temp_list.append(regex_pattern_phone.group(0) if regex_pattern_phone else "No information")
#                     temp_list.append(regex_pattern_email.group(0) if regex_pattern_email else "No information")
#
#                     f_end.write(f"{', '.join(temp_list)}\n")
#                 return f"New file has been created!"
#     except FileNotFoundError as e:
#         print(e)
#
# new_file_created = regex_contacts_data("contacts_data.txt")
# print(new_file_created)

#3.
# def regex_last_three_letter(string):
#     pattern = r"[\w]{1,3}\b"
#     last_three_letter = re.findall(pattern, string)
#     return ", ".join(last_three_letter)
#
# user_text = input("Enter your text: ")
# result = regex_last_three_letter(user_text)
# print(result)

#4.
def regex_unique_words(text):
    pattern = r"[\w'-]+"
    all_words_list = list(map(lambda x : x.lower(), re.findall(pattern, text)))
    new_dict = {}
    for word in all_words_list:
        new_dict[word] = new_dict.get(word, 0) + 1
    list_unique_words = [key for key, value in new_dict.items() if value == 1]

    return (f"\nУнікальні слова: {', '.join(list_unique_words)}\n"
            f"Кількість всіх слів: {len(all_words_list)}\n"
            f"Кількість унікальних слiв: {len(list_unique_words)}")

user_text = input("Enter your text: ")
result = regex_unique_words(user_text)
print(result)

#5.
#Анна, Коваленко, 19.03.1987, anna@2mail.com, Навчання дуже сподобалось.

# def regex_user_information(text):
#     pattern = (r"(?P<name>\w+)[\s.,-]+"
#                r"(?P<surname>\w+)[\s.,-]+"
#                r"(?P<birthday>\d{2}\.\d{2}\.\d{2,4})[\s.,-]+"
#                r"(?P<email>[\w.-]+@[\w.-]+\.\w{2,6})[\s.,-]+"
#                r"(?P<review>.*$)")
#     all_data = re.search(pattern, text)
#     all_dict = {
#         "name": all_data.group("name") if all_data else "Не знайдено",
#         "surname": all_data.group("surname") if all_data else "Не знайдено",
#         "birthday": all_data.group("birthday") if all_data else "Не знайдено",
#         "email": all_data.group("email") if all_data else "Не знайдено",
#         "review": all_data.group("review") if all_data else "Не знайдено"
#     }
#     return all_dict
#
# user_text = input("Введіть інформацію: ")
# print(regex_user_information(user_text))
