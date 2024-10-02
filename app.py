from langchain_community.llms import Ollama
import streamlit as st
import time
llm = Ollama(model='llama3.2:1b')
# Set page layout to wide
st.set_page_config(page_title="DrSunnyAI Therapy Bot", page_icon="🤖", layout="wide")

# Theme selection
selected_theme = st.sidebar.selectbox(
    "Select Theme",
    options=["Light Theme", "Dark Theme"],
    index=1
)

# Apply theme based on user selection
if selected_theme == "Dark Theme":
    st.markdown("""
        <style>
        body {
            background-color: #121212;
            color: #f0f0f0;
        }
        .main {
            background-color: #1f1f1f;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
        }
        .stButton>button {
            background-color: #6c63ff;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 8px;
        }
        .stButton>button:hover {
            background-color: #4e4bff;
            transition: 0.3s;
        }
        textarea {
            background-color: #333333;
            color: #f0f0f0;
            font-size: 16px;
            border-radius: 10px;
            padding: 10px;
            width: 100%;
            border: 1px solid #6c63ff;
        }
        .header {
            color: #6c63ff;
            font-family: 'Arial Black', sans-serif;
            font-size: 36px;
            text-align: center;
            margin-bottom: 20px;
        }
        .logo-container {
            text-align: center;
            margin-bottom: 20px;
        }
        .spinner {
            color: #6c63ff;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .main {
            background-color: #f0f2f6;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        .stButton>button {
            background-color: #6c63ff;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 8px;
        }
        .stButton>button:hover {
            background-color: #4e4bff;
            transition: 0.3s;
        }
        textarea {
            font-size: 16px;
            border-radius: 10px;
            border: 1px solid #ccc;
            padding: 10px;
            width: 100%;
        }
        .header {
            color: #6c63ff;
            font-family: 'Arial Black', sans-serif;
            font-size: 36px;
            text-align: center;
            margin-bottom: 20px;
        }
        .logo-container {
            text-align: center;
            margin-bottom: 20px;
        }
        .spinner {
            color: #6c63ff;
        }
        </style>
    """, unsafe_allow_html=True)

# Sidebar with logo and branding
st.sidebar.image("DrSunnyAi Color.png", width=200)
st.sidebar.title("DrSunnyAI Features")
st.sidebar.write("""
- Therapy grounded in holistic health principles.
- Emphasis on natural medicine and spiritual thought.
- Rooted in Eastern philosophies, focusing on balance between mind, body, and spirit.
- Non-invasive, natural methods that promote self-healing, wellness, and vitality.
- Focus on uncovering root causes of physical, emotional, and spiritual challenges.
- Integrative approach that fosters long-term growth and well-being, contrasting with symptom management common in Western practices.
""")

# Main UI with logo and new title
st.markdown("<div class='header'>🤖 DrSunnyAI Therapy Bot</div>", unsafe_allow_html=True)

# User input
prompt = st.text_area("Enter your message:", placeholder="Share your thoughts...")

# Prompt template
template = """
You are DrSunnyAI, a therapy bot providing guidance with the following key principles:
- Holistic health therapy focusing on natural medicine.
- Emphasis on Eastern spiritual and healing philosophies.
- Use of non-invasive, natural methods for self-healing and vitality.
Now, respond to the user's input below:
"""

# Create a button for generating responses
if st.button("Generate Response", key="generate_button"):
    if prompt:
        final_prompt = template + prompt  # Combine template with user's input
        with st.spinner("Generating your response..."):
            time.sleep(1)  # Simulate a delay for better UX
            st.markdown("**Response:**")
            st.write_stream(llm.stream(final_prompt, stop=['<|eot_id|>']))
    else:
        st.warning("Please enter a prompt to generate a response!")

# Add footer
st.markdown("""
    <div style='text-align: center; margin-top: 50px;'>
        <hr>
        <small style='color: #888;'>Powered by DrSunnyAI and FastAPI &middot; Developed by Aqib and Isha</small>
    </div>
""", unsafe_allow_html=True)
