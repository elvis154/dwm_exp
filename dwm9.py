from itertools import combinations 
 
def gen_candidates(itemsets, k): 
    return [sorted(set(a) | set(b)) for a in itemsets for b in itemsets if a != b and len(set(a) | set(b)) == k] 
 
def calc_support(dataset, itemset): 
    return sum(1 for t in dataset if all(i in t for i in itemset)) / len(dataset) 
 
def prune_candidates(dataset, candidates, min_support): 
    return [c for c in candidates if calc_support(dataset, c) >= min_support] 
 
def apriori(dataset, min_support): 
    itemsets, k, last_freq_itemsets = [[i] for i in set(i for t in dataset for i in t)], 2, [] 
    while itemsets: 
        itemsets = prune_candidates(dataset, gen_candidates(itemsets, k), min_support) 
        if not itemsets: 
            break 
        # Store only the current level's frequent itemsets 
        last_freq_itemsets = itemsets 
        k += 1 
    # Remove duplicates by converting to a set of tuples, then back to a list of lists 
    last_freq_itemsets = [list(itemset) for itemset in set(tuple(i) for i in last_freq_itemsets)] 
    return last_freq_itemsets 
 
def gen_rules(freq_itemsets, dataset, min_conf): 
    rules = [] 
    for itemset in freq_itemsets: 
        for i in range(1, len(itemset)): 
            for ant in combinations(itemset, i): 
                conf = calc_support(dataset, itemset) / calc_support(dataset, ant) 
                if conf > min_conf: 
                    rules.append((list(ant), list(set(itemset) - set(ant)), round(conf * 100, 2))) 
    return rules 
 
def input_data(): 
    transactions = [] 
    while (t := input("Transaction (comma-separated, 'done' to finish): ")) != 'done': 
        transactions.append([int(i) for i in t.split(',')]) 
    return transactions 
 
dataset = input_data() 
min_support = float(input("Minimum support (%): ")) / 100 
min_conf = float(input("Minimum confidence (%): ")) / 100 
 
freq_itemsets = apriori(dataset, min_support) 
rules = gen_rules(freq_itemsets, dataset, min_conf) 
 
print("\nFrequent Itemsets:", freq_itemsets) 
print("\nAssociation Rules:") 
for ant, con, conf in rules: 
    print(f"{ant} -> {con}, Confidence = {conf}%") 
 