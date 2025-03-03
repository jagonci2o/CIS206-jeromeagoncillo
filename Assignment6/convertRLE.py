def encodeRLE(st):
    n = len(st)
    i = 0
    encoded_string = ""

    while i < n:
        char = st[i]
        count = 1

        # Keep the "#" symbol and the number after it, if there is a number.
        if char == '#':
            encoded_string += '#'
            i += 1
            continue

        # Count the frequency of the same character
        while i < n - 1 and st[i] == st[i + 1]:
            count += 1
            i += 1
        i += 1

        encoded_string += char + (str(count) if count > 1 else "")

    return encoded_string


def decodeRLE(st):
    decoded_string = ""
    n = len(st)
    i = 0

    while i < n:
        if st[i] == '#':  
            # Keep the "#" symbol and the number after it, if there is a number.
            decoded_string += '#'
            i += 1
            if i < n and st[i].isdigit():  # If "#" is followed by a number, keep it
                decoded_string += st[i]
                i += 1
            continue

        char = st[i]
        i += 1
        count = ""

        # If the next characters are digits, collect them
        while i < n and st[i].isdigit():
            count += st[i]
            i += 1

        decoded_string += char * (int(count) if count else 1)

    return decoded_string


def process_input(user_input):
    if user_input.startswith("##00"):
        return decodeRLE(user_input[4:])  # Remove "##00" and decode

    # Detect if the input is RLE encoded (contains letters followed by digits)
    is_rle = any(user_input[i].isalpha() and i + 1 < len(user_input) and user_input[i + 1].isdigit() for i in range(len(user_input)))

    if is_rle:
        return decodeRLE(user_input)

    return encodeRLE(user_input)


def main():
    user_input = input("Enter a string of alphabetic characters or an RLE encoded string: ")
    try:
        print("Processed Output:", process_input(user_input))
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
