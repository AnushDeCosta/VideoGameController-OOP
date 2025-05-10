from character import Character
from controller import Controller
from trigger import Trigger  # Only needed if you want to call on_release()

# Step 1: Create a character
character = Character("Aloy")

# Step 2: Create the controller and map inputs
controller = Controller(character)
controller.map_controller()

# Step 3: Test Action Buttons
print("\n--- Testing Action Buttons ---")
for button in controller.get_action_buttons():
    print(f"Pressing: {button.get_mapping()}")
    controller.press_button(button)

# Step 4: Test Trigger Buttons
print("\n--- Testing Trigger Buttons ---")
for trigger in controller.get_triggers():
    print(f"Pressing: {trigger.get_mapping()}")
    controller.press_button(trigger)

    # Optional: Test on_release if available
    if hasattr(trigger, "on_release"):
        trigger.on_release()

# Step 5: Test Directional Buttons (not mapped yet, just test for stability)
print("\n--- Testing Directional Buttons (currently inactive) ---")
for dpad in controller.get_directional_buttons():
    print(f"Pressing: {dpad.get_mapping()}")
    controller.press_button(dpad)

# Step 6: Test Joystick Inputs
print("\n--- Testing Joysticks ---")
for joystick in controller.get_joysticks():
    print(f"Pressing Joystick: {joystick.get_mapping()}")
    controller.press_button(joystick)
