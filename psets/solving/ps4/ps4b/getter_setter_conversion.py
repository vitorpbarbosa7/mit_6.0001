class Temperature:
    def __init__(self, fahrenheit):
        self._fahrenheit = fahrenheit  # Store the internal temperature in Fahrenheit
    
    # Getter to return the temperature in Celsius
    def get_celsius(self):
        return (self._fahrenheit - 32) * 5.0 / 9.0

# Create an instance (internally stored in Fahrenheit)
temp = Temperature(77)

# Access the temperature in Celsius using a getter
print(temp.get_celsius())  # Output: 25.0 (which is Celsius equivalent of 77 Fahrenheit)

