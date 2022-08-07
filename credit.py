from cs50 import get_string
import re
import sys


def main():
    card_number = get_string("Number: ")
    if not is_valid(card_number):
        print("INVALID")
        sys.exit(1)

    if luhn_s_algo(card_number):
        if card_number[0] == "3":
            print("AMEX")
        elif card_number[0] == "5":
            print("MASTERCARD")
        else:
            print("VISA")
    else:
        print("INVALID")


# Checks the validity of input using re (Regex)
def is_valid(number):

    # Regex code to check validity of initial numbers and length of card number
    pattern = re.compile(r'((34|37)\d{13}|5[1-5]\d{14}|(4\d{12}|4\d{15}))$')

    return pattern.match(number)


# Checks whether card number exists based on Luhn's Algorithm. If so, print card type.
def luhn_s_algo(number):
    n = len(number)

    # Defining the two types of sum
    weird_sum = 0
    typical_sum = 0

    # Iterating backwards through card_number, adding each digit to its appropriate sum
    for i in range(n - 1, -1, -1):
        if (n - i) % 2 == 0:
            weird_sum += add_digits(2 * int(number[i]))
        else:
            typical_sum += int(number[i])

    # According to Luhn's Algorithm, the toal sum of a valid card must be a multiple of 10
    total_sum = weird_sum + typical_sum
    return total_sum % 10 == 0


# Calculates the sum of the digits in n. For calculating weird_sum above.
def add_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum


if __name__ == "__main__":
    main()