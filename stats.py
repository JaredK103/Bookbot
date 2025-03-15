def wordcount(book):
    words = book.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for character in text:
        character = character.lower()
        if character in char_counts:
            char_counts[character] += 1
        else:
            char_counts[character] = 1
    return char_counts

def list_sort(char_counts):
    result = []
    for char, count in char_counts.items():
        report_dict = {"char": char, "count": count}
        result.append(report_dict)
    def sort_on(dict):
        return dict["count"]
    result.sort(reverse=True, key=sort_on)
    return result
