import streamlit as st
from factorial import fact
import os

def load_users():
    if not os.path.exists('users.txt'):
        st.error('File users.txt khong ton tai')
        return []
    with open('users.txt', encoding='utf-8') as f:
        return [line.strip().lower() for line in f if line.strip()]

def login_page():
    st.title('Dang nhap')
    usrname = st.text_input('Nhap ten nguoi dung:').strip().lower()
    if st.button('Dang nhap'):
        if not usrname:
            st.warning('Vui long nhap ten nguoi dung!')
            return
        st.session_state.usrname = usrname
        st.session_state.page = 'calc' if usrname in load_users() else 'greeting'
        st.rerun()

def cal_fact():
    st.title('Factorial Calculator')
    st.write(f'Xin chao, {st.session_state.usrname}')
    if st.button('Dang xuat'):
        st.session_state.page = 'login'
        st.rerun()
    st.divider()

    number = st.number_input(
            "Enter a number:",
            min_value=0,
            max_value=900
        )
    if st.button("Calculate"):
        res = fact(number)
        st.write(f"The factorial of {number} is {res}.")

def greeting_page():
    st.title(f'Xin chao {st.session_state.usrname}!')
    st.write('Ban khong co quyen truy cap.')
    if st.button('Quay lai dang nhap'):
        st.session_state.page = 'login'
        st.rerun()

def main():
    st.session_state.setdefault('page', 'login')
    st.session_state.setdefault('usrname', '')

    if st.session_state.page == 'calc':
        cal_fact()
    elif st.session_state.page == 'greeting':
        greeting_page()
    else:
        login_page()
    
    


if __name__ == "__main__":
    main()
