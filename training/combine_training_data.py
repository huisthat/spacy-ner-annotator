#combining training data in different files to the same file

textfile = 'training_filenames.txt'

with open(textfile, 'r', encoding='utf-8') as f:
    names = f.readlines()

combined_names = []

for name in names:
    combined_name = name.strip('\n')
    combined_names.append(combined_name)

training_data = []

for name in combined_names:
    with open(name, 'r', encoding='utf-8') as f:
        text = f.readlines()
        # print(text)
        for line in text: 
            text = line.strip('\n')
            training_data.append(text)

training = training_data[0]

for text in training_data[1:]:
    add_text = text[1:]
    # print(training)
    training = training[:-1] + ", " + add_text 

with open('training_data.txt', 'w') as f:
    f.write(training)