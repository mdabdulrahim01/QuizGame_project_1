def main():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
            "answer": "A"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "C"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A. O2", "B. H2O", "C. CO2", "D. NaCl"],
            "answer": "B"
        }
    ]

    score = 0

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        user_answer = get_user_answer()
        is_correct = check_answer(user_answer, q["answer"])
        display_feedback(is_correct, q["answer"])
        if is_correct:
            score += 1

    print(f"Your final score is: {score}/{len(questions)}")

def get_user_answer():
    while True:
        answer = input("Your answer (A/B/C/D): ").upper()
        if answer in ["A", "B", "C", "D"]:
            return answer
        else:
            print("Invalid input. Please enter A, B, C, or D.")

def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def display_feedback(is_correct, correct_answer):
    if is_correct:
        print("Correct!")
    else:
        print(f"Wrong. The correct answer is {correct_answer}.")

if __name__ == "__main__":
    main()
