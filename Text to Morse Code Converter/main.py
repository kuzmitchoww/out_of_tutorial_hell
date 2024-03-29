# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----',
                   ',': '--..--',
                   '.': '.-.-.-',
                   '?': '..--..',
                   '/': '-..-.',
                   '-': '-....-',
                   '(': '-.--.',
                   ')': '-.--.-',
                   ' ': ' ',
                   '!': '-.-.--'
                   }


def text_to_morse_converter():
    # Get input from user
    text = input("Enter text to convert into morse code here: \n")
    # Convert input into a list of UpperCase letters (using list comprehension)
    text_to_list = [i.upper() for i in list(text)]
    # Get morse equivalent for every symbol in text using item in text_to_list as a key for a MORSE_CODE_DICT
    # (using list comprehension)
    text_list_to_morse_list = [MORSE_CODE_DICT[i] + ' ' for i in text_to_list]
    # Convert a list of morse symbols into result string to return
    converted_text = "".join(text_list_to_morse_list)

    return f"Here is your text converted into morse code:\n{converted_text}"


if __name__ == "__main__":
    print(text_to_morse_converter())
