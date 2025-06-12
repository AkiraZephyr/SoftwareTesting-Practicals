#Write a program in python that implements McCall's Quality model by evaluating software based on reliability, maintainability, and usability criteria.

def prompt_score(question):
    while True:
        try:
            score = int(input(f"{question} (1-5): "))
            if 1 <= score <= 5:
                return score
            print("Score must be between 1 and 5.")
        except ValueError:
            print("Enter a valid integer between 1 and 5.")

CRITERIA = {
    "Reliability": [
        "Handles unexpected input gracefully?",
        "Recovers from crashes or errors automatically?",
        "Responsive and available under load?",
        "Produces consistent results?",
        "Bugs are rare during usage?"
    ],
    "Maintainability": [
        "Code is modular and easy to modify?",
        "Documentation is sufficient and updated?",
        "New developers can understand code easily?",
        "Changes are easy to implement without breaking code?",
        "Version control and CI/CD are integrated?"
    ],
    "Usability": [
        "User interface is intuitive and user-friendly?",
        "Navigation is smooth?",
        "Error messages are clear and helpful?",
        "Key tasks can be performed with minimal guidance?",
        "Help and support documentation is available?"
    ]
}

def evaluate(attribute, questions):
    print(f"\n-- {attribute} --")
    scores = [prompt_score(q) for q in questions]
    return sum(scores) / len(scores)

def main():
    print("McCall’s Quality Model Evaluation\n")
    print("Rate each aspect from 1 (Poor) to 5 (Excellent).\n")
    results = {attr: evaluate(attr, qs) for attr, qs in CRITERIA.items()}

    print("\n--- Summary ---")
    for attr, score in results.items():
        print(f"{attr}: {score:.2f} / 5")
    overall = sum(results.values()) / len(results)
    print(f"\nOverall Quality Score: {overall:.2f} / 5")

    if overall >= 4:
        level = "Excellent"
    elif overall >= 3:
        level = "Good"
    elif overall >= 2:
        level = "Fair"
    else:
        level = "Poor"
    print(f"Quality Level: {level}")

if __name__ == "__main__":
    main()