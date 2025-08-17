# Rule based Machine Learning Concept Bot

# Function to show supported Machine Learning topics
def show_help():
    print("\nWelcome to Machine Learning Concept Bot!")
    print("Here are the ML topics you can ask about:")
    print("1. What is Supervised Learning?")
    print("2. What is Unsupervised Learning?")
    print("3. What is Reinforcement Learning?")
    print("4. What are Neural Networks?")
    print("5. What is Overfitting?")
    print("6. What are Decision Trees?")
    print("7. What is Cross Validation?")
    print("8. Take a Quiz")
    print("Type 'help' to see this list again.")
    print("Type 'exit' to quit the bot.\n")

# Function to run a simple Machine Learning quiz
def quiz():
    print("\n Machine Learning Quiz - Answer the following questions:")
    score = 0
    questions = {
        "1. What type of learning uses labeled training data? ": "supervised learning",
        "2. What type of learning finds patterns in data without labels? ": "unsupervised learning",
        "3. What type of learning uses rewards and punishments? ": "reinforcement learning",
        "4. What is it called when a model performs well on training data but poorly on new data? ": "overfitting",
        "5. What tree-based algorithm splits data based on features? ": "decision tree"
    }

    for question, answer in questions.items():
        user_answer = input(question).strip().lower()
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f" Incorrect. The correct answer is: {answer.title()}")

    print(f"\n Quiz Completed! Your Score: {score}/{len(questions)}\n")


def ml_concept_bot():
    show_help()
    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["exit", "quit"]:
            print(" Goodbye! Thanks for using Machine Learning Concept Bot.")
            break
        elif user_input == "help":
            show_help()
        elif "supervised learning" in user_input:
            print("\n Supervised Learning:\nA type of machine learning where the algorithm learns from labeled training data to make predictions on new, unseen data. Examples include classification and regression.")
        elif "unsupervised learning" in user_input:
            print("\n Unsupervised Learning:\nA type of machine learning where the algorithm finds patterns in data without labeled examples. Common techniques include clustering and dimensionality reduction.")
        elif "reinforcement learning" in user_input:
            print("\n Reinforcement Learning:\nA type of machine learning where an agent learns to make decisions by taking actions in an environment and receiving rewards or penalties.")
        elif "neural network" in user_input:
            print("\n Neural Networks:\nComputing systems inspired by biological neural networks. They consist of interconnected nodes (neurons) that process information and can learn complex patterns.")
        elif "overfitting" in user_input:
            print("\n Overfitting:\nA modeling error that occurs when a model learns the training data too well, including noise and outliers, resulting in poor performance on new data.")
        elif "decision tree" in user_input:
            print("\n Decision Trees:\nA flowchart-like tree structure where internal nodes represent features, branches represent decision rules, and leaf nodes represent outcomes.")
        elif "cross validation" in user_input:
            print("\n Cross Validation:\nA technique used to assess how well a model will generalize to new data by dividing the dataset into multiple folds for training and testing.")
        elif "quiz" in user_input:
            quiz()
        else:
            print(" Sorry, I don't understand. Type 'help' to see available topics.\n")

# Main block to run the bot
if __name__ == "__main__":
    ml_concept_bot()