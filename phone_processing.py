import re


def normalize_phone(phone_number):
    if phone_number:
        norm_mob = re.sub(r'(\s+)?[+]?[-]?', '', phone_number)
        print(norm_mob)
        # проверяем строку на наличие в ней только необходимых символов
        numeric_phone = re.findall(r'[\d]', norm_mob)
        print(numeric_phone[0])
        if numeric_phone[0] in ['7', '8']:
            print('NUMERIC PHONE ', numeric_phone[1:])
            print(''.join(numeric_phone[1:]))
        else:
            print('HVG')    
        # если количество знаков в двух строках совпадает, значит это номер телефона
        if (len(numeric_phone) == len(norm_mob)) and (len(norm_mob) >= 10):
            rev_norm_mob = norm_mob[::-1]
            print(rev_norm_mob)
            #norm_mob = rev_norm_mob[0:10]
            
            print(type((norm_mob)))
            # if norm_mob[::-1][0] == '9':
            #     print(norm_mob[::-1])
            #     return norm_mob[::-1]
    else:
        print(phone_number)
        return False


if __name__ == "__main__":
    print(normalize_phone('8 929 111-22-33'))
    print(normalize_phone('+79291112266'))
