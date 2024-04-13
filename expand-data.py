import os
import json
import shutil
import copy

def count_files_in_directory(directory):
    count = 0
    for _, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                count += 1
    return count

# Function to determine the bin index
def find_bin_index(output_length, bin_edges):
    for i, edge in enumerate(bin_edges):
        if output_length <= edge:
            return i
    return len(bin_edges)  # If larger than the last bin edge, place in the last bin



def expand_arc(directory_name):
    src_dir = "./data/" + directory_name
    base_dest_dir = "./expanded-data/" + directory_name

    

    for filename in os.listdir(src_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(src_dir, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)

                # write the original problem
                filename, extension = os.path.splitext(filename)
                new_filename = f"{filename}_0.json"
                data['test'] = data['test'][0]

                destination_path = os.path.join(base_dest_dir, new_filename)

                # Write the modified data to a new file
                with open(destination_path, "w") as f:
                    json.dump(data, f)


                train = copy.deepcopy(data['train'])
                test = copy.deepcopy(data['test'])

                # swap the test with each task_demonstration example
                for index, task_demonstration in enumerate(train):
                    new_data = {"train": copy.deepcopy(data['train']), "test": task_demonstration}
                    new_data["train"].remove(task_demonstration)
                    new_data["train"].append(test)

                    # write new data to new file
                    filename, extension = os.path.splitext(filename)
                    new_filename = f"{filename}_{index + 1}.json"
                    
                    intermediate_dir = "./expanded-data/training"   # add all newly created files to training
                    destination_path = os.path.join(intermediate_dir, new_filename)

                    # Write the modified data to a new file
                    with open(destination_path, "w") as f:
                        json.dump(new_data, f)




expand_arc("evaluation")
expand_arc("training")

file_count = count_files_in_directory("./expanded-data/training")
print("Number of files ./expanded-data/training:", file_count)
file_count = count_files_in_directory("./expanded-data/evaluation")
print("Number of files in ./expanded-data/evaluation:", file_count)