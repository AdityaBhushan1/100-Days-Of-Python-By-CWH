import string
import random

method = str(input("Kindly Choose One\na) Encode\nb)Decode\nChoose between 'a' and 'b': "))
method.lower()

if method == "a" or method == "b":
    ...
else:
    raise ValueError("You Entred The Wrong Method")


message = str(input("Enter The Message To Encode: "))
st = message.split(" ")

if method == 'a':

    encoded_msg = []

    for word in st:
        if len(word) > 3:
            r1 = "qds"
            r2 = "hre"
            encoded_word = r1 + word[1:] + word[0] + r2
            encoded_msg.append(encoded_word)
        else:
            encoded_msg.append(word[ : :-1])

    print(f"Here Is Your Encoded Message:")
    print(" ".join(encoded_msg))

elif method == "b":

    decoded_msg = []

    for word in st:
        if len(word) > 3:
            encoded_word = word[3:-3]
            encoded_word = encoded_word[-1] + encoded_word[:-1]
            decoded_msg.append(encoded_word)
        else:
            decoded_msg.append(word[ : :-1])

    print(f"Here Is Your Decoded Message:")
    print(" ".join(decoded_msg))


