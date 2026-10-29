def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    print("=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    choice = input("Select option (1): ")
    
    if choice == '1':
        val = float(input("Enter Celsius: "))
        print(f"Fahrenheit: {celsius_to_fahrenheit(val)}")
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
