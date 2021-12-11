def my_dist(word1, word2):
    def iterate(i, j):
        if i == 0 or j == 0:
            return max(i, j)
        elif word1[i - 1] == word2[j - 1]:
            return iterate(i - 1, j - 1)
        else:
            return 1 + min(iterate(i, j - 1),
                           iterate(i - 1, j),
                           iterate(i - 1, j - 1))

    return iterate(len(word1), len(word2))


if __name__ == '__main__':
    print(my_dist('fghij', 'abcde'))