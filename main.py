import streamlit as st
from factorial import fact
import os

def load_users():
    if not os.path.exists('users.txt'):
        st.error('File users.txt khong ton tai.')
        return []
    with open('users.txt', encoding='utf-8') as f:
        return [line.strip().lower() for line in f if line.strip()]

def login_page():
    st.title('Dang Nhap')
    username = st.text_input('Nhap ten nguoi dung:').strip().lower()
    if st.button('Dang nhap'):
        if not username:
            st.warning('Vui long nhap ten nguoi dung.')
            return
        st.session_state.username = username
        st.session_state.page = 'calculate_fact' if username in load_users() else 'greet'
        st.rerun()

def calculate_fact():
    st.title('Factorial Calculator')
    st.write(f'Hello, {st.session_state.username}!')
    if st.button('Dang xuat'):
        st.session_state.page = 'login'
        st.rerun()
    st.divider()

    num = st.number_input('Enter a number:', min_value=0, max_value=900)
    if st.button('Tinh giai thua'):
        res = fact(num)
        st.write(f'The factorial of {num} is {res}.')

def greet():
    st.title(f'Sorry, {st.session_state.username}!')
    st.write('Ban khong co quyen truy cap.')
    if st.button('Quay lai dang nhap'):
        st.session_state.page = 'login'
        st.rerun()

def main():
    st.session_state.setdefault('page', 'login')
    st.session_state.setdefault('username', '')

    if st.session_state.page == 'calculate_fact':
        calculate_fact()
    elif st.session_state.page == 'greet':
        greet()
    else:
        login_page()

if __name__ == "__main__":
    main()
