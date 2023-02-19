def concatenate(*args, **kwargs):
    sentences = ''
    for word in args:
        sentences += word

    for key in kwargs:
        sentences = sentences.replace(key, kwargs[key])

    return sentences


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))