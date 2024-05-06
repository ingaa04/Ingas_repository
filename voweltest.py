def vowels(text):
    text = text.lower()
    count = 0
    vokale = 'aeiou'
    for i in text:
        if i in vokale:
            count = count+1
    print(f"Die Anzahl der Vokale ist: {count}")
    return count
vowels('Halloo')
