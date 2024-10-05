from ps import PlaintextMessage


plain = PlaintextMessage('abcde', 1)

print(plain.get_message_text())
print(plain.get_message_text_encrypted())
#print(plain.get_shift())
#print(plain.get_valid_words())
