import numpy as np
from sklearn.cluster import KMeans


x_data = np.array(list(map(float, input("Enter the number in X_coordinate leaving space: ").split())))
y_data = np.array(list(map(float, input("Enter the number in Y_coordinate leaving space: ").split())))


data = np.column_stack((x_data, y_data))




k = int(input("Enter the number of cluster: "))
k_means = KMeans(n_clusters=k, random_state=0).fit(data)


print("\n Cluster Center: ", k_means.cluster_centers_.tolist())
for i in range(k):
   print(f"clusrters {i + 1}", data[k_means.labels_ == i].tolist())
