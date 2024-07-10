# Coffee Machine App

This is a command-line application that simulates the functionality of a coffee machine. Users can order different types of coffee, and the machine will check if there are enough resources to make the coffee and handle payments.

## Features

- **Order Coffee**: Choose from espresso, latte, or cappuccino.
- **Resource Management**: The machine tracks and updates the availability of water, milk, and coffee.
- **Payment Handling**: Accepts coins and calculates change.
- **Reporting**: Displays the remaining resources.
- **Shutdown**: Allows the machine to be turned off.

## How to Run

To run the app, ensure you have Python installed. Then, execute the following command in your terminal:

```bash
python coffee_machine.py
```

## User Instructions

1. **Start the Machine:** The machine will prompt you with **'What would you like? (espresso/latte/cappuccino):'**
2. **Enter Your Choice:
    - Type **'espresso'**, **'latte'**, or **'cappuccino'** to order a coffee.
    - Type **'report'** to display the remaining resources.
    - Type **'off'** to turn off the machine.
3. **Insert Coins**: If you choose to order a coffee, you will be prompted to insert coins.
4. **Receive Change**: The machine will calculate and return the change if the amount inserted is more than the cost of the coffee.
5. **Enjoy Your Coffee**: The machine will dispense your coffee.