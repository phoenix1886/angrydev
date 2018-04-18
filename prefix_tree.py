from heapq import nlargest


class Node:

    def __init__(self, char):
        self.val = char
        self.children = {}
        self.end_of_word = False

    def add_child(self, other):
        self.children[other.val] = other

    def traverse_children(self):
        result = []
        for child in self.children.values():
            if child.children:
                if child.end_of_word:
                    result += child.val
                result += [
                    child.val + grand_child
                    for grand_child in child.traverse_children()
                ]
            else:
                result += [child.val]
        return result

    def __add__(self, other):
        return '{}{}'.format(self.val, other.val)

    def __str__(self):
        return self.val


class PrefixTree:

    def __init__(self, words_frequency=None):
        self.root = Node('')
        if words_frequency:
            for word, freq in words_frequency.items():
                self.add_word(word, freq)

    def add_word(self, word, frequency):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.add_child(Node(char))
            current_node = current_node.children[char]
            current_node.frequency = frequency
        current_node.end_of_word = True

    def treverse_prefix(self, prefix):
        current_node = self.root
        for char in prefix:
            if current_node:
                current_node = current_node.children.get(char)
        return current_node

    def get_all_possible_words(self, prefix):
        root_node = self.treverse_prefix(prefix)
        if root_node:
            possible_words = list(map(
                lambda s: prefix+s,
                root_node.traverse_children()))
        else:
            possible_words = []
        return possible_words
