#parse jsgf grammar file
from jsgf import parse_grammar_string

#read and parse grammar file with parse_grammar_string function
with open ('grammar file path', 'r', encoding='utf-8' ) as f:

    grammar_file = f.read()
grammar= parse_grammar_string(grammar_file)
print(grammar)

# function to find rules that match utterances
def find_matching_rules(utt, grammar):
    try:

        find_rule= grammar.find_matching_rules(utt)[0]
        return True

    except:
        return False

#use function to check if utterances from file match a rule
with open ('tests file path', 'r', encoding='utf-8') as file:

    for line in file.readlines():
        assert find_matching_rules(line, grammar), line

    