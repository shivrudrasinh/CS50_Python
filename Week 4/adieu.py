# CS50P Adieu, Adieu

import inflect

def main():
    p = inflect.engine()
    names = []

    # Keep taking names until EOF
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()  # move to a new line after Ctrl+D / Ctrl+Z
            break

    # Join names with commas and "and"
    output = p.join(names)
    print(f"Adieu, adieu, to {output}")


if __name__ == "__main__":
    main()
