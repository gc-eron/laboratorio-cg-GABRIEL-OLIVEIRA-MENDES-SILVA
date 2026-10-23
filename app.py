import streamlit as st

paginas = [
    st.Page("src/atv1.py", title="Atv1"),
    st.Page("src/atv2.py", title="Atv2"),
]
st.navigation(paginas).run()