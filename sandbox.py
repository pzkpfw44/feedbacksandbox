import random

def get_scenario():
    scenarios = [
        "John has consistently missed deadlines but has strong technical skills. Write constructive feedback for him.",
        "Lisa is a high performer but struggles with teamwork. How would you give her feedback?",
        "Michael is new to the team and seems hesitant to take initiative. Provide feedback to encourage him.",
        "Sarah delivers excellent reports but rarely speaks up in meetings. How would you address this?"
    ]
    return random.choice(scenarios)

def evaluate_feedback(feedback):
    from openai import OpenAI
    
    client = OpenAI()
    prompt = f"""
    Evaluate the following workplace feedback for clarity, constructiveness, balance, and bias. 
    If it is vague, too negative, lacks actionability, or is emotionally charged, provide corrections.
    
    Feedback: {feedback}
    
    Provide an improved version with explanations.
    """
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content

def feedback_sandbox():
    print("Welcome to the AI Feedback Sandbox!\n")
    scenario = get_scenario()
    print(f"Scenario: {scenario}\n")
    
    feedback = input("Write your feedback: ")
    print("\nEvaluating feedback...\n")
    
    improved_feedback = evaluate_feedback(feedback)
    print("AI Suggestions:\n")
    print(improved_feedback)

if __name__ == "__main__":
    feedback_sandbox()
