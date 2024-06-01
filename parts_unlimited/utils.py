from collections import Counter


def most_common_words(descriptions):
    words = Counter(word for desc in descriptions for word in desc.split())
    common = words.most_common(5)
    return [{'word': word, 'count': count} for word, count in common]