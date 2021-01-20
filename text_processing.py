#######################
# Test Processing I   #
#######################

"""
NLP에서 흔히하는 전처리는 소문자 변환, 앞뒤 필요없는 띄어쓰기를 제거하는 등의 텍스트 정규화 (text normalization)입니다. 
이번 숙제에서는 텍스트 처리 방법을 파이썬으로 배워보겠습니다. 
"""


def normalize(input_string):
    string = input_string[:] # copy the input string
    string = string.lower()  # convert to lowercase
    string = string.strip()  # remove left and right spaces
    
    if string:
        string = string.split()
        normalized_string = string[0]
        for i in range(1,len(string)):
            normalized_string = normalized_string + ' ' + string[i]
    else:
        normalized_string = ''

    return normalized_string


def no_vowels(input_string):
    if input_string:
        string = input_string.lower()[:]
        vowels = 'aeiou'
        no_vowel_string = ''
        for i in range(len(string)):
            if string[i] not in vowels:
                no_vowel_string = no_vowel_string + input_string[i]
    else:
        no_vowel_string = ''

    return no_vowel_string
