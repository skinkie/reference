import os


def replace_string_with_number(filename, string_to_replace, prefix):
    if not os.path.isfile(filename):
        print(f"Error: '{filename}' is not a valid file.")
        return

    # Open the input file for reading
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Replace the string with sequential numbers and prefix
    new_lines = []
    count = 1
    for line in lines:
        new_line = line.replace(string_to_replace, f"{prefix}{count}")
        new_lines.append(new_line)
        count += 1

    # Create a new file with the modified content
    new_filename = f"{filename}"
    with open(new_filename, 'w') as file:
        file.writelines(new_lines)

    print(f"Replacement completed. Modified content saved in '{new_filename}'.")


# Example usage
filename = 'C:/Users/ue71603/MG_Daten/conversion/at/NX-PI_01_at_svv_LINE_svv_3-155-j22_20220503.xml'  # Replace with your input filename
string_to_replace = 'xxx'  # Replace with the string to be replaced
prefix = 'num_'  # Replace with your desired prefix

replace_string_with_number(filename, string_to_replace, prefix)

