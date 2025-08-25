import requests
import streamlit as st

def get_openai_response(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']['content']

# def get_ollama_response(input_text):
#     response=requests.post(
#     "http://localhost:8000/poem/invoke",
#     json={'input':{'topic':input_text}})

#     return response.json()['output']

#     ## streamlit framework
def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke",
        json={'input': {'topic': input_text}}
    )
    
    # Debug: print the entire response to see its structure
    print("Full response:", response.json())
    print("Status code:", response.status_code)
    
    return response.json()  # Return the full response for inspection


st.title('Langchain Demo With LLAMA2 API')
input_text=st.text_input("Write an essay on")
input_text1=st.text_input("Write a poem on")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))