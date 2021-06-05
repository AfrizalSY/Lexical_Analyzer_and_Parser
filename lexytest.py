from collections import defaultdict

from grammar import *

import grammar.subject as subject
import grammar.noun as noun
import grammar.verb as verb

def analyzer(input_string):
    input_string = input_string.lower() + "#"

    """
    CFG
    S  ::= SB VB NN
    SB ::= mbah(nenek/kakek) | mbak(kakak kandung/saudara perempuan yang lebih tua) | mbek(kambing) | mbok(nenek)
    VB ::= maca(membaca) | mangan(makan) | takon(bertanya) | tumbas(membeli)
    NN ::= bakiak(sandal kayu) | brem(makanan daerah madiun) | bacem(makanan olahan kecap) | becak(alat transportasi)
    """

    # state initialization [q0, q1, ...]
    state_list = []; list(state_list.append(f'q{i}') for i in range(40))
    
    transition_table = defaultdict(lambda: "ERROR", {})

    # initial state (q0)
    transition_table[("q0", " ")] = "q0"

    # transition for new token (FS)
    
    transition_table[("q40", "#")] = "ACCEPT"
    transition_table[("q40", " ")] = "q41"

    transition_table[("q41", "#")] = "ACCEPT"
    transition_table[("q41", " ")] = "q41"
 
    # Initialize State
    transition_table = subject.transition_table(transition_table)
    transition_table = noun.transition_table(transition_table)
    transition_table = verb.transition_table(transition_table)

    idx_char = 0
    state = "q0"
    current_token = ""

    while state != "ACCEPT":
        current_char = input_string[idx_char]
        current_token += current_char

        print(state, current_char)
        state = transition_table[(state, current_char)]
        if state == "q40":
            print("current token: {} is valid".format(current_token))
            current_token = ""
        if state == "ERROR":
            print("error")
            break
        idx_char += 1
    # Conclusion
    if state == "ACCEPT":
        print(f'\nsemua token yang di input: {input_string} valid\n')

    return state == "ACCEPT"