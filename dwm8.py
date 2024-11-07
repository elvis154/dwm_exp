def equal_frequency_binning(data, num_bins): 

    sorted_data = sorted(data) 

    bin_size = len(data) // num_bins 

    bins = [sorted_data[i * bin_size: (i + 1) * bin_size] for i in range(num_bins - 1)] 

    bins.append(sorted_data[(num_bins - 1) * bin_size:]) 

    return bins 

 

def bin_mean(bins): 

    return [sum(b) / len(b) for b in bins] 

 

def bin_median(bins): 

    return [sorted(b)[len(b) // 2] for b in bins] 

 

def bin_boundary(bins): 

    return [(b[0], b[-1]) for b in bins] 

 

def main(): 

    data = list(map(int, input("Enter numbers separated by commas: ").split(','))) 

    num_bins = int(input("Enter the number of bins: ")) 

     

    bins = equal_frequency_binning(data, num_bins) 

    means = bin_mean(bins) 

    medians = bin_median(bins) 

    boundaries = bin_boundary(bins) 

 

    print("\nBins:") 

    for i, b in enumerate(bins): 

        print(f"Bin {i + 1}: {b}") 

 

    print("\nSmoothing by Bin Mean:") 

    for i, mean in enumerate(means): 

        print(f"Bin {i + 1}: {[mean] * len(bins[i])}") 

 

    print("\nSmoothing by Bin Median:") 

    for i, median in enumerate(medians): 

        print(f"Bin {i + 1}: {[median] * len(bins[i])}") 

 

    print("\nSmoothing by Bin Boundary:") 

    for i, boundary in enumerate(boundaries): 

        print(f"Bin {i + 1}: {[boundary[0]] * (len(bins[i]) - 1) + [boundary[1]]}") 

 

    input("\nPress Enter to exit...") 

 

if __name__ == "__main__": 

    main() 

##################################################################


import matplotlib.pyplot as plt 

 

# Function to plot bar chart 

def plot_bar_chart(data): 

    # Creating labels for the data 

    labels = [f"Student {i+1}" for i in range(len(data))] 

    # Plotting the bar chart 

    plt.figure(figsize=(8, 6)) 

    plt.bar(labels, data, color='blue') 

    plt.xlabel('Students') 

    plt.ylabel('No. of Chocolates') 

    plt.title('Bar Graph of User Input Data') 

    plt.show() 

 

# Function to plot histogram 

def plot_histogram(data): 

    # Plotting the histogram 

    plt.figure(figsize=(8, 6)) 

    plt.hist(data, bins=5, color='green', edgecolor='black') 

    plt.xlabel('Value Range') 

    plt.ylabel('Frequency') 

    plt.title('Histogram of User Input Data') 

    plt.show() 

 

def main(): 

    

    data = list(map(int, input("Enter space-separated integers: ").split())) 

 

    # Visualize the data 

    plot_bar_chart(data) 

    plot_histogram(data) 

 

if __name__ == "__main__": 

    main() 
