"""Base64_Distribution_Books

Calculates the distribution in character types of Base64 versus Plain-Text of English books
Author: Axel Persinger
"""


"""Import Libraries

calc_distribution - Custom file to calculate and print the distributions
base64 - Encode buffer to b64
requests - Retrieve text
urllib3 - Because in 2019 I still have to supress certs
"""
import calc_distribution
import base64
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


"""Global Variables
"""


def main():
    global_plain = b''
    global_b64 = b''
    books = {
        'Moby Dick': 'https://www.gutenberg.org/files/2701/2701-0.txt',
        'Pride and Prejudice': 'https://www.gutenberg.org/files/1342/1342-0.txt', 
        'Frankenstein': 'https://www.gutenberg.org/files/84/84-0.txt',
        'A Modest Proposal': 'https://www.gutenberg.org/files/1080/1080-0.txt', 
        'A Strange Case of Dr. Jekyll and Hyde': 'https://www.gutenberg.org/files/43/43-0.txt'
    }

    for title in books:
        plain_text = requests.get(books[title], verify=False).content
        base64_encoded = base64.b64encode(plain_text)

        global_plain += plain_text
        global_b64 += base64_encoded

        plain_distribution = calc_distribution.calc_distribution(plain_text)
        b64_distribution = calc_distribution.calc_distribution(base64_encoded)
        
        calc_distribution.print_distribution(plain_distribution, title+' Plain Text:', len(plain_text))
        calc_distribution.print_distribution(b64_distribution, title+' Base64 Encoded:', len(base64_encoded))
        print('\n')

    plain_distribution = calc_distribution.calc_distribution(global_plain)
    b64_distribution = calc_distribution.calc_distribution(global_b64)

    calc_distribution.print_distribution(plain_distribution, 'All Books Plain Text:', len(global_plain))
    calc_distribution.print_distribution(b64_distribution, 'All Books Base64 Encoded:', len(global_b64))


if __name__ == "__main__":
    main()
