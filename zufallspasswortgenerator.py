import random
import string


def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    passwort_length = int(input("Geben Sie die gewünschte Passwortlänge ein:"))
    password = generate_password(passwort_length)
    print("Generiertes Passwort:", password)


if __name__ == "__main__":
    main()
