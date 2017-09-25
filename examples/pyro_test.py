import Pyro4

wordCounter_uri = "PYRO:example.WordCounter@localhost:5000"
lineCounter_uri = "PYRO:example.LineCounter@localhost:5001"

wordCounter = Pyro4.Proxy(wordCounter_uri)
lineCounter = Pyro4.Proxy(lineCounter_uri)
print("wordCounter: {0}".format(wordCounter.get_nb_words("toto titi tata")))
print("lineCounter: {0}".format(lineCounter.get_nb_lines("hello\nworld\n\n!")))
