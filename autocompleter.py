from autocomplete_engine import (
    AutocompleteEngine,
    parse_words_frequencies,
    parse_prefixes
)


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
