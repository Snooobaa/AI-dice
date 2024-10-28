import os
from openai import OpenAI
client = OpenAI()


def side_spec() -> int:
    """
    User inputs how many sides they want on their AI dice
    """
    while True:
        dice_sides = int(input("How many sides would you like your dice to have?\n"))
        if dice_sides < 1:
            print("Please enter a positive integer")
        else:
            return dice_sides

def roll_dice():
    """
    OpenAI API Call to roll dice using GPT-4o-mini
    It is worth noting that using the 4o-mini model there is 0 randomness with the current prompt. For example, sides = 6 will always return 4.
    This phenomenon can also be seen when asking 4o-mini to generate number between 1-6 on the web. 
    Unsure if better prompt engineering can add some randomness - can't be bothered to find out. 
    """
    sides = side_spec()
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a random number generator for an AI powered dice."},
        {
            "role": "user",
            "content": f"Generate a single number between 1 and {sides}. Your response should be a single number. Nothing more, nothing less."
        }
    ]
)
    rolled_number = completion.choices[0].message.content
    print(f"You rolled a {rolled_number}!")
    
roll_dice()
