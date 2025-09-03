# BB 1st MadLib Project

inputs = 0
words =[]
range(len(words))
word_types = ["verb", "breed of dog", "person's name", "number", "noun", "adjective", "a medication"]
while inputs < len(word_types):
    word = input(f"Please type a {word_types[inputs]}: ")
    words.append(word)
    inputs += 1 

lib_1 = "One day, I decided to" + words[0] + "through the park when I stumbled upon a" + words[5] + words[1] + 'wearing sunglasses and a tiny backpack. Naturally, I asked, Hey, are you lost? \nTo my surprise, the dog barked, “Nope! I’m on a mission from"' + words[2] + "to deliver" + words[3] + 'vials of' + words[6] + "to the secret" + words[4] + 'hidden beneath the playground slide. \nI blinked twice, unsure if I was hallucinating or just incredibly sleep-deprived. But before I could react, the dog winked and vanished into a bush, leaving behind a trail of glitter and a half-eaten sandwich.'
print(lib_1)