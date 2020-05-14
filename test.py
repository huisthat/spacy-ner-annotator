import spacy
import textwrap

# TEST_DATA = ['We have spotted Mirai targeting port 2020 and 69', 'Sometimes just mentioning the new target DGN2730 is enough.', 'We can still identify if Miori now targets DGN2030 Netgear routers.', 'Emotet has new targets like DGN3000 v3 routers', 'Among the list of devices targeted by the Wicked Mirai are Netgear DGN1000 and DGN2200 v1 routers (also used by Reaper botnet).', 'DGN1000 is a model Emotet targets, see if we can identify it', 'If Mirai targets more Netgear routers, we can detect it', 'Mirai targets a new PHP vulnerability discovered recently', 'Emotet\'s RCE vulnerability is detectable', 'Even in other formats like this: Yowai vairant exploits ports 80, 9999, 43 and 60008', 'This Spacy model can extract port 33567 and 40421/tcp', 'The new malware has been found to target port 22', 'According to researchers, Wicked bot now attacks ports 80 and 9999']
stripped= []
with open('test.txt', 'r') as f:
    sentences = f.readlines()
    [stripped.append(s.rstrip()) for s in sentences]

# Load and test the saved model
output_dir = 'model 1'
print("Loading from", output_dir)
nlp2 = spacy.load(output_dir)

wrapper = textwrap.TextWrapper(width=80)
counter = 1
for text in stripped:
    doc = nlp2(text)
    print(f"-------------------{counter}--------------------")
    print("TEXT:", wrapper.fill(text))

    for ent in doc.ents:
        value = ent.text
        #take out port and ports words from the prediction
        value = value.replace('ports ', '') 
        value = value.replace('port ', '')
        value = value.replace('Port ', '')
        value = value.replace('Ports ', '')
        label = ent.label_
        print(f"LABEL: {label} | VALUE: {value}")
        # print("VALUE:", value)
        # print("LABEL:", label)
    print()
    counter += 1