def transition_table(transition):
    # string "bakiak"
    transition[("q41", "b")] = "q21"
    transition[("q0", "b")] = "q21"
    transition[("q21", "a")] = "q22"
    transition[("q22", "k")] = "q26"
    transition[("q26", "i")] = "q27"
    transition[("q27", "a")] = "q28"
    transition[("q28", "k")] = "q40"

    # string "brem"
    transition[("q41", "b")] = "q21"
    transition[("q0", "b")] = "q21"
    transition[("q21", "r")] = "q14"
    transition[("q14", "e")] = "q15"
    transition[("q15", "m")] = "q40"

    # string "bacem"
    transition[("q41", "b")] = "q21"
    transition[("q0", "b")] = "q21"
    transition[("q21", "a")] = "q22"
    transition[("q22", "c")] = "q23"
    transition[("q23", "e")] = "q24"
    transition[("q24", "m")] = "q40"

    # string "becak"
    transition[("q41", "b")] = "q21"
    transition[("q0", "b")] = "q21"
    transition[("q21", "e")] = "q17"
    transition[("q17", "c")] = "q18"
    transition[("q18", "a")] = "q19"
    transition[("q19", "k")] = "q40"

    return transition

def parse_table(parse):
    parse[('NN', 'mbah')] = ['error']
    parse[('NN', 'mbak')] = ['error']
    parse[('NN', 'mbek')] = ['error']
    parse[('NN', 'mbok')] = ['error']
    parse[('NN', 'bakiak')] = ['bakiak']
    parse[('NN', 'brem')] = ['brem']
    parse[('NN', 'bacem')] = ['bacem']
    parse[('NN', 'becak')] = ['becak']
    parse[('NN', 'maca')] = ['error']
    parse[('NN', 'mangan')] = ['error']
    parse[('NN', 'takon')] = ['error']
    parse[('NN', 'tumbas')] = ['error']
    parse[('NN', 'EOS')] = ['error']

    return parse