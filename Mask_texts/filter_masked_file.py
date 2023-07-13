import os

def filter_sentences_with_mask(file_path, output_file):
    with open(file_path, 'r') as file:
        sentences = file.read().split('\n')

    mask_sentences = [sentence for sentence in sentences if '[MASK]' in sentence]

    with open(f'filtered_{output_file}', 'w') as file:
        for sentence in mask_sentences:
            file.write(sentence + '\n')

source_directory = './masked_files'

for filename in os.listdir(source_directory):
    file_path = os.path.join(source_directory, filename)  # Create the full file path
    print(filename)

    # Call the function to filter and write the sentences with the MASK token
    filter_sentences_with_mask(file_path, filename)
