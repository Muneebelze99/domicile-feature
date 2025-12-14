def celsius_to_fahrenheit():
    print("Celsius to Fahrenheit Converter")
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}C={fahrenheit}F")
celsius_to_fahrenheit()