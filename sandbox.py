import openai
import os
import random
import streamlit as st

# Set OpenAI API key (Make sure to set it in environment variables)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Predefined feedback scenarios with roles
scenarios = [
    {"title": "Project Alpha", "role": "Internal Customer", "description": "The team was supposed to deliver a data analysis report, but deadlines were missed. Provide feedback on the team's performance."},
    {"title": "Project Beta", "role": "Project Sponsor", "description": "The project was delivered on time, but key decisions were made without consulting stakeholders. Provide feedback on the decision-making process."},
    {"title": "Project Gamma", "role": "Project Contributor", "description": "A colleague contributed strong technical insights but had trouble collaborating with the team. Provide feedback on their teamwork."},
    {"title": "Project Delta", "role": "Peer Reviewer", "description": "A team member delivered high-quality documentation but often missed team sync meetings. Provide feedback on their engagement."},
    {"title": "Project Epsilon", "role": "Team Member", "description": "A colleague was proactive in brainstorming sessions but sometimes dismissed others' ideas too quickly. Provide structured feedback on their approach."}
]

def evaluate_feedback(feedback, rating):
    prompt = f"""
    Evaluate the following workplace feedback for clarity, constructiveness, balance, and bias.
    If it is vague, too negative, lacks actionability, or is emotionally charged, provide corrections.

    Feedback: {feedback}
    
    Additionally, analyze if the user consistently gives very positive feedback without constructive criticism. 
    The given rating is {rating}/5, check for feedback trends.
    
    Provide an improved version with explanations.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# Streamlit UI
st.title("AI Feedback Sandbox")
st.write("Improve workplace feedback quality by getting AI suggestions.")

# Display project scenarios with better readability
st.subheader("Select a Feedback Scenario")
selected_scenario = st.radio("Choose a scenario:", scenarios, format_func=lambda x: f"{x['title']} - {x['role']}")

if selected_scenario:
    st.subheader(f"Scenario: {selected_scenario['title']}")
    st.write(f"**Alex’s Role:** {selected_scenario['role']}")
    st.write(f"**Situation:** {selected_scenario['description']}")
    
    # User input for feedback
    feedback = st.text_area("Write your feedback here:", "")
    rating = st.slider("How critical is your feedback? (1 = very positive, 5 = highly critical)", 1, 5, 3)
    
    if st.button("Evaluate Feedback"):
        if feedback.strip():
            st.write("### AI Suggestions:")
            improved_feedback = evaluate_feedback(feedback, rating)
            st.write(improved_feedback)
        else:
            st.warning("Please write some feedback before submitting.")

