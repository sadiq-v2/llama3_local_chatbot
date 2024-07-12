import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain.schema import HumanMessage

# Initialize LLM model
# llm = ChatOllama(model="llama3")

llm = ChatOllama(model="llama3")

# Define a function to get global answers
def get_global_answer(question):
    return llm.invoke([HumanMessage(content=question)])

def main():
    st.title("LLM Chat Application")

    # Create a text input for user queries
    global_query = st.text_area("Enter your question:", height=200)

    if st.button("Get Answer"):
        # Ensure query is not empty
        if global_query:
            # Get global answer
            global_answer = get_global_answer(global_query)
            st.write("Answer:", global_answer)
        else:
            st.write("Please enter a question.")

if __name__ == "__main__":
    main()
