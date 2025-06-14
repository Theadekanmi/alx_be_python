def get_weather_recommendation(weather):
    """
    Returns clothing recommendation based on weather condition.
    
    Args:
        weather (str): The current weather condition
        
    Returns:
        str: Clothing recommendation
    """
    weather = weather.lower().strip()  # Normalize input
    
    if weather == "sunny":
        return "Wear a t-shirt and sunglasses."
    elif weather == "rainy":
        return "Don't forget your umbrella and a raincoat."
    elif weather == "cold":
        return "Make sure to wear a warm coat and a scarf."
    else:
        return "Sorry, I don't have recommendations for this weather."

def main():
    """Main function to handle user interaction."""
    # Prompt user for weather input
    weather_input = input("What's the weather like today? (sunny/rainy/cold): ")
    
    # Get and print recommendation
    recommendation = get_weather_recommendation(weather_input)
    print(recommendation)

if __name__ == "__main__":
    main()