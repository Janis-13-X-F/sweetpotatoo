import streamlit as st

st.title("cherrishmylove")
st.write(
    "i love will poulter"
)
st.image("e8cead85c002cf0012be723e98245e47.jpg")
# iniwmanjay


st.tittle("yippieyooi")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
  st.write(f"{angka} adalah Bilangan Genap")
else
  st.write(f"{angka} adalah Bilangan Ganjil")
