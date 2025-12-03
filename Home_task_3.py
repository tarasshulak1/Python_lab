import re

test_string = """tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""



protected = re.sub(r'“iZ”', '<<KEEP_iZ>>', test_string)
# print(protected)


corrected = re.sub(r'\biz\b', 'is', protected, flags=re.IGNORECASE)

final_text = corrected.replace('<<KEEP_iZ>>', '“iZ”')




sentences = re.split(r'(\.|\?|\!)', final_text)   # keep punctuation separately
normalized = ""

for i in range(0, len(sentences)-1, 2):
    sentence = sentences[i].strip()
    punctuation = sentences[i+1]

    if sentence:
        sentence = sentence.lower()                   # make all lowercase
        sentence = sentence[0].upper() + sentence[1:] # capitalize 1st letter
        normalized += sentence + punctuation + " "

normalized = normalized.strip()


# --------  Build a sentence from last words --------
sentences_list = re.findall(r'([^.!?]+)', normalized)
last_words = []

for s in sentences_list:
    words = s.strip().split()
    if words:
        last_words.append(words[-1])

new_sentence = " ".join(last_words).capitalize() + "."
final_text = normalized + " " + new_sentence


# -------- Count whitespaces --------
whitespace_count = sum(char.isspace() for char in test_string)


# -------- PRINT RESULTS --------
print("FINAL TEXT:\n")
print(final_text)
print("\nNumber of whitespace characters:", whitespace_count)