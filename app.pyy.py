def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Select option (1 or 2): ")
    
    if choice == '1':
        val = float(input("Enter Celsius: "))
        print(f"Fahrenheit: {celsius_to_fahrenheit(val)}")
    elif choice == '2':
        val = float(input("Enter Fahrenheit: "))
        print(f"Celsius: {fahrenheit_to_celsius(val)}")
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
