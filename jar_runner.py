import subprocess
import pandas as pd
#jar_file_path = "C:\\Users\\ved shrirao\\Desktop\\Code\\feed-play-1.0.jar"  # Replace with the actual path to your JAR file

# Run the JAR file and capture its output
process = subprocess.Popen(["java", "-Ddebug=true", "-Dspeed=1.0", "-classpath", "./feed-play-1.0.jar","hackathon.player.Main","dataset.csv", "5000"], stdout=subprocess.PIPE)

# Read and process the continuous stream of data
print('hello')
ctr = 0
while (ctr<10):
    output = process.stdout.readline().decode().strip()
    
input_string = output
print(input_string)
# Split the input_string into multiple strings using '}'
string_list = input_string.split('}')

# Remove any empty strings from the list
string_list = [s for s in string_list if s]

# Store the strings in a list variable
strings = string_list

# Print the list of strings
#print(strings)
data_strings = strings

# Creating an empty list to store dictionaries
data_list = []

# Parsing each string and extracting key-value pairs
for data_string in data_strings:
    data_dict = {}
    pairs = data_string.split("{")[1].split("}")[0].split(", ")
    for pair in pairs:
        key, value = pair.split("=")
        data_dict[key] = value
        data_list.append(data_dict)

    # Creating a DataFrame from the list of dictionaries
df = pd.DataFrame(data_list)

    # Printing the DataFrame
print(df)
ctr+=1



        # Perform your data processing operations here
        # Extract relevant information, perform calculations, etc.

        # Example: Print the captured output
        #print(output)