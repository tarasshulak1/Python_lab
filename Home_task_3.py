import re

test_string = """tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

def rename_iz_to_is(string: str) -> str:
    protected = re.sub(r'“iZ”', '<<KEEP_iZ>>', string)
    corrected = re.sub(r'\biz\b', 'is', protected, flags=re.IGNORECASE)
    final_text = corrected.replace('<<KEEP_iZ>>', '“iZ”')

    return final_text


def normalize_string(string_to_be_normalized: str) -> str:

    sentences = re.split(r'(\.|\?|\!)', string_to_be_normalized)   # keep punctuation separately
    normalized = ""

    for i in range(0, len(sentences)-1, 2):
        sentence = sentences[i].strip()
        punctuation = sentences[i+1]

        if sentence:
            sentence = sentence.lower()                   # make all lowercase
            sentence = sentence[0].upper() + sentence[1:] # capitalize 1st letter
            normalized += sentence + punctuation + " "

    return normalized.strip()



def sentence_from_last_words(normalized_string: str) -> str:
    sentences_list = re.findall(r'([^.!?]+)', normalized_string)
    last_words = []

    for s in sentences_list:
        words = s.strip().split()
        if words:
            last_words.append(words[-1])

    new_sentence = " ".join(last_words).capitalize() + "."
    return normalized_string + " " + new_sentence


def count_whitespace(normalized_string: str) -> int:
    return  sum(char.isspace() for char in test_string)



# -------- PRINT RESULTS --------
final_text = rename_iz_to_is(test_string)
normalized_string = normalize_string(final_text)
print(sentence_from_last_words(normalized_string))
print(count_whitespace(normalized_string))
