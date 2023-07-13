import xml.etree.ElementTree as ET
import os
import shutil


def get_genre_tag_text(file_name):

    tree = ET.parse(file_name)
    root = tree.getroot()

    genre_tag = root.find('.//genre')
    genre = genre_tag.text

    return genre


def copy_file_in_directory(file_name):

    destination_dir = './filtered_genres_Diorisis_xml'

    # Create the destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    # Copy the file to the destination directory
    shutil.copy2(file_name, destination_dir)


def extract_texts_given_genre(file_name):
    
    gerne = get_genre_tag_text(file_name)

    if gerne == 'Narrative':
        copy_file_in_directory(file_name)
    if gerne == 'Essays':
        copy_file_in_directory(file_name)


source_folder_path = './filtered_genres_Diorisis_xml'

# Loop through each file in the folder
for file_name in os.listdir(source_folder_path):

    # Construct the full file path
    file_path = os.path.join(source_folder_path, file_name)
    
    extract_texts_given_genre(file_path)
    