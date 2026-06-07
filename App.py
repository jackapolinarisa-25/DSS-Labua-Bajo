import streamlit as st

from graph import graph
from dijkstra import dijkstra

st.title("DSS Wisata Labuan Bajo")

start = st.selectbox(
    "Pilih Lokasi Awal",
    list(graph.keys())
)

if st.button("Cari Rekomendasi"):

    result = dijkstra(graph, start)

    st.subheader("Hasil Perhitungan")

    for tempat, jarak in result.items():
        st.write(
            f"{tempat} : {jarak} km"
        )
