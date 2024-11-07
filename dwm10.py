import string 

 

def main(): 

    #1 

    it = int(input("Iterations: ")) 

    factor = float(input("Teleportation factor (0 to 1): ")) 

    n = int(input("Number of pages: ")) 

    #2 

    store_list = {char: 1/n for char in string.ascii_lowercase[:n]} 

    matrix = [list(map(int, input(f"Row {i + 1}: ").split())) for i in range(n)] 

    print("\nMatrix:", *matrix, sep="\n") 

    #3 

    print("\nInitial ranks:", {k: f"{v:.3f}" for k, v in store_list.items()}) 

    #4 

    for x in range(1, it + 1): 

        print(f"\nIteration {x}:") 

        for i in range(n): 

            inbound_sum = sum(store_list[string.ascii_lowercase[j]] / sum(matrix[j])  

                              for j in range(n) if matrix[j][i] == 1 and sum(matrix[j]) > 0) 

            new_rank = (1 - factor) + factor * inbound_sum 

            store_list[string.ascii_lowercase[i]] = new_rank 

            print(f"{string.ascii_lowercase[i]}: {(1 - factor):.3f} + {factor} * {inbound_sum:.3f} = {new_rank:.3f}") 

 

        print("\nUpdated ranks:", {k: f"{v:.3f}" for k, v in store_list.items()}) 

    #5 

    highest_node = max(store_list, key=store_list.get) 

    print(f"\nHighest PageRank: '{highest_node}' = {store_list[highest_node]:.3f}") 

 

if __name__ == '__main__': 

    main() 