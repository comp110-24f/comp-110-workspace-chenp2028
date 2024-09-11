def get_weather_report() -> str:
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket")
        return weather
    elif weather == "hot":
        print("Keep cool out there!")
        return weather
    else:
        print("I don't recongnize this weather")
        return weather


get_weather_report()
