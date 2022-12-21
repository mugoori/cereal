import streamlit as st
from app_home import run_home_app
from app_eda import run_eda_app
from userchoice import userchoice

def main() :
    st.title('원하는 시리얼을 찾아보자')

    menu = ['Home','EDA','userchoice']
    choice = st.sidebar.selectbox('메뉴',menu)
    
    if choice == 'Home' :
        run_home_app()
    if choice == 'EDA' :
        run_eda_app()
    if choice == 'userchoice' :
        userchoice()

if __name__ == '__main__' :
    main()