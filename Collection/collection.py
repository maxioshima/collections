from functools import lru_cache


@lru_cache(maxsize=None)
def unique_characters_counter(string_for_count):
    unique_characters = []
    [unique_characters.append(string_for_count[a]) for a in range(0, len(string_for_count)) if
     string_for_count.count(string_for_count[a]) == 1]
    return len(unique_characters)


if __name__ == '__main__':
    string_for_count = input()
    print(unique_characters_counter(string_for_count))
