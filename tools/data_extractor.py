import pandas as pd

# Replace 'your_large_file.csv' with the actual path to your CSV file
input_file_path = '../data/traindata.csv'
output_file_path = '../data/traindata_cleaned.csv'

# Specify the qualifications you're interested in
target_qualifications = ['BCA', 'M.Tech', 'MCA', 'M.Com', 'B.Com', 'B.Tech', 'BBA']

# Specify the columns you want to extract
columns_to_extract = ['Job Description', 'Qualifications']

# Use the 'usecols' parameter to specify the columns you want to read
df = pd.read_csv(input_file_path, usecols=columns_to_extract)

# Filter the DataFrame based on the specified qualifications
filtered_df = df[df['Qualifications'].isin(target_qualifications)]

# Save the extracted columns to a new CSV file
filtered_df.to_csv(output_file_path, index=False)
