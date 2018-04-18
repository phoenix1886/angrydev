from autocomplete_engine import AutocompleteEngine
import sys


def parse_words_frequencies(stream=sys.stdin):
    num_of_words = int(
        stream.readline()
    )

    words_frequencies = {}
    for i in range(num_of_words):
        word_freq = stream.readline().rstrip()
        word, frequency = word_freq.split()
        words_frequencies[word] = int(frequency)
    return words_frequencies


def parse_prefixes(stream=sys.stdin):
    num_of_prefixes = int(
        stream.readline()
    )

    prefixes = []
    for i in range(num_of_prefixes):
        prefix = stream.readline().rstrip()
        prefixes.append(prefix)

    return prefixes


if __name__ == '__main__':
    words_frequencies = parse_words_frequencies()
    prefixes = parse_prefixes()

    autocomplete_engine = AutocompleteEngine(
        words_frequencies
    )

    output = []
    for prefix in prefixes:
        output.append('\n'.join(autocomplete_engine.autocomplete(prefix)))
    output = '\n\n'.join(output)

    print(output)
