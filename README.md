# spacy-ner-annotator

1: Prepare training data
Label data through this website: http://ai.infintus.com/spacy/

Download json file

2: Change format
Convert json file to txt file with convert_spacy_train_data.py

3: Combining different/previous training data
Input new filename in training_filenames.txt

Run combine_training_data.py

4: Training model
Copy contents of new file created (training_data.txt) to TRAIN_DATA in train.py

Run train.py and name model

5: Testing model
Input test data into TEST_DATA in test.py
