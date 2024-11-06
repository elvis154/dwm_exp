import numpy as np

def equal_freq_bins(data, num_bins):
    sorted_data = np.sort(data)
    bin_size = len(data) // num_bins
    return [sorted_data[i * bin_size: (i + 1) * bin_size] for i in range(num_bins - 1)] + [sorted_data[(num_bins - 1) * bin_size:]]

def smooth_bins(bins, method):
    func = {'mean': np.mean, 'median': np.median, 'boundary': lambda b: [b[0], b[-1]]}
    return [func[method](b) for b in bins]

# User input
data = np.array(list(map(int, input("Enter numbers separated by commas: ").split(','))))
num_bins = int(input("Enter number of bins: "))

# Binning and smoothing
bins = equal_freq_bins(data, num_bins)
means, medians, boundaries = smooth_bins(bins, 'mean'), smooth_bins(bins, 'median'), smooth_bins(bins, 'boundary')

# Output
print("\nBins:")
for i, b in enumerate(bins, 1):
    print(f"Bin {i}: {b}")

print("\nSmoothing by Mean:")
for i, mean in enumerate(means, 1):
    print(f"Bin {i}: {mean}")

print("\nSmoothing by Median:")
for i, median in enumerate(medians, 1):
    print(f"Bin {i}: {median}")

print("\nSmoothing by Boundary:")
for i, boundary in enumerate(boundaries, 1):
    print(f"Bin {i}: {boundary[0]}, {boundary[0]}, {boundary[1]}")
