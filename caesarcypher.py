direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
  for i in text:
    position = alphabet.index(i) 
    new_position = position + shift
    cypher_text = alphabet[new_position]
    print(cypher_text)
  

def decrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = (position - shift_amount) % 26
    print(new_position)
    cipher_text += alphabet[new_position]
  print(f"The decoded text is {cipher_text}")

if direction == "encode":
  encrypt(text, shift)
elif direction == "decode":
  decrypt(text, shift)
else:
  print("wrong spelling, please try again")
