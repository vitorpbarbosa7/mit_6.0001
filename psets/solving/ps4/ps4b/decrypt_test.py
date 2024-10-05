from ps import CiphertextMessage, get_story_string

message = get_story_string()
print(message)

decrypt = CiphertextMessage(message)
decrypt.decrypt_message()
