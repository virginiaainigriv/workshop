import pandas as pd
import random
import numpy as np



def count_words(dataframe):
    return len(dataframe)


# generate list of random numbers to use a positions in the df for mask tokens
def generate_randoms(values):

    # number of random values to select
    num_values_to_select = 1000

    # Select x random values from the list
    return random.sample(list(values), num_values_to_select)


def export_to_txt(dataframe, file_name):
    concatenated_values = []
    current_sentence = None

    for _, row in dataframe.iterrows():
        sentence = row['Sentence']
        entry = row['Entry']

        if current_sentence is None:
            # First entry, set the current_sentence
            current_sentence = sentence
        elif sentence != current_sentence:
            # New sentence, add a newline before starting the next sentence
            concatenated_values.append('\n')
            current_sentence = sentence

        concatenated_values.append(entry)

    with open(f'{file_name}.txt', 'w') as file:
        file.write(' '.join(concatenated_values))


def mask_random(dataframe):

    all_values_maskable = list(range(count_words(dataframe) + 1))

    values_to_be_masked = generate_randoms(all_values_maskable)

    previous_value = 1

    for value in values_to_be_masked:

        while dataframe.loc[previous_value, 'Sentence'] == dataframe.loc[value, 'Sentence']:
            value += 1

        dataframe.loc[value, 'Entry'] = '[MASK]'

        previous_value = dataframe.loc[value, 'Sentence']

    export_to_txt(dataframe, 'masked_concatenated_random')


def mask_part_of_speech(dataframe, part_of_speech):

    # Get the indices where POS is part_of_speech
    all_values_maskable = POS_indices = dataframe[dataframe['POS'] == part_of_speech].index

    values_to_be_masked = generate_randoms(all_values_maskable)

    dataframe.loc[values_to_be_masked, 'Entry'] = '[MASK]'

    export_to_txt(dataframe, f'masked_concatenated_pos_{part_of_speech}')



dataframe = pd.read_csv('unmasked_narrative_essays.csv')
dataframe = dataframe.dropna(subset=['Entry', 'POS'])
dataframe = dataframe.reset_index(drop=True)

# Set the display options to show all rows
pd.set_option('display.max_rows', None)


df0 = dataframe.copy()
df1 = dataframe.copy()
df2 = dataframe.copy()
df3 = dataframe.copy()

mask_random(df0)
mask_part_of_speech(df1, 'noun')
mask_part_of_speech(df2, 'verb')
mask_part_of_speech(df3, 'adjective')



