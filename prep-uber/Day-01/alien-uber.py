'''
Example 1: words = ["word", "world", "row"], order = "worldabcefghijkmnpqstuvxyz"
Example 2: words = ["word", "wor", "row"], order = "worldabcefghijkmnpqstuvxyz"
Example 3: words = ["hello", "uber"], order = "huabcdefgijklmnpqrstuvwxyz"
Time Complexicity = O(N * L) = O(M) = where M is # of chars in all words
Space Complexicity = O(26) = O(1)
'''
def is_sorted(words, order):

    if len(words) == 1:
        return True

    hash_order = {}

    for i in range(len(order)):
        hash_order[order[i]] = i

    for i in range(len(words) - 1):
        first_word = words[i]
        second_word = words[i + 1]

        for j in range(len(first_word)):

            if j >= len(second_word):
                return False

            index_char_first_word = hash_order[first_word[j]]
            index_char_second_word = hash_order[second_word[j]]

            if index_char_first_word != index_char_second_word:
                if index_char_second_word < index_char_first_word:
                    return False
                else:
                    break

    return True

print(is_sorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
print(is_sorted(["word", "wor", "row"], "worldabcefghijkmnpqstuvxyz"))
print(is_sorted(["hello", "uber"], "huabcdefgijklmnpqrstuvwxyz"))