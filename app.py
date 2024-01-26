import spacy
from spacypdfreader.spacypdfreader import pdf_reader
import pycountry
nlp = spacy.load("en_core_web_sm")
doc = pdf_reader("countries_nlp/415610_KENYA-2022-HUMAN-RIGHTS-REPORT.pdf", nlp)
gpes = []
for ent in doc.ents:
    if ent.label_ == "GPE":
        gpes.append(ent.text)

countries = []
for gpe in gpes:
    try:
        if pycountry.countries.lookup(gpe):
            countries.append(gpe)
    except:
        pass

countries = set(countries)
countries

