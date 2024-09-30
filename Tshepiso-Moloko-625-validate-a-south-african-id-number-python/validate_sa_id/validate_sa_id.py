from datetime import datetime

def date_parser(date):
    outcome = True
    formatted_date = "%d/%m/%Y"

    parts = date.split('/')
    if len(parts) != 3:
        outcome = False
    else:
        day, month, year = parts
        if not day.isdigit() or not month.isdigit() or not year.isdigit():
            outcome = False
        else:
            day = int(day)
            month = int(month)
            year = int(year)

            if day < 1 or day > 31 or month < 1 or month > 12 or year < 1 or year > 9999:
                outcome = False
            elif month in [4, 6, 9, 11] and day > 30:
                outcome = False
            elif month == 2:
                if day > 29 or (day == 29 and not (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
                    outcome = False

    return outcome

def is_valid_date(date_str):
    year  = date_str[0:2]
    month = date_str[2:4]
    day = date_str[4:6]

    id_date = f"{day}/{month}/{year}"

    return date_parser(id_date)

def is_valid_gender(gender_str):
    gender = int(gender_str)
    if len(gender_str) != 4:
        return False
    if gender < 0000 or gender > 9999:
        return False
    return True

def is_valid_citizenship(citizenship_str):
    return citizenship_str in ["0", "1"]

def is_valid_checksum_digit(id_number):
    check_digit = int(id_number[-1])
    id_without_check_digit = id_number[-2::-1]
    digit_list = [int(individual_digit_in_id_without_check_digit) for individual_digit_in_id_without_check_digit in id_without_check_digit]
    for index in range(len(digit_list)):
        if index % 2 == 0:
            digit_list[index] *= 2
            if digit_list[index] > 9:
                digit_list[index] -= 9
    digit_sum = sum(digit_list)
    calculated_check_digit = (10 - (digit_sum % 10)) % 10
    return check_digit == calculated_check_digit

def is_id_number_valid(id_number):
    return (
        isinstance(id_number, str) and
        len(id_number) == 13 and
        id_number.isdigit() and
        is_valid_date(id_number[:6]) and
        is_valid_gender(id_number[6:10]) and
        is_valid_citizenship(id_number[10]) and
        is_valid_checksum_digit(id_number)
    )

if __name__ == '__main__':
    id_number = '9807246182082'
    print(is_id_number_valid(id_number))