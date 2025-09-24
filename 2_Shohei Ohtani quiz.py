import streamlit as st
st.title("Quiz: How well do you know Shohei Ohtani?")

st.image("https://i.ytimg.com/vi/SBa9UlavrRo/maxresdefault.jpg", use_container_width=True)
st.image("https://image-cdn.essentiallysports.com/wp-content/uploads/Shohei-Ohtani-Pitching-Practice.jpg", use_container_width=True)
st.image("https://cf-img-a-in.tosshub.com/lingo/stak/images/story/202502/67b8df6272031-shohei-ohtani-211732462-16x9.jpg", use_container_width=True)

if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "score" not in st.session_state:
    st.session_state.score = 0

# multi select
quiz_questions_multiselect = [
    {
        "question": "Which of the following baseball position(s) does Shohei Ohtani play?",
        "multi_select_choices": ["Pitcher", "First base", "Shortstop", "Designated hitter (DH)"],
        "multi_select_correct": ["Pitcher", "Designated hitter (DH)"],
    }
]

# numerical answer
quiz_questions_numerical = [
    {"question": "How many **home runs** did he hit in 2024?", "answer": 54}, 
    {"question": "How many **bases** did he steal in 2024?", "answer": 59}
]



# multiple choice
quiz_questions_multiplechoice = [
    {
        "question": "Which NPB team did he play for?",
        "choices": ["Chiba Lotte Marines", "Orix Buffaloes", "Hokkaido Nippon-ham Fighters"],
        "correct": "Hokkaido Nippon-ham Fighters",
    },
    {
        "question": "What is his current jersey number with the Dodgers?",
        "choices": ["11", "17", "16",],
        "correct": ["17"],
    },
]

# last question
quiz_questions_allcorrect = [
    {
        "question": "Is he awesome ⚾🦄",
        "choices": ["yes",],
        "allcorrect": ["yes",],
    },
]

all_questions = quiz_questions_multiselect + quiz_questions_numerical + quiz_questions_multiplechoice + quiz_questions_allcorrect
question = all_questions[st.session_state.current_question]
st.subheader(question["question"])

if "choices" in question:
    answer = st.radio("Choose an answer", question["choices"]) #NEW
    if answer == "correct":
        st.session_state.score += 1
    elif answer not in "correct":
        st.session_state.score += 0
elif "answer" in question:
    answer = st.number_input("Write a number:", min_value=0, max_value=100, value=0, step=1), #NEW
    if answer == "answer":
        st.session_state.score += 1
    else:
        st.session_state.score += 0
elif "multi_select_choices" in question:
    answer = st.multiselect("Choose all the right answers", question["multi_select_choices"]) #NEW
    if answer == "multi_select_correct":
        st.session_state.score += 1
    elif answer not in question["multi_select_correct"]:
        st.session_state.score += 0

if st.session_state.current_question < len(all_questions) - 1:
    if st.button("Next ⚾🦄️"):
        st.session_state.current_question += 1
else:
    st.button("Done ⚾🦄️")
    st.write(f"You got {st.session_state.score + 1} out of 6 questions correct")
