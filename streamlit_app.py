import streamlit as st
from google import genai

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Gemini AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# =====================================
# GEMINI CLIENT
# =====================================

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("🤖 Gemini AI Assistant")
st.sidebar.write("Built by Vamshi")

mode = st.sidebar.selectbox(
    "Choose Mode",
    [
        "Career Mentor",
        "Python Teacher",
        "Technical Interviewer"
    ]
)

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# =====================================
# MEMORY
# =====================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# =====================================
# STATS
# =====================================

st.sidebar.write(
    f"Messages: {len(st.session_state.messages)}"
)

# =====================================
# DOWNLOAD CHAT
# =====================================

chat_text = ""

for msg in st.session_state.messages:
    chat_text += (
        f"{msg['role']}: "
        f"{msg['content']}\n\n"
    )

st.sidebar.download_button(
    label="📥 Download Chat",
    data=chat_text,
    file_name="chat_history.txt",
    mime="text/plain"
)

# =====================================
# TITLE
# =====================================

st.title("🤖 Gemini AI Assistant")

# =====================================
# SYSTEM PROMPT
# =====================================

if mode == "Career Mentor":

    system_prompt = """
    You are a career mentor.

    Help students with:
    - internships
    - resumes
    - AI careers
    - project guidance

    Give practical advice.
    """

elif mode == "Python Teacher":

    system_prompt = """
    You are a Python teacher.

    Explain concepts simply.

    Always provide:
    - meaning
    - examples
    - beginner friendly explanations
    """

else:

    system_prompt = """
    You are a technical interviewer.

    Ask interview questions.

    Evaluate answers.

    Give feedback and scores.
    """

# =====================================
# SHOW OLD CHAT
# =====================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# =====================================
# USER INPUT
# =====================================

user_input = st.chat_input(
    "Type your message..."
)

# =====================================
# CHAT PROCESSING
# =====================================

if user_input:

    # Save User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    try:

        # Build Full Conversation

        conversation = system_prompt + "\n\n"

        for msg in st.session_state.messages:

            conversation += (
                f"{msg['role']}: "
                f"{msg['content']}\n"
            )

        # Gemini Call

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=conversation
        )

        ai_reply = response.text

        # Save AI Response

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": ai_reply
            }
        )

        # Display AI Response

        with st.chat_message("assistant"):
            st.markdown(ai_reply)

    except Exception as e:

        error_text = str(e)

        if "429" in error_text:

            st.error(
                "⚠️ Quota reached. Wait 30-60 seconds and try again."
            )

        elif "503" in error_text:

            st.error(
                "⚠️ Gemini server busy. Please try again shortly."
            )

        else:

            st.error(
                f"Error: {e}"
            )