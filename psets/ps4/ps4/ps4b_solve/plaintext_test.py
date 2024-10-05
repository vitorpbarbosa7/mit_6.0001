from ps import PlaintextMessage

text = 'turing complete'
plain = PlaintextMessage(text, 1)

print(plain.get_shift())
print(plain.get_message_text())
print(plain.get_message_text_encrypted())

print('change shift')
plain.change_shift(2)
print(plain.get_shift())

print(plain.get_message_text())
print(plain.get_message_text_encrypted())
