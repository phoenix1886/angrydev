from prefix_tree import PrefixTree
from heapq import nsmallest


NUMBER_OF_WORDS_TO_SHOW = 10


class AutocompleteEngine:

    def __init__(
        self,
        words_frequencies,
        num_words_to_show=NUMBER_OF_WORDS_TO_SHOW
    ):
        self.words_frequencies = words_frequencies
        self.prefix_tree = PrefixTree(words_frequencies)
        self.num_words_to_show = num_words_to_show

    def _get_possible_words_with_frequencies(self, prefix):
        possible_words = self.prefix_tree.get_all_possible_words(prefix)
        possible_words_with_frequencies = [
            {'word': word, 'frequency': self.words_frequencies[word]}
            for word in possible_words
        ]
        return possible_words_with_frequencies

    def autocomplete(self, prefix):
        words = [
            word_freq['word'] for word_freq in
            nsmallest(
                self.num_words_to_show,
                self._get_possible_words_with_frequencies(prefix),
                key=lambda word_freq: (
                    -word_freq['frequency'],
                    word_freq['word']
                )
            )
        ]
        return words
