import streamlit as st
from sims import optimal as optax
#import covid

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
        #"COVID-19": covid,
        "Climate": None,
        "Learn More": None,
    }

    st.sidebar.title("Settings")
    model_select = st.sidebar.radio("Select Environment", list(PAGES.keys()))

    st.sidebar.markdown("***")
    animate = st.sidebar.checkbox("Animate Simulation?", value=True)
    iterations = st.sidebar.number_input('Iterations / Steps', value=1000, min_value=1, disabled=(not animate))
    plt_every = st.sidebar.number_input('Plot Every', value=100, min_value=1, disabled=(not animate))
    save = st.sidebar.checkbox("Save simulation to gif?", value=False, disabled=(not animate))

    st.sidebar.text("")
    num_agents = st.sidebar.number_input('Number of Agents', value=4, min_value=2)


    page = PAGES[model_select]
    page.sim_page(iterations, animate, plt_every, num_agents, save)
    