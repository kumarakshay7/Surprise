import streamlit as st
import time

# Set page configuration
st.set_page_config(page_title="💖 A Special Message for You 💖", layout="centered")

# Custom CSS for an enhanced, romantic design
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Roboto&display=swap');
    body {
        background: linear-gradient(135deg, #ffe6e6, #ffffff);
        font-family: 'Roboto', sans-serif;
    }
    .header {
        color: #ff4d6d;
        text-align: center;
        font-size: 48px;
        font-family: 'Dancing Script', cursive;
        margin-bottom: 20px;
    }
    .message {
        color: #333;
        font-size: 20px;
        padding: 25px;
        background-color: rgba(255, 255, 255, 0.85);
        border-radius: 15px;
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='header'>💌 A Special Message for You 💌</div>", unsafe_allow_html=True)
st.image("https://source.unsplash.com/featured/?romantic", use_column_width=True)

name = st.text_input("Enter your name to begin:")

if name:
    st.write(f"Hello {name}! Get ready to start the quiz before unlocking a special surprise! 💖")
    time.sleep(1)
    
    st.markdown("<h3 style='text-align:center; color:#ff4d6d;'>💡 Answer these questions correctly to unlock the surprise message 💡</h3>", unsafe_allow_html=True)
    
    correct_answers = {
        "q1": "Unwind event", "q2": "Whiskey", "q3": "November 23rd",
        "q4": "Laughing at the movie theater", "q5": "An everlasting memory",
        "q6": "Vickey Ka Woh Wala Video", "q7": "Sweet and smooth like Dard chocolate",
        "q8": "To unlock a special surprise message"
    }
    
    user_answers = {}
    
    def check_answer(question, options, correct):
        user_answer = st.radio(question, options, key=question)
        user_answers[question] = user_answer
        
        if user_answer != "Select an option":
            if user_answer == correct:
                st.success("✅ Correct!")
            else:
                st.error("❌ Wrong Answer!")
    
    check_answer("Where did we first meet?", ["Select an option", "Church", "Office", "Unwind event", "Isha Foundation", "Movie theater"], correct_answers["q1"])
    check_answer("What drink did I ask you about?", ["Select an option", "Soft drink", "Vadka", "Whiskey", "Beer", "Wine"], correct_answers["q2"])
    check_answer("When did I realize I had feelings for you?", ["Select an option", "October 28th", "November 23rd", "December 25th", "January 1st"], correct_answers["q3"])
    check_answer("Which memory makes my heart race the most?", ["Select an option", "Dancing at the Unwind event", "Church", "Strolling at Isha Foundation", "Laughing at the movie theater"], correct_answers["q4"])
    check_answer("What does our journey mean to me?", ["Select an option", "A fleeting moment", "Nothing", "An everlasting memory", "Just a chapter"], correct_answers["q5"])
    check_answer("Which movie did you enjoy watching with me the most?", ["Select an option", "Sanam Teri Kasam", "Chhaava", "Vickey Ka Woh Wala Video"], correct_answers["q6"])
    check_answer("Imagine your life’s theme song. Which of these best describes it?", ["Select an option", "Sweet and smooth like Dard chocolate", "Warm and twisty like noodles", "Deep and dramatic like a sad song"], correct_answers["q7"])
    check_answer("What is the aim of this interactive experience?", ["Select an option", "To unlock a special surprise message", "To test your knowledge", "Just for fun"], correct_answers["q8"])
    
    score = sum([1 for key in correct_answers if user_answers.get(key) == correct_answers[key]])
    
    if score >= 7:
        if name.strip().lower() == "ahona ayan":
            st.success("Congratulations, Ahona Ayan! You got most answers correct! 🎉")
            time.sleep(1)
            
            love_letter = """ **Hey Ahona,**

I’ve been meaning to say something for a while now, but I never found the right words...
            """
            for line in love_letter.split("\n"):
                st.write(line)
                time.sleep(0.2)
    else:
        st.error("Oops! You need at least 6 correct answers to proceed. Please try again! 💡")
else:
    st.info("Please enter your name to begin the experience.")
