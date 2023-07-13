import pandas as pd
import xml.etree.ElementTree as ET
import os
import shutil

def extract_words_POS_from_xml(file_name):
    # Parse the XML file
    tree = ET.parse(file_name)
    root = tree.getroot()

    sentences = []
    entries = []
    poses = []

    counter = 0
    # Iterate over sentence tags
    for sentence in root.findall('.//sentence'):
        # Iterate over word tags
        counter += 1
        for word in sentence.findall('.//word'):
            # Find the lemma tag
            lemma_tag = word.find('.//lemma')
            if lemma_tag is not None:
                sentences.append(counter)

                # Extract entry and POS values
                entry = lemma_tag.get('entry')
                pos = lemma_tag.get('POS')
                entries.append(entry)
                poses.append(pos)

    # Create a DataFrame
    df = pd.DataFrame({'Sentence': sentences,'Entry': entries, 'POS': poses})

    return df


def convert_datafream_to_csv(file_name, file_dataframe):

    destination_dir = './filtered_genres_Diorisis_csv'

    # Create the destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    file_dataframe.to_csv(f'{destination_dir}/{file_name}.csv', index=False)




source_folder_path = './filtered_genres_Diorisis_xml'

# Loop through each file in the folder
for file in os.listdir(source_folder_path):

    # Construct the full file path
    file_path = os.path.join(source_folder_path, file)
    
    file_dataframe = extract_words_POS_from_xml(file_path)

    file_name = os.path.splitext(file)[0]

    convert_datafream_to_csv(file_name, file_dataframe)