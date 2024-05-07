import hashlib

import streamlit as st

st.set_page_config(page_title="Hash")
st.title("Hash")

algoritmo = st.radio("Algoritmo", ["md5", "sha-1", "sha-2", "sha-3"])

input_text = st.text_input("Escribe aqui")
output_hash = st.caption("")

if input_text:
    print("texto ingresado", input_text)
    myhash = ""
    if algoritmo=="md5":
        myhash = hashlib.md5(input_text.encode()).hexdigest()
    if algoritmo=="sha-1":
        myhash = hashlib.sha1(input_text.encode()).hexdigest()
    if algoritmo=="sha-2":
        myhash = hashlib.sha256(input_text.encode()).hexdigest()
    if algoritmo=="sha-3":
        myhash = hashlib.sha3_384(input_text.encode()).hexdigest()
    output_hash = st.caption("Hash: " + myhash)
