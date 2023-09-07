import os

def search_file(file_name, search_path):
    # Walk through the directory tree
    for root, dirs, files in os.walk(search_path):
        if file_name in files:
            # File found
            return os.path.join(root, file_name)
    # File not found
    return None

# Set the search path
search_path = "C:\\Users\\User\\Documents\\My Project\\DOCUTRACKER\\backend\\Server"

# Search for the file
file_path = search_file("data.json", search_path)

if file_path:
    print("File found at:", file_path)
else:
    print("File not found.")