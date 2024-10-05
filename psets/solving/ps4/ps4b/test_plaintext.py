from ps import PlaintextMessage


plain = PlaintextMessage('abcde', 1)

print(plain.get_shift())
print(plain.get_message_text())
print(plain.get_message_text_encrypted())

print('change shift')
plain.change_shift(2)
print(plain.get_shift())

print(plain.get_message_text())
print(plain.get_message_text_encrypted())
