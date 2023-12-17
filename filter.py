import os

def filter_active_files(folder_path):
    # Step 1: List all files in the folder
    file_list = [f for f in os.listdir(folder_path) if f.endswith("_Active.txt")]

    # Step 2: Read the contents of the whitelist file
    with open("whitelist.txt", "r") as whitelist_file:
        whitelist_words = set(line.strip() for line in whitelist_file)

    # Step 3: Iterate through each active file and filter lines
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, "r") as active_file:
            lines = active_file.readlines()

        # Filter lines based on whitelist words
        filtered_lines = [line for line in lines if not any(word in line for word in whitelist_words)]

        # Print and save back the filtered content
        if len(filtered_lines) < len(lines):
            print(f"Filtered words found in {file_name}:")
            for line in set(lines) - set(filtered_lines):
                print(f"  {line.strip()}")

            with open(file_path, "w") as active_file:
                active_file.writelines(filtered_lines)

            print(f"Filtered file saved: {file_name}\n")

if __name__ == "__main__":
    folder_path = "."  # You can replace "." with the path to your folder
    filter_active_files(folder_path)
