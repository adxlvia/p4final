import random

answers = [
    "Yes, definitely.",
    "Ask again later.",
    "I don't think so.",
    "My sources say no.",
    "You may rely on it.",
    "Cannot predict now.",
    "Very doubtful.",
    "Yes."
]

def get_answer():
    """Returns a random answer from the list."""
    return random.choice(answers)

def main():
    print("Welcome to the Macgic 8-ball!")

    while True: 
        question = input("Ask a yes/no question (or type 'quit' to exit): ").strip()

        if question.lower() == 'quit':
            print("Goodbye. Thanks for playing.")
            break

        if question.endswith('?'):
            print(f"Answer: {get_answer}")
        else:
            print("please ask a valid yes/no question (end with a '?').")

main()