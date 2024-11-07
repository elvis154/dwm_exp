import pandas as pd 

 

# Define the dataset and convert it to DataFrame 

data = [ 

    {'Color': 'Red', 'Type': 'Sports', 'Origin': 'Domestic', 'Stolen?': 'Yes'}, 

    {'Color': 'Red', 'Type': 'Sports', 'Origin': 'Domestic', 'Stolen?': 'No'}, 

    {'Color': 'Red', 'Type': 'Sports', 'Origin': 'Domestic', 'Stolen?': 'Yes'}, 

    {'Color': 'Red', 'Type': 'Sports', 'Origin': 'Domestic', 'Stolen?': 'No'}, 

    {'Color': 'Yellow', 'Type': 'Sports', 'Origin': 'Imported', 'Stolen?': 'Yes'}, 

    {'Color': 'Yellow', 'Type': 'SUV', 'Origin': 'Imported', 'Stolen?': 'Yes'}, 

    {'Color': 'Yellow', 'Type': 'SUV', 'Origin': 'Imported', 'Stolen?': 'Yes'}, 

    {'Color': 'Yellow', 'Type': 'SUV', 'Origin': 'Domestic', 'Stolen?': 'No'}, 

    {'Color': 'Red', 'Type': 'SUV', 'Origin': 'Imported', 'Stolen?': 'No'}, 

    {'Color': 'Red', 'Type': 'Sports', 'Origin': 'Imported', 'Stolen?': 'Yes'} 

] 

 

df = pd.DataFrame(data) 

 

# Display dataset and dimensions 

print("Training Data Table:") 

print(df) 

print(f"\nRows: {df.shape[0]}, Columns: {df.shape[1]}\n") 

 

# Calculate and display class probabilities 

p_stolen_yes = (df['Stolen?'] == 'Yes').mean() 

p_stolen_no = 1 - p_stolen_yes 

print(f"P(Stolen? = Yes): {p_stolen_yes:.2f}") 

print(f"P(Stolen? = No): {p_stolen_no:.2f}\n") 

 

# Calculate likelihoods 

def calculate_likelihood(attribute, value, stolen_status): 

    subset = df[df['Stolen?'] == stolen_status] 

    return (subset[attribute] == value).mean() 

 

# Likelihoods given Stolen? = Yes 

p_color_yes = calculate_likelihood('Color', 'Red', 'Yes') 

p_type_yes = calculate_likelihood('Type', 'SUV', 'Yes') 

p_origin_yes = calculate_likelihood('Origin', 'Domestic', 'Yes') 

 

# Likelihoods given Stolen? = No 

p_color_no = calculate_likelihood('Color', 'Red', 'No') 

p_type_no = calculate_likelihood('Type', 'SUV', 'No') 

p_origin_no = calculate_likelihood('Origin', 'Domestic', 'No') 

 

# New tuple for classification 

new_tuple = {'Color': 'Red', 'Type': 'SUV', 'Origin': 'Domestic'} 

print("New Tuple for Classification:", new_tuple) 

 

# Calculate posterior probabilities 

posterior_yes = p_color_yes * p_type_yes * p_origin_yes * p_stolen_yes 

posterior_no = p_color_no * p_type_no * p_origin_no * p_stolen_no 

 

# Display classification result 

print("\nPosterior Probabilities:") 

print(f"P(Stolen? = Yes | New Tuple): {posterior_yes:.5f}") 

print(f"P(Stolen? = No | New Tuple): {posterior_no:.5f}") 

if posterior_yes > posterior_no: 

    print("Classified as yes") 

else: 

    print("Classified as no") 

 