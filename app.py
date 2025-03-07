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
st.image("https://source.unsplash.com/featured/?romantic", use_container_width=True)

name = st.text_input("Enter your name to begin:")

if name:
    st.write(f"Hello {name}! Get ready to start the quiz before unlocking a special surprise! 💖")
    time.sleep(1)
    
    st.markdown("<h3 style='text-align:center; color:#ff4d6d;'>💡 Answer these questions correctly to unlock the surprise message 💡</h3>", unsafe_allow_html=True)
    
    correct_answers = {
        "Where did we first meet?": "Unwind event",
        "What drink did I ask you about?": "Whiskey",
        "When did I realize I had feelings for you?": "November 23rd",
        "Which memory makes my heart race the most?": "Laughing at the movie theater",
        "What does our journey mean to me?": "An everlasting memory",
        "Which movie did you enjoy watching with me the most?": "Vickey Ka Woh Wala Video",
        "Imagine your life’s theme song. Which of these best describes it?": "Sweet and smooth like Dark chocolate",
        "What is the aim of this interactive experience?": "To unlock a special surprise message"
    }
    
    user_answers = {}
    
    def check_answer(question, options, correct):
        answer = st.radio(question, options, key=question)
        user_answers[question] = answer
        if answer != "Select an option":
            if answer == correct:
                st.success("✅ Correct!")
            else:
                st.error("❌ Wrong Answer!")
        return answer
    
    # Call check_answer for each question
    q1 = check_answer("Where did we first meet?", 
                      ["Select an option", "Church", "Office", "Unwind event", "Isha Foundation", "Movie theater"],
                      correct_answers["Where did we first meet?"])
    q2 = check_answer("What drink did I ask you about?", 
                      ["Select an option", "Soft drink", "Vadka", "Whiskey", "Beer", "Wine"],
                      correct_answers["What drink did I ask you about?"])
    q3 = check_answer("When did I realize I had feelings for you?", 
                      ["Select an option", "October 28th", "November 23rd", "December 25th", "January 1st"],
                      correct_answers["When did I realize I had feelings for you?"])
    q4 = check_answer("Which memory makes my heart race the most?", 
                      ["Select an option", "Dancing at the Unwind event", "Church", "Strolling at Isha Foundation", "Laughing at the movie theater"],
                      correct_answers["Which memory makes my heart race the most?"])
    q5 = check_answer("What does our journey mean to me?", 
                      ["Select an option", "A fleeting moment", "Nothing", "An everlasting memory", "Just a chapter"],
                      correct_answers["What does our journey mean to me?"])
    q6 = check_answer("Which movie did you enjoy watching with me the most?", 
                      ["Select an option", "Sanam Teri Kasam", "Chhaava", "Vickey Ka Woh Wala Video"],
                      correct_answers["Which movie did you enjoy watching with me the most?"])
    q7 = check_answer("Imagine your life’s theme song. Which of these best describes it?", 
                      ["Select an option", "Sweet and smooth like Dark chocolate", "Warm and twisty like noodles", "Deep and dramatic like a sad song"],
                      correct_answers["Imagine your life’s theme song. Which of these best describes it?"])
    q8 = check_answer("What is the aim of this interactive experience?", 
                      ["Select an option", "To unlock a special surprise message", "To test your knowledge", "Just for fun"],
                      correct_answers["What is the aim of this interactive experience?"])
    
    # Calculate score by checking user_answers dictionary
    score = sum([1 for question in correct_answers if user_answers.get(question) == correct_answers[question]])
    
    if score >= 7:
        if name.strip().lower() == "ahona ayan":
            st.success("Congratulations, Ahona Ayan! You got most answers correct! 🎉")
            time.sleep(1)
            
            love_letter = """
**Hey Ahona,**

I’ve been meaning to say something for a while now, but I never found the right words.
Today, I just want to be completely honest with you.

From the first time I saw you at the Unwind event, I felt something different.
I still remember that magical night—how we talked, laughed, and shared those unforgettable moments.
Your smile lit up my world and every moment since has been a cherished memory.

With every conversation and every shared experience,
I found myself drawn closer to you.
From our spontaneous chats to the quiet moments,
every memory with you is etched in my heart.

You make me happy in a way that's hard to put into words.
When I'm with you everything else fades away.
My worries, my stress, my tension all disappear with you—I feel comfortable, understood, and truly myself.
And that's something rare.

Ek geet suna tha maine kabhi,
Teri awaaz mein basi thi koi baat naye si.
Bas ek pal ko laga, kya ye ek ishaara tha?
Ya sirf ek geet, jo yuhi guzara tha?

Mera dil ghabrata hai, ek ajeeb sa darr hai,
Kahin kho na doon tujhe, ye khayal bhi zahar hai.
Main sawalon mein uljha, tu khamosh si khadi,
Kya sach mein tere dil ki ek kasak bhi hai badi?

Har shaam guzar jaati hai ek umeed ke saath,
Ki kabhi toh aayega tera ek shabdon ka haath.
Koi ek jawab, koi ek izhaar,
Ki haan, tu bhi karti hai mujhse pyaar.

I must admit, I was hesitant at first, unsure if I should express these feelings.
But now, with all the certainty in my heart, I know that you are incredibly special to me.
So here I am, laying my heart bare, hoping that you can feel the warmth and sincerity behind these words.
            """
            for line in love_letter.split("\n"):
                st.write(line)
                time.sleep(0.2)
            
            # Feedback & Response Section
            st.subheader("Your Thoughts, Ahona")
            feedback = st.radio(
                "How did the letter make you feel?",
                ["Select an option", "Overwhelmed with joy", "Touched and moved", "Surprised", "I need some time to process"]
            )
            
            response = st.radio("💖 Will you be mine?", ["Select an option", "Yes, I would love to!", "I need time to think...", "I'm sorry, but no."])
            
            if response == "Yes, I would love to!":
                st.success("You just made me the happiest person in the world! ❤️😍💞")
                st.balloons()
                st.markdown("""
                <div style="font-size: 60px; text-align: center; animation: pulse 2s infinite; color: red;">
                    💖💓💗💞💘
                </div>
                <br>
                <!-- Custom Heart Shape -->
                <div class="heart"></div>
                <style>
                @keyframes pulse {
                  0% { transform: scale(1); }
                  50% { transform: scale(1.2); }
                  100% { transform: scale(1); }
                }
                .heart {
                  position: relative;
                  width: 100px;
                  height: 90px;
                  margin: 20px auto;
                }
                .heart:before,
                .heart:after {
                  content: \"\";\n                  position: absolute;\n                  width: 50px;\n                  height: 80px;\n                  background: red;\n                  border-radius: 50px 50px 0 0;\n                }\n                .heart:before {\n                  left: 50px;\n                  top: 0;\n                  transform: rotate(-45deg);\n                  transform-origin: 0 100%;\n                }\n                .heart:after {\n                  left: 0;\n                  top: 0;\n                  transform: rotate(45deg);\n                  transform-origin: 100% 100%;\n                }\n                </style>\n                """, unsafe_allow_html=True)
            elif response == "I need time to think...":
                st.warning("Take your time, Ahona. No matter what, you’ll always be special to me. 😊")
            else:
                st.error("I respect your decision. No matter what, you’ll always be cherished. 💖")
        else:
            st.warning("This experience is reserved for a very special person named Ahona Ayan. Thank you for participating!")
    else:
        st.error("Oops! You need at least 7 correct answers to proceed. Please try again! 💡")
else:
    st.info("Please enter your name to begin the experience.")
