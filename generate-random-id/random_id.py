import random
import string

def random_id(length=6):
    letters = string.ascii_letters
    digits = string.digits
    all_characters = letters + digits
    result = ''
    for i in range(length):
        if(len(result) > length): break;
    
        result += all_characters[random.randint(0, len(all_characters) - 1)]
    return result
