from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
import json
from datetime import datetime

load_dotenv()

# Configure Streamlit page
st.set_page_config(page_title="📚 Study Planner Agent", layout="wide")

# Configure Google Generative AI
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

# Create data directory if not exists
if not os.path.exists("data"):
    os.makedirs("data")

# Title and Description
st.title("📚 Student Study Planner Agent")
st.markdown("Your AI-powered study companion for DSA, OS, Python, and Computer Networks")

# Sidebar navigation
st.sidebar.title("🎯 Skills Menu")
skill_choice = st.sidebar.radio(
    "Choose a Skill:",
    ["Home", "Fetch Materials", "Schedule Tasks", "Summarize Notes", "Track Progress"]
)

# Home Page
if skill_choice == "Home":
    st.header("Welcome to Your Study Planner! 🚀")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📖 Skills", "4", "Active")
    with col2:
        st.metric("⏰ Ready to Use", "24/7", "Always")
    with col3:
        st.metric("🎓 Subjects", "4+", "CS Focus")
    with col4:
        st.metric("💪 Support", "Full AI", "Powered")
    
    st.markdown("---")
    st.subheader("What You Can Do:")
    st.write("""
    1. *Fetch Materials* - Get study resources for any topic
    2. *Schedule Tasks* - Create personalized study schedules
    3. *Summarize Notes* - Convert notes into flashcards
    4. *Track Progress* - Monitor your learning journey
    """)

# Skill 1: Fetch Study Materials
elif skill_choice == "Fetch Materials":
    st.header("📖 Fetch Study Materials")
    
    col1, col2 = st.columns(2)
    
    with col1:
        subject = st.selectbox(
            "Select Subject:",
            ["Data Structures & Algorithms", "Operating Systems", "Python Programming", "Computer Networks"]
        )
    
    with col2:
        topic = st.text_input("Enter Topic:", placeholder="e.g., Binary Search Trees")
    
    level = st.radio("Difficulty Level:", ["Beginner", "Intermediate", "Advanced"])
    
    if st.button("🔍 Fetch Materials"):
        if topic:
            st.info(f"Searching for {level} resources on {topic}...")
            
            # Call Google Generative AI
            model = genai.GenerativeModel('gemini-2.5-flash')
            prompt = f"Give me 5 best study resources for {subject} - {topic} at {level} level. Include links and time estimates."
            
            response = model.generate_content(prompt)
            st.success("✅ Resources Found!")
            st.write(response.text)
            
            # Save to JSON
            materials_data = {
                "subject": subject,
                "topic": topic,
                "level": level,
                "timestamp": datetime.now().isoformat(),
                "resources": response.text
            }
            
            with open("data/materials.json", "a") as f:
                json.dump(materials_data, f)
                f.write("\n")
        else:
            st.error("Please enter a topic!")

# Skill 2: Schedule Study Tasks
elif skill_choice == "Schedule Tasks":
    st.header("⏰ Schedule Study Tasks")
    
    col1, col2 = st.columns(2)
    
    with col1:
        subject = st.selectbox(
            "Select Subject:",
            ["Data Structures & Algorithms", "Operating Systems", "Python Programming", "Computer Networks"]
        )
        topic = st.text_input("Enter Topic:", placeholder="e.g., CPU Scheduling")
    
    with col2:
        hours_per_week = st.slider("Hours per Week:", 1, 20, 5)
        deadline_days = st.slider("Deadline (days):", 1, 30, 14)
    
    priority = st.radio("Priority:", ["High", "Medium", "Low"])
    
    if st.button("📅 Create Schedule"):
        st.info(f"Creating schedule for {subject}...")
        
        # Call Google Generative AI
        model = genai.GenerativeModel('gemini-2.5-flash')
        prompt = f"Create a study schedule for {subject} - {topic}. Available: {hours_per_week} hours/week, Deadline: {deadline_days} days, Priority: {priority}. Give day-wise breakdown."
        
        response = model.generate_content(prompt)
        st.success("✅ Schedule Created!")
        st.write(response.text)
        
        # Save to JSON
        schedule_data = {
            "subject": subject,
            "topic": topic,
            "hours_per_week": hours_per_week,
            "deadline_days": deadline_days,
            "priority": priority,
            "timestamp": datetime.now().isoformat(),
            "schedule": response.text
        }
        
        with open("data/schedules.json", "a") as f:
            json.dump(schedule_data, f)
            f.write("\n")

# Skill 3: Summarize Notes
elif skill_choice == "Summarize Notes":
    st.header("📝 Summarize Study Notes")
    
    subject = st.selectbox(
        "Select Subject:",
        ["Data Structures & Algorithms", "Operating Systems", "Python Programming", "Computer Networks"]
    )
    
    topic = st.text_input("Enter Topic:", placeholder="e.g., Sorting Algorithms")
    
    summary_length = st.radio("Summary Length:", ["Brief (50%)", "Medium (70%)", "Detailed (100%)"])
    
    notes = st.text_area("Paste Your Notes Here:", height=200, placeholder="Paste your study notes...")
    
    if st.button("✨ Summarize Notes"):
        if notes:
            st.info("Summarizing your notes...")
            
            # Call Google Generative AI
            model = genai.GenerativeModel('gemini-2.5-flash')
            prompt = f"Summarize these {subject} notes on {topic} as {summary_length}. Create 5 flashcard Q&A pairs:\n\n{notes}"
            
            response = model.generate_content(prompt)
            st.success("✅ Summary Created!")
            st.write(response.text)
            
            # Save to JSON
            summary_data = {
                "subject": subject,
                "topic": topic,
                "summary_length": summary_length,
                "timestamp": datetime.now().isoformat(),
                "summary": response.text
            }
            
            with open("data/summaries.json", "a") as f:
                json.dump(summary_data, f)
                f.write("\n")
        else:
            st.error("Please paste your notes!")

# Skill 4: Track Progress
elif skill_choice == "Track Progress":
    st.header("📊 Track Study Progress")
    
    col1, col2 = st.columns(2)
    
    with col1:
        subject = st.selectbox(
            "Select Subject:",
            ["Data Structures & Algorithms", "Operating Systems", "Python Programming", "Computer Networks"]
        )
        topic = st.text_input("Enter Topic:", placeholder="e.g., Sorting Algorithms")
    
    with col2:
        time_spent = st.slider("Hours Spent Studying:", 0, 50, 5)
        tasks_completed = st.number_input("Tasks Completed:", 0, 100, 15)
    
    goal_percentage = st.slider("Goal Completion %:", 0, 100, 100)
    
    if st.button("📈 Track Progress"):
        st.info("Calculating your progress...")
        
        # Call Google Generative AI
        model = genai.GenerativeModel('gemini-2.5-flash')
        prompt = f"Analyze progress for {subject} - {topic}. Hours spent: {time_spent}, Tasks done: {tasks_completed}, Goal: {goal_percentage}%. Give motivational insights and next steps."
        
        response = model.generate_content(prompt)
        st.success("✅ Progress Tracked!")
        st.write(response.text)
        
        # Progress bar
        progress = min((tasks_completed / max(1, goal_percentage)) * 100, 100)
        st.progress(progress / 100)
        st.write(f"*Progress: {progress:.1f}%*")
        
        # Save to JSON
        progress_data = {
            "subject": subject,
            "topic": topic,
            "time_spent": time_spent,
            "tasks_completed": tasks_completed,
            "goal_percentage": goal_percentage,
            "timestamp": datetime.now().isoformat(),
            "progress": progress,
            "insights": response.text
        }
        
        with open("data/progress.json", "a") as f:
            json.dump(progress_data, f)
            f.write("\n")

# Footer
st.markdown("---")
st.markdown("*Made with pure ❤️ for your learning journey | Powered by Google Generative AI*")