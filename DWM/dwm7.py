import numpy as np


def equal_frequency_binning(data, num_bins):
   sorted_data = np.sort(data)
   bin_size = len(data) // num_bins
   # Handle the case where the number of bins doesn't perfectly divide the data
   bins = [sorted_data[i * bin_size: (i + 1) * bin_size] for i in range(num_bins - 1)]
   bins.append(sorted_data[(num_bins - 1) * bin_size:]) # Include remaining elements in the last bin
   return bins


def bin_mean(bin_data):
   return [np.mean(b) for b in bin_data]


def bin_median(bin_data):
   return [np.median(b) for b in bin_data]


def bin_boundary(bin_data):
   return [b[[0, -1]] for b in bin_data]


# Input from user
user_input = input("Enter numbers separated by commas: ")
data = list(map(int, user_input.split(',')))
num_bins = int(input("Enter the number of bins: "))


# Equal frequency binning
bins = equal_frequency_binning(data, num_bins)


# Smoothing techniques
means = bin_mean(bins)
medians = bin_median(bins)
boundaries = bin_boundary(bins)


# Output results
print("\nSorted Data:")
print(sorted(data))


print("\nBins:")
for i, b in enumerate(bins):
   print(f"Bin {i + 1}: {b}")


print("\nSmoothing by Bin Mean:")
for i in range(num_bins):
   print(f"Bin {i + 1}: {means[i]:.1f} (all values: {means[i]}, {means[i]}, {means[i]})")


print("\nSmoothing by Bin Median:")
for i in range(num_bins):
   print(f"Bin {i + 1}: {medians[i]:.1f} (all values: {medians[i]}, {medians[i]}, {medians[i]})")


print("\nSmoothing by Bin Boundary:")
for i in range(num_bins):
   boundary_values = boundaries[i]
   print(f"Bin {i + 1}: {boundary_values[0]}, {boundary_values[0]}, {boundary_values[1]}")


# Prevent the window from closing immediately
input("\nPress Enter to exit...")


