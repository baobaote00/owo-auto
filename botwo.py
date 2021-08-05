import time
import random
from pynput.keyboard import Controller, Key
import names

keyboard = Controller()  # Create the controller

def type_string_with_delay(string):
    for character in string:  # Loop over each character in the string
        keyboard.type(character)  # Type the character
        delay = random.uniform(0, 0.5)  # Generate a random number between 0 and 10
        time.sleep(delay)  # Sleep for the amount of seconds generated

i = 0
max = int(input("số lần: "))
print(max)

time.sleep(1.5)

def type_delay(string):
    type_string_with_delay(string)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

while i < max:
    i+=1
    print("count:",i)
    # if random.randint(0,1):
    #     type_delay("owo h")  
    #     time.sleep(random.uniform(1,5))
    #     type_delay("owo b")
    # else:
    #     type_delay("owo b")
    #     time.sleep(random.uniform(1,5))
    #     type_delay("owo h")
    type_delay("owo")
    delay = random.uniform(10, 15)  # Generate a random number between 0 and 10
    print("delay:",delay)  # Sleep for the amount of seconds generated
    time.sleep(delay)
    # if i % 5 == 0 and random.randint(0, 1):
    #     with keyboard.pressed(Key.alt):
    #         keyboard.press(Key.tab)
    #         time.sleep(1)
    #         keyboard.release(Key.tab)

    #     time.sleep(1)
    #     name = names.get_full_name()
    #     type_string_with_delay(name)
    #     for i1 in range(len(name)):
    #         keyboard.press(Key.backspace)
    #         keyboard.release(Key.backspace)
    #     time.sleep(0.5)

    #     with keyboard.pressed(Key.alt):
    #         keyboard.press(Key.tab)
    #         time.sleep(1)
    #         keyboard.release(Key.tab)





