from vocab import my_vocab

token = input("Enter your prompt: ")


def encode(text):
    encoded = []
    word = ""

    for char in text:
        if char != " ":
            word += my_vocab[char]
        else:
            word += my_vocab[char]
            encoded.append(int(word))
            word = ""
    if word:
        encoded.append(int(word))

    return encoded


encoded_token = encode(token)
print(f"Encoded token: {encoded_token}")


def decode(encoded_token):
    decoded = ""
    for num in encoded_token:
        word = []
        word_str = str(num)
        for i in range(0, len(word_str), 2):
            word.append(word_str[i : i + 2])

        for i in word:
            for key, value in my_vocab.items():
                if i == value:
                    decoded += key

    return decoded


def vocab_size():
    return len(my_vocab)


print(f"Decoded token: {decode(encoded_token)}")
print(f"Vocab size: {vocab_size()}")
