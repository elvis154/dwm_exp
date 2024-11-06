import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt

def get_user_input():
    return list(map(int, input("Enter the data points (space-separated): ").split()))

def agglomerative_clustering(X, n_clusters):
    # Reshape X to be a 2D array, required by linkage
    X = X.reshape(-1, 1)
    
    # Create a distance matrix using pairwise distances
    distance_matrix = squareform(pdist(X))
    
    # Perform agglomerative clustering
    linkage_matrix = linkage(X, method='single')
    
    # Get cluster labels based on the specified number of clusters
    labels = fcluster(linkage_matrix, n_clusters, criterion='maxclust')
    
    # Create the final clusters based on labels
    clusters = [[i for i in range(len(labels)) if labels[i] == cluster] for cluster in range(1, n_clusters + 1)]
    
    return clusters, distance_matrix, linkage_matrix, labels

def print_clusters(X, clusters, labels):
    print("\nFinal clusters (by data points):")
    for i, cluster in enumerate(clusters, 1):
        if cluster:  # Check if cluster is not empty
            print(f"Cluster {i}: {[X[point] for point in cluster]}")  # Show the actual data points in each cluster
        else:
            print(f"Cluster {i}: Empty")

    print("\nCluster labels for each data point:")
    for i, label in enumerate(labels):
        print(f"Data point {X.flatten()[i]} -> Cluster {label}")  # Flattened X for easy access to original points

def main():
    X = np.array(get_user_input())
    n_clusters = int(input("Enter the number of clusters you want: "))
    
    if n_clusters < 1 or n_clusters > len(X):
        print("Error: The number of clusters must be between 1 and the number of data points.")
        return
    
    clusters, distance_matrix, linkage_matrix, labels = agglomerative_clustering(X, n_clusters)

    # Display the distance matrix
    print("\nDistance Matrix (squared distances between points):\n", distance_matrix)

    # Print the final clusters
    print_clusters(X, clusters, labels)
    
    # Plot the dendrogram for hierarchical clustering visualization
    plt.figure(figsize=(8, 5))
    dendrogram(linkage_matrix, labels=X.flatten(), color_threshold=0)
    plt.title("Dendrogram - Agglomerative Clustering")
    plt.xlabel("Data Points")
    plt.ylabel("Distance")
    plt.show()

if __name__ == "__main__":
    main()
