"""Base64_Distribution

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
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isdigit():
            digit += 1
        else:
            other += 1
    
    return upper, lower, digit, other


def main():
    global_plain = ''
    global_b64 = ''
    books = {
        'Moby Dick': 'https://www.gutenberg.org/files/2701/2701-0.txt',
        'Pride and Prejudice': 'https://www.gutenberg.org/files/1342/1342-0.txt', 
        'Frankenstein': 'https://www.gutenberg.org/files/84/84-0.txt',
        'A Modest Proposal': 'https://www.gutenberg.org/files/1080/1080-0.txt', 
        'A Strange Case of Dr. Jekyll and Hyde': 'https://www.gutenberg.org/files/43/43-0.txt'
    }

    for title in books:
        plain_text = requests.get(books[title], verify=False).text
        base64_encoded = base64.b64encode(plain_text.encode('utf-8')).decode()

        global_plain += plain_text
        global_b64 += base64_encoded

        plain_distribution = calc_distribution(plain_text)
        b64_distribution = calc_distribution(base64_encoded)
        
        print_distribution(plain_distribution, title+' Plain Text:', len(plain_text))
        print_distribution(b64_distribution, title+' Base64 Encoded:', len(base64_encoded))
        print('\n')

    plain_distribution = calc_distribution(global_plain)
    b64_distribution = calc_distribution(global_b64)

    print_distribution(plain_distribution, 'All Books Plain Text:', len(global_plain))
    print_distribution(b64_distribution, 'All Books Base64 Encoded:', len(global_b64))


if __name__ == "__main__":
    main()
