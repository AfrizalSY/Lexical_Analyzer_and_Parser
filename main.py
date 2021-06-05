import lexytest, parsertest

print("""\
Grammar Jawa:
SB = mbah | mbak| mbek | mbok 
VB = maca | mangan | takon | tumbas
NN = bakiak | brem | bacem | becak      
""")

kalimat = input("Masukkan Kalimat / Kata Yang Ingin Diperiksa: ")

print("""\
----------------------------------
    Proses Lexical Analyzer
----------------------------------
""")
is_valid = lexytest.analyzer(kalimat)

print("""\
----------------------------------
          Proses Parser
----------------------------------""")
if is_valid:
   parsertest.analyzer(kalimat)
else :
   print(f'Input string {kalimat}, tidak diterima, tidak ada pada Grammar')  