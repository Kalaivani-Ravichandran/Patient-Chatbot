import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("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")

# Setup OpenAI client
client = OpenAI(api_key=api_key)

# Streamlit UI
st.set_page_config(page_title="TechMate - AI Tech Support")
st.title("🛠️ TechMate – Your AI Tech Support Agent")
st.write("Ask me your technical issues – I’ll try to help!")

user_query = st.text_area("❓ Describe your tech problem:")

if st.button("🧠 Get Help"):
    if not api_key:
        st.error("❌ API key not loaded. Please check your .env file.")
    elif not user_query.strip():
        st.warning("Please enter your question.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o",  # Use "gpt-4o" or "gpt-3.5-turbo"
                    messages=[
                        {"role": "system", "content": "You are a helpful tech support agent. Explain step-by-step, add any terminal commands needed."},
                        {"role": "user", "content": user_query}
                    ],
                    temperature=0.4
                )
                answer = response.choices[0].message.content
                st.success("Here's the solution:")
                st.markdown(answer)
            except Exception as e:
                st.error(f"❌ Error: {e}")
                raise e  # 🔍 print full error in terminal
