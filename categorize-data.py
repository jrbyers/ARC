import os
import json
import shutil


# Function to determine the bin index
def find_bin_index(output_length, bin_edges):
    for i, edge in enumerate(bin_edges):
        if output_length <= edge:
            return i
    return len(bin_edges)  # If larger than the last bin edge, place in the last bin



def copy_files_based_on_output():
    src_dir = "./data/evaluation"
    base_dest_dir = "./categorized-data"

    bin_edges = [5, 10, 25, 50, 100, 250, 500, 1000]

    for filename in os.listdir(src_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(src_dir, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                train = data['train']
                first_train = train[0]
                output_size = len(first_train['output']) * len(first_train['output'][0])
                
                bin_index = find_bin_index(output_size, bin_edges)
                bin_val = bin_edges[bin_index]
                dest_dir = base_dest_dir + f"/bin_{bin_val}"
                os.makedirs(dest_dir, exist_ok=True)
                shutil.copy(file_path, dest_dir)


copy_files_based_on_output()