"""Calc_Distribution

Calculates the distribution in character types of Base64 versus Plain-Text
Author: Axel Persinger
"""

"""Import Libraries

requests - Retrieve text
base64 - Convert string to Base64
urllib3 - Because in 2019 I still have to supress certs
"""
import base64
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


"""Global Variables

"""


def print_distribution(dist, title, buff_len):
    """print_distribution
    Print distribution in a pretty format.
    Args:
        dist (list) - Distribution output from calc_distribution
        title
    """
    print("{}\n\tUppercase: {} - {:.2f}%\n\tLowercase: {} - {:.2f}%\n\tDigits: {} - {:.2f}%\n\tOther: {} - {:.2f}%".format(
        title,
        dist[0], dist[0]/buff_len*100,
        dist[1], dist[1]/buff_len*100,
        dist[2], dist[2]/buff_len*100,
        dist[3], dist[3]/buff_len*100,
    ))


def calc_distribution(text):
    """calc_distribution
    Calculates the distribution of uppercase, lowercase, digit, and other characters in a text buffer.
    Args:
        text (str) - Plain-text buffer
    Returns:
        (list) - List in the format of [upper, lower, digit, other]
    """
    upper = 0
    lower = 0
    digit = 0
    other = 0

    for c in text:
        c = bytes([c])
        try:
            if c.isupper():
                upper += 1
            elif c.islower():
                lower += 1
            elif c.isdigit():
                digit += 1
            else:
                other += 1
        except:
            print(type(c), c)
    
    return upper, lower, digit, other