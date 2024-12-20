# Accept filename from the user
filename = input("Input the Filename: ")

# Extract the extension
file_extension = filename.split(".")[-1]

# Map common extensions to their full names
extension_map = {
    "py": "python",
    "txt": "text file",
    "jpg": "image",
    "png": "image",
    "pdf": "PDF document",
    "doc": "Word document",
    "docx": "Word document",
    "html": "HTML file",
    "css": "CSS file",
    "js": "JavaScript file"
}

# Get the full name of the extension, or use the raw extension
extension_name = extension_map.get(file_extension, file_extension)

# Display the result
print(f"The extension of the file is : '{extension_name}'")
