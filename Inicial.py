import streamlit as st
import webbrowser

st.title("Perguntas Repp 💊")

QuantidadePropagandistas = st.slider(
    "Sua farmácia tem quantos propagandistas?", 0, 10, None)

if QuantidadePropagandistas == 0:
    ExperienciaPropagandista = st.toggle(
        "Já teve experiência com propagandista?")

    if ExperienciaPropagandista:
        st.text_input("Conte-nos como foi...")
        st.text_input('O que espera do propagandista?')
    st.divider()
    btn = st.button("Acesse nosso site")
    if btn:
        webbrowser.open_new_tab("https://www.reppmobile.com")


if QuantidadePropagandistas != 0:
    st.text_input(
        'Quantos prescritores seu propagandista tem na carteira?')
    st.text_input(
        'Qual a média diária de visitas que seu propagandista faz?')
    st.radio('Seu propagandista precisa ir até a farmácia para relatar como foram as visitas?',
             ['Sim', 'Não'], index=None)
    st.radio('Você mede o retorno financeiro de cada visita realizada?',
             ['Sim', 'Não'], index=None)
    st.radio('Você considera que tem tempo para gerir o propagandista?',
             ['Sim', 'Não'], index=None)
    st.divider()
    btn = st.button("Acesse nosso site")
    if btn:
        webbrowser.open_new_tab("https://www.reppmobile.com")
