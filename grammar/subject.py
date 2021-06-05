def transition_table(transition):
    # string "mbah"
    transition[("q41", "m")] = "q3"
    transition[("q0", "m")] = "q3"
    transition[("q3", "b")] = "q4"
    transition[("q4", "a")] = "q5"
    transition[("q5", "h")] = "q40"

    # string "mbak"
    transition[("q41", "m")] = "q3"
    transition[("q0", "m")] = "q3"
    transition[("q3", "b")] = "q4"
    transition[("q4", "a")] = "q1"
    transition[("q1", "k")] = "q40"

    # string "mbok"
    transition[("q41", "m")] = "q3"
    transition[("q0", "m")] = "q3"
    transition[("q3", "b")] = "q4"
    transition[("q4", "o")] = "q1"
    transition[("q1", "k")] = "q40"

    # string "mbek"
    transition[("q41", "m")] = "q3"
    transition[("q0", "m")] = "q3"
    transition[("q3", "b")] = "q4"
    transition[("q4", "e")] = "q1"
    transition[("q1", "k")] = "q40"

    return transition

def parse_table(parse):
    parse[('SB', 'mbah')] = ['mbah']
    parse[('SB', 'mbak')] = ['mbak']
    parse[('SB', 'mbek')] = ['mbek']
    parse[('SB', 'mbok')] = ['mbok']
    parse[('SB', 'bakiak')] = ['error']
    parse[('SB', 'brem')] = ['error']
    parse[('SB', 'bacem')] = ['error']
    parse[('SB', 'becak')] = ['error']
    parse[('SB', 'maca')] = ['error']
    parse[('SB', 'mangan')] = ['error']
    parse[('SB', 'takon')] = ['error']
    parse[('SB', 'tumbas')] = ['error']
    parse[('SB', 'EOS')] = ['error']

    return parse