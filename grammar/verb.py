def transition_table(transition):
    # string "maca"
    transition[("q41", "m")] = "q3"
    transition[("q0", "m")] = "q3"
    transition[("q3", "a")] = "q11"
    transition[("q11", "c")] = "q12"
    transition[("q12", "a")] = "q40"

    # string "mangan"
    transition[("q41", "m")] = "q3"
    transition[("q0", "m")] = "q3"
    transition[("q3", "a")] = "q11"
    transition[("q11", "n")] = "q7"
    transition[("q7", "g")] = "q8"
    transition[("q8", "a")] = "q9"
    transition[("q9", "n")] = "q40"

    # string "takon"
    transition[("q41", "t")] = "30"
    transition[("q0", "t")] = "30"
    transition[("q30", "a")] = "q31"
    transition[("q31", "k")] = "q32"
    transition[("q32", "o")] = "q33"
    transition[("q33", "n")] = "q40"

    # string "tumbas"
    transition[("q41", "t")] = "30"
    transition[("q0", "t")] = "q30"
    transition[("q30", "u")] = "35"
    transition[("q35", "m")] = "q36"
    transition[("q36", "b")] = "q37"
    transition[("q37", "a")] = "q38"
    transition[("q38", "s")] = "q40"

    return transition

def parse_table(parse):
    parse[('VB', 'mbah')] = ['error']
    parse[('VB', 'mbak')] = ['error']
    parse[('VB', 'mbek')] = ['error']
    parse[('VB', 'mbok')] = ['error']
    parse[('VB', 'bakiak')] = ['error']
    parse[('VB', 'brem')] = ['error']
    parse[('VB', 'bacem')] = ['error']
    parse[('VB', 'becak')] = ['error']
    parse[('VB', 'maca')] = ['maca']
    parse[('VB', 'mangan')] = ['mangan']
    parse[('VB', 'takon')] = ['takon']
    parse[('VB', 'tumbas')] = ['tumbas']
    parse[('VB', 'EOS')] = ['error']
    
    return parse