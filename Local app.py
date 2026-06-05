def calculate_batch_ingredients(batch_volume):
    # Ingredient percentages
    percentages = {
        "Sugar": 46.0,
        "Energy Flavor": 0.21525,
        "Energy Blend": 1.5,
        "Citric Acid": 1.17,
        "Sodium Citrate": 0.21,
        "Sodium Benzoate": 0.05,
        "Caffeine": 0.044,
        "Colour": 0.007,
        "Sucralose": 0.02
    }
    
    print(f"\n--- Batch Recipe for {batch_volume} Units ---")
    
    total_ingredients_percentage = 0
    
    # Calculate and print the amount for each ingredient
    for ingredient, percent in percentages.items():
        amount = (percent / 100) * batch_volume
        total_ingredients_percentage += percent
        print(f"* {ingredient}: {amount:.5f} ({percent}%)")
    
    # Calculate the remaining amount for Water
    water_percentage = 100 - total_ingredients_percentage
    water_amount = (water_percentage / 100) * batch_volume
    
    print(f"* Water: {water_amount:.5f} ({water_percentage:.5f}%)")
    print("-" * 45)

# Get batch volume input from the user
try:
    volume = float(input("Enter your Batch Volume: "))
    calculate_batch_ingredients(volume)
except ValueError:
    print("Please enter a valid numeric value.")
