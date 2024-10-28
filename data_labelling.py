import os
import csv

# Set the path to the directory with the MRI images
data_path = "/Users/killercookie/Brain MRI/Alzheimer/MRI"

# Create a list to store the data
data = []

# Loop through each subfolder (label)
for label in os.listdir(data_path):
    label_path = os.path.join(data_path, label)
    
    # Check if it is a directory (to avoid hidden files, etc.)
    if os.path.isdir(label_path):
        # Loop through each file in the folder
        for filename in os.listdir(label_path):
            if filename.endswith(".jpg"):  # Check for .jpg files
                file_path = os.path.join(label_path, filename)
                # Append the filename and label to the data list
                data.append([filename, label])

# Define the path to the output CSV file
csv_path = "/Users/killercookie/Brain MRI/Alzheimer/label.csv"

# Write data to CSV
with open(csv_path, mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    # Write header
    writer.writerow(["id", "label"])
    # Write each row
    writer.writerows(data)

print(f"label.csv created at: {csv_path}")
