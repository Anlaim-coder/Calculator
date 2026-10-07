should_encrypt = int(input("Если хотите зашифровать напишите 1,\nесли хотите расшифровать напишите 0:\n"))


def encrypt(text, key) -> str:
    encrypted = ""
    text = text.lower()
    text = text.replace("ё", "е")
    for char in text:
        if ord(char) >= 97 and ord(char) <= 122:
            char = (ord(char)-ord('a') + key) % 26
            encrypted += chr(char+ ord('a'))
        elif ord(char) >= 1072 and ord(char) <= 1103:
            char = (ord(char)-ord('а') + key) % 32
            encrypted += chr(char+ ord('а'))

    return encrypted

if should_encrypt == 1:
    text = str(input("Что хотите зашифровать:\n"))
    key = int(input("ключ:\n"))
    encrypted = encrypt(text, key)
    print(f"Ваш зашифрованный текст:\n{encrypted}")

else:
    text = str(input("Что хотите расшифровать?\n"))
    key = int(input("Ключ:\n"))
    decrypted = encrypt(text, - key)
    print(f"Ваш расшифрованный текст:\n{decrypted}")


