def words_sorting(*args):
    word_dict = {}
    result = []
    for word in args:
        word_dict[word] = 0
        for letter in word:
            word_dict[word] += ord(letter)
    total_sum = sum(word_dict.values())
    if total_sum % 2 == 0:
        sorted_data = sorted(word_dict.items(), key=lambda x: x[0])
        for data in sorted_data:
            result.append(f"{data[0]} - {data[1]}")
    else:
        sorted_data = sorted(word_dict.items(), key=lambda x: -x[1])
        for data in sorted_data:
            result.append(f"{data[0]} - {data[1]}")
    return "\n".join(result)


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

