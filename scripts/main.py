import streamlit as st
import optimal as optax
import covid

if __name__ == "__main__":

    st.set_page_config(
        page_title="MARL Market Policy",
        page_icon="🧊",
        initial_sidebar_state="expanded"
    )

    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

    PAGES = {
        "Optimal Tax": optax,
        "COVID-19": covid,
        "Climate": None,
        "Learn More": None,
    }

    st.sidebar.title("Settings")

    model_select = st.sidebar.radio("Select Environment", list(PAGES.keys()))
    st.sidebar.markdown("***")

    iterations = st.sidebar.number_input('Iterations / Steps', value=1000, min_value=1)
    plt_every = st.sidebar.number_input('Plot Every', value=100, min_value=1)
    
    st.sidebar.text("")
    save = st.sidebar.checkbox("Save simulation to gif?")

    page = PAGES[model_select]
    page.model_page(iterations, plt_every, save)
    