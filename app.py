
import google.generativeai as genai
import streamlit as st

# Configure the generative model
GOOGLE_API_KEY = "my dummy key"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def main():
    st.title("AI Code Reviewer")
    
    st.markdown("---")
    
    st.sidebar.title("Options")
    st.sidebar.write("Customize your review")
    
    code = st.text_area("Enter your Python code for review:", height=300)
    
    st.markdown("---")
    
    if st.button("Review Code"):
        with st.spinner("Analyzing..."):
            response = model.generate_content(f"This Python code snippet potentially contains bugs or areas for improvement:\n\n```python\n{code}\n```\nPlease identify potential issues and suggest fixes, including code snippets demonstrating the improvements.")
            
            st.markdown("---")
            st.subheader("Review Results:")
            st.write(response.text)

if __name__ == "__main__":
    main()


