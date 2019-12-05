"""Base64_Distribution_Code

Calculates the distribution in character types of Base64 versus Plain-Text of various coding languages
Author: Axel Persinger
"""


"""Import Libraries

calc_distribution - Custom file to calculate and print the distributions
base64 - Encode buffer to b64
zipfile - Decompress contents in memory
io.BytesIO - Handle in memory file buff
requests - Retrieve text
urllib3 - Because in 2019 I still have to supress certs
"""
import calc_distribution
import base64
import zipfile
from io import BytesIO
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


"""Global Variables
"""


def filter_files(zip_buff, lang):
    """filter_files
    Grabs the contents oof files of the specific language (bc Github repoos will contain other file types)
    Args:
        zip_buff (bytes) - Contents of zip file
        lang (str) - Language/file ext to return
    Returns:
        (str) - String containing only text for that language
    """
    rtr = b''
    input_zip=zipfile.ZipFile(BytesIO(zip_buff))
    for name in input_zip.namelist():
        if name.endswith(lang):
            rtr += input_zip.read(name) + b'\n'
    return rtr


def main():
    global_plain = b''
    global_b64 = b''
    languages = {
        '.py': 'https://codeload.github.com/python/cpython/zip/master',
        '.c': 'https://codeload.github.com/curl/curl/zip/master',
        '.cpp': 'https://codeload.github.com/microsoft/terminal/zip/master',
        '.ps1': 'https://codeload.github.com/EmpireProject/Empire/zip/master',
        '.cs': 'https://codeload.github.com/PowerShell/PowerShell/zip/master',
    }

    for lang in languages:
        zipped = requests.get(languages[lang], verify=False).content
        plain_text = filter_files(zipped, lang)
        base64_encoded = base64.b64encode(plain_text)

        global_plain += plain_text
        global_b64 += base64_encoded

        plain_distribution = calc_distribution.calc_distribution(plain_text)
        b64_distribution = calc_distribution.calc_distribution(base64_encoded)
        
        calc_distribution.print_distribution(plain_distribution, lang+' Plain Text:', len(plain_text))
        calc_distribution.print_distribution(b64_distribution, lang+' Base64 Encoded:', len(base64_encoded))
        print('\n')

    plain_distribution = calc_distribution.calc_distribution(global_plain)
    b64_distribution = calc_distribution.calc_distribution(global_b64)

    calc_distribution.print_distribution(plain_distribution, 'All languages Plain Text:', len(global_plain))
    calc_distribution.print_distribution(b64_distribution, 'All languages Base64 Encoded:', len(global_b64))


if __name__ == "__main__":
    main()
