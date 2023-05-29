import streamlit as st
from streamlit_chat import message
from transformers import pipeline
import torch
from model import generate_text,destinos

#generate_text = pipeline(model="databricks/dolly-v2-3b", torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto")


st.set_page_config(
    page_title="Equipo 5. Vueling chat demo",
    page_icon=":robot:"
)

st.header("Amelia Earhart")

with st.sidebar:
    st.title("Amelia Earhart")
    st.markdown('''
    ## Sobre nosotros
    Este prototipo está creado para el proceso de compra de Vueling. El usuario tiene la capacidad de hacer la pregunta que desee, incluyendo consejos sobre la ciudad 
    que quiere visitar, comparativas sobre dos o más ciudades, planes que hacer en el destino... Además, este chat incluye la compra directa de los vuelos.
    ''')


if 'generated' not in st.session_state:
    st.session_state['generated'] = [f"Estos son los posibles destinos según tus preferencias: {destinos}"]
## past stores User's questions
if 'past' not in st.session_state:
    st.session_state['past'] = ['Hola!']
    

input_container = st.container()
response_container = st.container()

def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text

## Applying the user input box
with input_container:
    user_input = get_text()


def generate_response(prompt):
    response = generate_text(f"{prompt}")
    response = response[0]["generated_text"]
    #response = st.button("Response!")
    return response


with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    for i in range(len(st.session_state['generated'])):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state['generated'][i], key=str(i))

