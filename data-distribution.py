import os
import json
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

def count_for_dimensions(directory):

    size_counts = defaultdict(int)
    outputs_counts = defaultdict(int)
    outputs_counts_rowxcol = defaultdict(int)

    # Loop through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                train = data['train']
                test = data['test']
                first_train = train[0]
                input_size = len(first_train['input'])
                output_size = len(first_train['output'])
                output_size_total = len(first_train['output']) * len(first_train['output'][0])
                size_counts[(input_size, output_size)] += 1
                outputs_counts[output_size] += 1
                outputs_counts_rowxcol[output_size_total] += 1

    return size_counts, outputs_counts, outputs_counts_rowxcol

def plot_input_output_occurances(size_counts):
    # Sort the size_counts dictionary by the sum of input and output sizes
    sorted_counts = sorted(size_counts.items(), key=lambda x: sum(x[0]))

    # Prepare data for plotting
    sizes = [size for size, _ in sorted_counts]
    counts = [count for _, count in sorted_counts]

    # Convert sizes to strings for x-tick labels
    sizes_str = [f"{size[0]}, {size[1]}" for size in sizes]

    # Plotting
    plt.figure(figsize=(24, 6))
    plt.bar(range(len(sizes_str)), counts, tick_label=sizes_str)
    plt.xlabel('Input and Output Sizes')
    plt.ylabel('Count')
    plt.title('Frequency of Input and Output Sizes')
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.tight_layout()
    plt.show()
    plt.savefig('freq_input_output_sizes.png')

def plot_output_occurances(outputs_counts):
    sorted_sizes = dict(sorted(outputs_counts.items()))

    # Extract x and y values for plotting
    sizes = list(sorted_sizes.keys())
    counts = list(sorted_sizes.values())

    # Plotting
    plt.bar(range(len(sizes)), counts, tick_label=sizes)
    plt.xlabel('Output Sizes')
    plt.ylabel('Count')
    plt.title('Frequency of Output Sizes')
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.show()
    plt.savefig('freq_input_output_sizes.png')

def plot_output_occurances(outputs_counts):
    sorted_sizes = dict(sorted(outputs_counts.items()))

    # Extract x and y values for plotting
    sizes = list(sorted_sizes.keys())
    counts = list(sorted_sizes.values())

    # Plotting
    plt.bar(range(len(sizes)), counts, tick_label=sizes)
    plt.xlabel('Output Sizes')
    plt.ylabel('Count')
    plt.title('Frequency of Output Sizes')
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.show()
    plt.savefig('freq_output_sizes.png')

def plot_output2_occurances(outputs_counts):
    sorted_sizes = dict(sorted(outputs_counts.items()))

    # Extract x and y values for plotting
    x_values = list(sorted_sizes.keys())
    y_values = list(sorted_sizes.values())

    # Define the number of bins (ranges)
    num_bins = 18

    # Calculate the range width
    x_min = min(x_values)
    x_max = max(x_values)
    bin_width = (x_max - x_min) / num_bins

    # Calculate the edges of the bins
    bin_edges = [1, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900]
    #bin_edges = [1, 10, 25, 50, 10000]

    num_bins = len(bin_edges) - 1

    # Group x_values into bins and sum corresponding y values
    binned_y_sums = [0] * num_bins
    for x, y in zip(x_values, y_values):
        for i in range(num_bins):
            if bin_edges[i] <= x < bin_edges[i + 1]:
                binned_y_sums[i] += y
    

    # Calculate the average x value for each bin
    #x_bin_centers = [np.mean(bin) for bin in zip(bin_edges[:-1], bin_edges[1:])]
    x_bin_centers = [(bin_edges[i] + bin_edges[i + 1]) / 2 for i in range(num_bins)]

    # Plot the data
    plt.bar(x_bin_centers, binned_y_sums, width=bin_width, align='center')
    plt.xlabel('Output Sizes (row * col)')
    plt.ylabel('Count')
    plt.title('Frequency of Output (row * col) Sizes')
    plt.xticks(bin_edges)
    plt.xticks(rotation=45, ha='right', fontsize=8)
    
    plt.show()
    plt.savefig('freq_output_rowxcol_sizes.png')


def plot_tokens():
    # input shapes for ARC
    #shapes = [356, 6590, 4460, 2210, 19010, 10406, 947, 6104, 2933, 13895, 12554, 10982, 4835, 3479, 2609, 2210, 686, 1184, 6527, 4679, 6191, 4808, 2120, 1916, 2201, 1370, 3143, 5942, 2210, 2924, 7499, 11219, 4268, 1223, 13604, 4889, 845, 8546, 9998, 1451, 4790, 2753, 1937, 6137, 4004, 4835, 2195, 5843, 13235, 4892, 5717, 4835, 11219, 7157, 542, 3425, 4619, 7619, 2639, 2120, 13604, 5888, 11300, 4028, 3128, 3317, 851, 1223, 2012, 2237, 3413, 2045, 3146, 8837, 2564, 5471, 1784, 4991, 8510, 2210, 887, 1142, 1403, 3344, 8039, 14438, 1031, 2093, 4820, 6332, 929, 7703, 956, 1964, 19010, 6761, 3209, 18470, 5768, 3803, 10655, 2819, 3608, 4811, 2264, 4511, 3659, 24416, 593, 1931, 1775, 16574, 2816, 8024, 5111, 446, 7691, 2210, 6104, 9851, 1952, 1031, 3488, 2624, 7004, 3863, 2303, 2513, 13883, 6191, 3893, 9764, 5216, 2210, 893, 5057, 2156, 9008, 683, 5174, 4220, 6044, 5234, 4250, 1454, 1622, 4034, 3839, 554, 1139, 2000, 998, 8039, 3470, 6545, 2156, 344, 1292, 2585, 3326, 1751, 623, 4835, 2297, 11510, 2816, 1847, 1400, 3422, 479, 1376, 4823, 4016, 3815, 1577, 2423, 1982, 1658, 5885, 3536, 6110, 1745, 2210, 5660, 1370, 6896, 7355, 2210, 3326, 3815, 11264, 6434, 3134, 2210, 2873, 3761, 671, 4700, 2816, 3182, 1541, 5030, 2906, 2243, 3848, 13985, 4376, 11900, 1499, 1046, 5486, 8708, 947, 3026, 1844, 1271, 7028, 1499, 3134, 15668, 13931, 3944, 1856, 11300, 7040, 2210, 3752, 8540, 4262, 7481, 6179, 8600, 24416, 5876, 4610, 2891, 7436, 2954, 4454, 3716, 2816, 1373, 7691, 2063, 8300, 3134, 7226, 9596, 7748, 2210, 8954, 1418, 5342, 1088, 4100, 1160, 2816, 11330, 3932, 15503, 4724, 4868, 4229, 2363, 2216, 3761, 24416, 1370, 947, 2762, 1754, 1145, 8426, 7943, 5174, 2807, 1598, 15374, 4835, 2984, 19010, 5435, 4082, 10274, 1334, 1316, 4082, 6431, 446, 1334, 2438, 5564, 1469, 965, 7571, 2210, 947, 9086, 3782, 2897, 15419, 8510, 1604, 3266, 1067, 2123, 5822, 491, 19010, 2285, 3602, 2495, 1961, 2816, 2360, 4835, 2210, 881, 1124, 4835, 1568, 9764, 2762, 3530, 3131, 1403, 5876, 4988, 2237, 7592, 9035, 2210, 7442, 2651, 10184, 2951, 14213, 8150, 3659, 635, 3269, 14390, 4835, 2579, 788, 4700, 8834, 2891, 2018, 2651, 15590, 443, 10934, 11672, 1619, 1148, 2819, 12878, 3290, 2345, 2276, 2267, 1619, 1358, 6485, 10274, 2567, 2585, 3038, 7583, 4961, 11660, 2678, 3185, 1235, 824, 1259, 1112, 4835, 9344, 18020, 2210, 4028, 10964, 2210, 2534, 3659, 3446, 3488, 10157, 3434, 24416, 2624, 1568, 809, 9164, 9644, 3026, 3806, 4202]
    
    data = shapes

    ranges = [0, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 15000]
    counts, _ = np.histogram(data, bins=ranges)

    # Plot
    plt.bar(range(len(ranges)-1), counts, align='center')
    plt.xticks(range(len(ranges)-1), [f"{ranges[i]}-{ranges[i+1]}" for i in range(len(ranges)-1)], rotation=70)
    
    # Plot the data
    plt.xlabel('Token Range')
    plt.ylabel('Number of Problems')
    plt.title('Number of Problems for Different Token Ranges')
    plt.tight_layout()   # avoid label getting cut off
    
    plt.show()
    plt.savefig('total-tokens.png')



directory = './data/evaluation'  # Change this to the directory containing your JSON files

size_counts, outputs_counts, outputs_counts_rowxcol = count_for_dimensions(directory)

# can only do one at a time
#plot_input_output_occurances(size_counts)
#plot_output_occurances(outputs_counts)
#plot_output2_occurances(outputs_counts_rowxcol)
plot_tokens()
