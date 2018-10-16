import re
import phonenumbers


def normalize_phone(raw_number):
    norm_mob = re.sub(r'(\D+)', '', raw_number)
    try:
        parsed_number = phonenumbers.parse(norm_mob, 'RU')
        if phonenumbers.is_valid_number(parsed_number):
            return parsed_number.national_number
    except NumberParseException:
        return raw_number


if __name__ == "__main__":
    normalize_phone('8 929 111-22-33')
    normalize_phone('+79291112266')
