import pandas as pd
import os

concatenated_df = pd.DataFrame()

source_directory = '../Genre_Extraction/filtered_genres_Diorisis_csv'

file_count = len([filename for filename in os.listdir(source_directory) if os.path.isfile(os.path.join(source_directory, filename))])
concatenated = 0


# Iterate over the files in the directory
for filename in os.listdir(source_directory):
    if filename.endswith('.csv'):

        # Read each CSV file into a temporary dataframe
        filepath = os.path.join(source_directory, filename)
        temp_df = pd.read_csv(filepath)

        # Concatenate the temporary dataframe with the main dataframe
        concatenated_df = pd.concat([concatenated_df, temp_df])

    concatenated += 1
    print(f'Concatenated {concatenated}/{file_count}')


# Reset the index of the concatenated dataframe
concatenated_df = concatenated_df.reset_index(drop=True)

# Save the concatenated dataframe to a CSV file
output_filepath = 'unmasked_narrative_essays.csv'
concatenated_df.to_csv(output_filepath, index=False)
