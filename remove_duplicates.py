"""
@arshankar11 / Delhi / 11Oct26
This python script removes duplicate entries from a text file.

Complexity:
Time: O(n)
Space: O(n)

"""

def remove_duplicate_entries (input_file, output_file):
    
    seen_lines = set()  # Sets provide O(1) llokup times

    try:
        with open(input_file,'r',encoding='utf-8') as infile,\
             open(output_file,'w',encoding='utf-8') as outfile:

            for line in infile:
                if line not in seen_lines:
                    outfile.write(line)
                    seen_lines.add(line)

        print(f"Success! Input file duplicate entries cleaned up and saved in : {output_file}")

    except FileNotFoundError:
        print(f"Error: The input file :{input_file} was not found.")
    except Exception as e:
        print (f"Error occured : {e}")

if __name__ == '__main__':
    
    input_file = 'txt/inventory.txt'
    output_file = 'txt/cleaned_inventory.txt'

    remove_duplicate_entries(input_file,output_file)