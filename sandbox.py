import openai
import os
import random

def get_scenario():
    scenarios = [
        "Project Alpha: John was responsible for data analysis but struggled with meeting deadlines. Provide constructive feedback on his contribution.",
        "Project Beta: Lisa took the lead in organizing the project but received complaints about lack of inclusivity in decision-making. Write feedback for her.",
        "Project Gamma: Michael contributed strong technical insights but had trouble collaborating with the team. How would you give him feedback?",
        "Project Delta: Sarah delivered high-quality documentation but often missed team sync meetings. Provide balanced feedback.",
        "Project Epsilon: David was proactive in brainstorming sessions but sometimes dismissed others' ideas too quickly. Write a structured feedback message."
    ]
    return random.choice(scenarios)

def evaluate_feedback(feedback):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    prompt = f"""
    Evaluate the following workplace feedback for clarity, constructiveness, balance, and bias.
    If it is vague, too negative, lacks actionability, or is emotionally charged, provide corrections.
    
    Feedback: {feedback}
    
    Provide an improved version with explanations.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]

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

