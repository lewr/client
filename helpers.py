layout_wrong_en2ru = {
    '`': "ё", '1': "1", '2': "2", '3': "3", '4': "4", '5': "5", '6': "6", '7': "7", '8': "8", '9': "9", '0': "0",
    'q': "й", 'w': "ц", 'e': "у", 'r': "к", 't': "е", 'y': "н", 'u': "г", 'i': "ш", 'o': "щ", 'p': "з", '[': "х",
    ']': "ъ", 'a': "ф", 's': "ы", 'd': "в", 'f': "а", 'g': "п", 'h': "р", 'j': "о", 'k': "л", 'l': "д", ';': "ж",
    '\'': "э", 'z': "я", 'x': "ч", 'c': "с", 'v': "м", 'b': "и", 'n': "т", 'm': "ь", ',': "б", '.': "ю", ' ': " "
}

layout_wrong_ru2en = {
    'ё': "`", '1': "1", '2': "2", '3': "3", '4': "4", '5': "5", '6': "6", '7': "7", '8': "8", '9': "9", '0': "0",
    'й': "q", 'ц': "w", 'у': "e", 'к': "r", 'е': "t", 'н': "y", 'г': "u", 'ш': "i", 'щ': "o", 'з': "p", 'х': "[",
    'ъ': "]", 'ф': "a", 'ы': "s", 'в': "d", 'а': "f", 'п': "g", 'р': "h", 'о': "j", 'л': "k", 'д': "l", 'ж': ";",
    'э': "\'", 'я': "z", 'ч': "x", 'с': "c", 'м': "v", 'и': "b", 'т': "n", 'ь': "m", 'б': ",", 'ю': ".", ' ': " "    
}

layout_translit_ru2en = {
    'ё': "e", '1': "1", '2': "2", '3': "3", '4': "4", '5': "5", '6': "6", '7': "7", '8': "8", '9': "9", '0': "0",
    'й': "y", 'ц': "c", 'у': "u", 'к': "k", 'е': "e", 'н': "n", 'г': "g", 'ш': "h", 'щ': "h", 'з': "z", 'х': "h",
    'ъ': ".", 'ф': "f", 'ы': "y", 'в': "v", 'а': "a", 'п': "p", 'р': "r", 'о': "o", 'л': "l", 'д': "d", 'ж': "g",
    'э': "e'", 'я': "y", 'ч': "h", 'с': "c", 'м': "m", 'и': "i", 'т': "t", 'ь': ".", 'б': "b", 'ю': "u", ' ': " "    
}

def try_сhange_char(char, layout):
    """Return change string by transliteration"""
    newchar = "" 
    try:
        newchar = layout[char]
    except KeyError:
        pass
    return newchar

def try_correct_layout(name,layout):
    """Return change string by correct layout"""
    corrected_name = ""
    for char in name:
        corrected_name = corrected_name + try_сhange_char(char, layout)
    if len(corrected_name) != len(name):
        corrected_name = ""
    return corrected_name

def fix_name(name):
    """Return option from the transliteration or correcting the layout
    name   -> fix_name, for example:
    ghbdtn -> привет
    привет -> privet
    privet -> привет
    """
    fix_name = try_correct_layout(name, layout_wrong_en2ru)
    if not fix_name:
        fix_name = try_correct_layout(name, layout_translit_ru2en)
    if not fix_name:
        fix_name = name
    return fix_name

def check_config(config, req_params):
    for param in req_params:
        try:
            if config(param):
                pass
        except:
            print(f"{param} not set in .env")
            exit()
