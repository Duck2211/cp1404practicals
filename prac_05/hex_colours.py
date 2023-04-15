COLORS = {"": "", "Absolute Zero": "0048ba", "Aquamarine4": "458b74", "Blue Green": "0d98ba", "BlueViolet":"8a2be2","Bole":"79443b","Bone":"e3dac9","Boysenberry":"873260","Brandeis Blue": "0070ff","Brass": "b5a642","BrickRed":"cb4154"}


def main():
    color_name = validate_color_name()
    while color_name != "":
        color_code = COLORS[color_name]
        print(f"{color_code}")
        color_name = validate_color_name()


def validate_color_name():
    "this will ask for the color name"
    color_name = input("Color Name: ").title()
    while color_name not in COLORS:
        print("Invalid Color Name")
        color_name = input("Color Name: ").title()
    return color_name

main()