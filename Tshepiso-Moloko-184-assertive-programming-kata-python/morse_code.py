def morse_code_dict():
    morse_dict = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        ",": "--..--",
        ".": ".-.-.-",
        "?": "..--..",
        "/": "-..-.",
        "-": "-....-",
        " ": "/",
        "(": "-.--.",
        ")": "-.--.-",
        "&": ".-...", 
        ":": "---...", 
        ";": "-.-.-.", 
        "=": "-...-", 
        "+": ".-.-.",  
        "_": "..--.-", 
        '"': ".-..-.", 
        "$": "...-..-", 
        "@": ".--.-.",
        "!": "-.-.--",
        "%": ".--.."
    }

    return morse_dict

def check_input_and_output(text, morse):
    if len(text) > 0:
        assert len(text) == len(morse.split(" ")), "the output and input lengths are not equal."
        assert text.count(" ") == morse.count("/"), "the output and input number of spaces are not equal."

def letters_to_morse_code(text):
    if type(text) == float or type(text) == int:
        text = str(text)
    else:
        text = text.lower()

    if len(text) > 0:
        morse_code = " ".join(morse_code_dict()[i] for i in text)
    else:
        morse_code = ""

    check_input_and_output(text, morse_code)
    return morse_code

def morse_code_to_letters(morse_code):
    morse_code = morse_code.replace("_", "-")
    decryption = {value: key for key, value in morse_code_dict().items()}
    if len(morse_code) > 0:
        text = "".join(decryption[i] for i in morse_code.split(" "))
    else:
        text = ""

    check_input_and_output(text, morse_code)
    return text

if __name__ == '__main__':
    print(letters_to_morse_code("Hi there 1 2 3."))