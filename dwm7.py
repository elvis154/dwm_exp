import numpy as np 

import matplotlib.pyplot as plt 

from scipy.cluster.hierarchy import dendrogram, linkage 

 

# Agglomerative clustering (single-linkage) 

def agglomerative_clustering(X, n_clusters): 

    clusters = [[i] for i in range(len(X))] 

    dendrogram_steps = [] 

 

    # Perform clustering 

    while len(clusters) > n_clusters: 

        i, j = min((i, j) for i in range(len(clusters)) for j in range(i + 1, len(clusters))), 

            key=lambda pair: min(abs(X[p] - X[q]) for p in clusters[pair[0]] for q in clusters[pair[1]])) 

        clusters[i].extend(clusters[j]) 

        del clusters[j] 

        dendrogram_steps.append([X[p] for cluster in clusters for p in cluster]) 

    return clusters 

 

# Plot the dendrogram 

def plot_dendrogram(X): 

    linked = linkage(np.array(X).reshape(-1, 1), method='single') 

    plt.figure(figsize=(8, 5)) 

    dendrogram(linked, orientation='top', show_leaf_counts=True) 

    plt.xlabel('Data Points') 

    plt.ylabel('Euclidean Distance') 

    plt.title('Dendrogram') 

    plt.show() 

 

# Main function 

def main(): 

    X = list(map(int, input("Enter data points (comma-separated): ").split(','))) 

    n_clusters = int(input("Enter the desired number of clusters: ")) 

     

    clusters = agglomerative_clustering(X, n_clusters) 

    print("\nFinal Clusters:", [[X[i] for i in cluster] for cluster in clusters]) 

    plot_dendrogram(X) 

 

if _name_ == "_main_": 

    main() 
