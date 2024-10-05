from ps import CiphertextMessage, get_story_string

message = get_story_string()

decrypt = CiphertextMessage(message)
decrypt.decrypt_message()
