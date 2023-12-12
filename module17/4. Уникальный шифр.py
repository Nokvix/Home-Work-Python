from collections import Counter


def count_unique_characters(message: str) -> int:
    return len(list(filter(lambda count: count == 1, Counter(message.lower()).values())))


message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
