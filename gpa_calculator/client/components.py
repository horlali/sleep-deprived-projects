import streamlit as st


def column_sizes():
    col1, col2, col3, col4, col5 = st.columns(
        [
            0.2,
            0.05,
            0.1,
            0.1,
            0.1,
        ]
    )

    return col1, col2, col3, col4, col5


def header_columns():
    col1, col2, col3, col4, col5 = column_sizes()

    with col1:
        st.write("##### Course")

    with col2:
        st.write("##### Elective")

    with col3:
        st.write("##### Grade")

    with col4:
        st.write("##### Credit")

    with col5:
        st.write("##### Grade Point")


def markdown_header(header: str, text: str):
    st.markdown(
        f"<{header} style='text-align: center;'>{text}</{header}>",
        unsafe_allow_html=True,
    )
