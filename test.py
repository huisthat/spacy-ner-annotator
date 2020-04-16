
import spacy

TEST_DATA = ['Emotet has utilized port 1010 to communicate with the servers while Zeus uses 2020 to communicate with the botnets.', 'Yowai variant exploits port 1000, 6000 and 67', 'This Spacy model can extract port 33567 and 40421/tcp', 'The new malware has been found to target port 100', 'According to researchers, Wicked bot now attacks ports 70 and 999', 'There was a spike in connections over port number 107', 'The port that has been most commonly used by the malware is 2000']

output_dir = 'test2'

# test the saved model
print("Loading from", output_dir)
nlp2 = spacy.load(output_dir)
for text in TEST_DATA:
    doc = nlp2(text)
    print("TEXT:", text)

    for ent in doc.ents:
        value = ent.text
        value = value.replace('ports ', '')
        value = value.replace('port ', '')
        label = ent.label_
        print("VALUE:", value)
        print("LABEL:", label)
    print()
    # print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
    # print("Tokens", [(t.text, t.ent_type_, t.ent_iob) for t in doc])

    # with open('PREDS.txt', 'a') as f:
    #     f.write("TEXT: " + text + '\n')
    #     f.write("VALUE: " + value + '\n')
    #     f.write("LABEL: " + label + '\n\n')