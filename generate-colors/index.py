import random
import string

def generate_colors(type="rgb", length=1):
    result = []
    if type == "rgb":
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        for _ in range(length):
            result.append(f"rgb({r}, {g}, {b})")
    
    elif type == "hex":
        letters = "abcdef"
        numbers = string.digits
        all_characters = letters + numbers
        for _ in range(length):
            color = "#"
            for __ in range(6):
                color += all_characters[random.randint(0, len(all_characters) - 1)]
                
            result.append(color)

    return result

type_color = input("Which color format do you prefer ? (hex/rgb) : ")
user_input = input("How Many colors do you want? : ")
print("Result : ", generate_colors(type_color, int(user_input)))