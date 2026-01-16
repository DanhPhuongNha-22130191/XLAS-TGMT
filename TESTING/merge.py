import os
import glob
import json

def merge_json_files():
    # Define the source directory containing JSON files
    source_dir = r"D:\Download\MENUCOMMENTTESTSUILT"
    
    # Define the output file name
    output_filename = "22130191_DanhPhuongNha_Lab7.json"
    
    # Get the directory where this script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Full path for the output file
    output_path = os.path.join(current_dir, output_filename)
    
    # List to hold the merged data
    merged_data = []
    
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: The directory '{source_dir}' does not exist.")
        return

    # Find all JSON files in the source directory
    json_files = glob.glob(os.path.join(source_dir, "*.json"))
    
    if not json_files:
        print(f"No JSON files found in '{source_dir}'.")
        return

    print(f"Found {len(json_files)} JSON files. Starting merge...")

    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # Append the entire file content as a single item
                merged_data.append(data)
                    
            print(f"Successfully read: {os.path.basename(file_path)}")
        except Exception as e:
            print(f"Error reading file '{os.path.basename(file_path)}': {e}")

    # Write the merged data to the output file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            # Write start of list
            f.write("[\n")
            
            # Iterate and write each item on a new line
            for i, item in enumerate(merged_data):
                # Dump the item to a JSON string (compact, no indent)
                json_str = json.dumps(item, ensure_ascii=False)
                
                # Add comma if not the last item
                if i < len(merged_data) - 1:
                    f.write("    " + json_str + ",\n")
                else:
                    f.write("    " + json_str + "\n")
                    
            # Write end of list
            f.write("]")
            
        print(f"\nSuccessfully merged {len(json_files)} files into '{output_filename}'")
        print(f"Path: {output_path}")
    except Exception as e:
        print(f"Error writing to output file: {e}")

if __name__ == "__main__":
    merge_json_files()
