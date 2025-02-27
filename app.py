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
    
    q1 = st.radio("Where did we first meet?", ["Select an option", "Church", "Office", "Unwind event", "Isha Foundation", "Movie theater"])
    q2 = st.radio("What drink did I ask you about?", ["Select an option", "Soft drink", "Vadka", "Whiskey", "Beer", "Wine"])
    q3 = st.radio("When did I realize I had feelings for you?", ["Select an option", "October 28th", "November 23rd", "December 25th", "January 1st"])
    q4 = st.radio("Which memory makes my heart race the most?", ["Select an option", "Dancing at the Unwind event", "Church", "Strolling at Isha Foundation", "Laughing at the movie theater"])
    q5 = st.radio("What does our journey mean to me?", ["Select an option", "A fleeting moment", "Nothing", "An everlasting memory", "Just a chapter"])
    q6 = st.radio("Which movie did you enjoy watching with me the most?", ["Select an option", "Sanam Teri Kasam", "Chhaava", "Vickey Ka Woh Wala Video"])
    q7 = st.radio("Imagine your life’s theme song. Which of these best describes it?", ["Select an option", "Sweet and smooth like Dard chocolate", "Warm and twisty like noodles", "Deep and dramatic like a sad song"])
    q8 = st.radio("What is the aim of this interactive experience?", ["Select an option", "To unlock a special surprise message", "To test your knowledge", "Just for fun"])
    
    correct_answers = {"q1": "Unwind event", "q2": "Whiskey", "q3": "November 23rd", "q4": "Laughing at the movie theater", "q5": "An everlasting memory", "q6": "Vickey Ka Woh Wala Video", "q7": "Sweet and smooth like Dard chocolate", "q8": "To unlock a special surprise message"}
    user_answers = {"q1": q1, "q2": q2, "q3": q3, "q4": q4, "q5": q5, "q6": q6, "q7": q7, "q8": q8}
    def check_answer(question, options, correct):
        user_answer = st.radio(question, options, key=question)
        user_answers[question] = user_answer
        
        if user_answer != "Select an option":
            if user_answer == correct:
                st.success("✅ Correct!")
            else:
                st.error("❌ Wrong Answer!")
    
    score = sum([1 for key in correct_answers if user_answers[key] == correct_answers[key]])
    
    if score >= 6:
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
            
            # ----------------------------
            # Feedback & Response Section
            # ----------------------------
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
                  content: "";
                  position: absolute;
                  width: 50px;
                  height: 80px;
                  background: red;
                  border-radius: 50px 50px 0 0;
                }
                .heart:before {
                  left: 50px;
                  top: 0;
                  transform: rotate(-45deg);
                  transform-origin: 0 100%;
                }
                .heart:after {
                  left: 0;
                  top: 0;
                  transform: rotate(45deg);
                  transform-origin: 100% 100%;
                }
                </style>
                """, unsafe_allow_html=True)
            elif response == "I need time to think...":
                st.warning("Take your time, Ahona. No matter what, you’ll always be special to me. 😊")
            else:
                st.error("I respect your decision. No matter what, you’ll always be cherished. 💖")
        else:
            st.warning("This experience is reserved for a very special person named Ahona Ayan. Thank you for participating!")
    else:
        st.error("Oops! You need at least 6 correct answers to proceed. Please try again! 💡")
else:
    st.info("Please enter your name to begin the experience.")
