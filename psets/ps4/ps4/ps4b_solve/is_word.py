from ps4b import load_words, is_word

wordlist = load_words('words.txt')

res = is_word(wordlist, 'a')
print(res)



