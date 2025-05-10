# Video Game Controller – OOP Project

![Image](https://github.com/user-attachments/assets/06e150b9-7b8f-47ce-bb96-badfb3e24831)

## Summary
Video Game Controller is a Python-based object-oriented program that simulates a gaming control system using OOP principles such as composition and aggregation. The project includes action buttons, triggers, and joysticks to interact with a character class that can jump, move, attack, and rotate.

## Introduction
This project was developed to reinforce object-oriented programming fundamentals as part of the Week 5 OOP Workshop for the Bachelor of Data Analytics (XBDA) at the University of South Australia (UniSA). It covers:

- Subclassing and inheritance via `Trigger` and `Joystick`
- Aggregation through `Controller` managing a `Character`
- Composition of inputs (Button, Trigger, Joystick)
- Clear separation of responsibilities across modules

> **Note**: This project includes optional challenge features such as joystick-based movement and rotation.

## Project Features
The system allows users to:

- **Map and press standard action buttons** (`A`, `B`, `X`, `Y`) to jump, dodge, craft, and attack
- **Trigger held actions** using `LT` and `RT` (aim and shoot)
- **Move and rotate** with `LJ` and `RJ` joysticks
- **Use directional buttons** (currently inactive for extension)
- **Display character state** like arrow count, jump state, and direction

### Core Mechanics
- Each button is mapped to a specific method on the `Character`
- `Trigger` and `Joystick` extend the base `Button` class for specialized behavior
- `Controller` stores references to inputs and delegates input actions
- `main.py` serves as a test driver for all interactions

### Character State & Movement
- Tracks `x`, `y` position and `facing_angle`
- Responds to input by adjusting coordinates or rotating within 0–360°

## Tools
- Python 3.10+
- PyCharm or VSCode
- GitHub for version control

## Files
```
├── character.py     # Defines the Character class and all action methods
├── button.py        # Base class for all input types
├── trigger.py       # Subclass of Button with optional on_release()
├── joystick.py      # Subclass of Button used to simulate movement and rotation
├── controller.py    # Manages all button mappings and character interaction
├── main.py          # Script to simulate controller input and print character response
├── README.md        # Project documentation
```

## Usage
To use the controller system:

```python
from character import Character
from controller import Controller

character = Character("Aloy")
controller = Controller(character)
controller.map_controller()

# Simulate pressing each action button
for button in controller.get_action_buttons():
    controller.press_button(button)

# Simulate joystick input
for joystick in controller.get_joysticks():
    controller.press_button(joystick)
```

## Sample Output
```
--- Testing Joysticks ---
Pressing Joystick: LJ
Aloy moves up to position (0, 1).
Aloy moves right to position (1, 1).
Pressing Joystick: RJ
Aloy rotates to 45° facing.
```

## Future Enhancements
- Implement on_release() behavior for triggers and joysticks
- Add support for directional button actions
- Integrate menu-based or CLI input
- Persist character state between sessions

## License
This project is intended for educational purposes only as part of coursework for the University of South Australia (UniSA) Bachelor of Data Analytics (XBDA) degree.  
© 2025 Anush De Costa.

## Acknowledgements
Special thanks to the UniSA teaching team for guidance on modular design, delegation principles, and best practices in Python OOP.
