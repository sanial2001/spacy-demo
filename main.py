import collections

import spacy


class Matcher:
    def __init__(self):
        self.purchase = ["purchase", "acquisition", "asset", "investment", "acquirement", "bargain", "booty", "buy",
                         "gain"]
        self.sell = ["sell", "advertise", "auction", "close", "handle", "hawk", "market", "move", "peddle"]
        self.d = collections.defaultdict(int)

    def count(self, text):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        item, qty = "", 0
        for token in doc:
            if token.text.isdigit():
                qty = int(token.text)
            if token.pos_ == "NOUN" and token.tag_ == "NN":
                item += token.text

        for token in doc:
            # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            #      token.shape_, token.is_alpha, token.is_stop)
            if token.pos_ == "VERB" and token.lemma_ in self.purchase:
                self.d[item] += qty
            elif token.pos_ == "VERB" and token.lemma_ in self.sell:
                self.d[item] -= qty

        print(self.d.items())


if __name__ == "__main__":
    obj = Matcher()
    obj.count(text="sold 3 pieces of lux soap")
