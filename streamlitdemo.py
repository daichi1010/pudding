
import streamlit as st
st.title('High&Low')
import random 
button1 = st.button('50High')
if button1:
    num=random.randint(1,100)
    if num>=50:
            st.write('OK')
    elif num<50:
        st.write('NO')
    st.write(num)
button2 = st.button('50Low')
if button2:
    num2=random.randint(1,100)
    if num2>50:
        st.write('NO')
    elif num2<=50:
        st.write('OK')
    st.write(num2)
button3 = st.button('25High')
if button3:
    num3=random.randint(1,100)
    if num3>=25:
            st.write('OK')
    elif num3<25:
        st.write('NO')
    st.write(num3)
button4 = st.button('25Low')
if button4:
    num4=random.randint(1,100)
    if num4>25:
        st.write('NO')
    elif num4<=25:
        st.write('OK')
    st.write(num4)
button5 = st.button('75High')
if button5:
    num5=random.randint(1,100)
    if num5>=75:
            st.write('OK')
    elif num5<75:
        st.write('NO')
    st.write(num5)
button6 = st.button('75Low')
if button6:
    num6=random.randint(1,100)
    if num6>75:
        st.write('NO')
    elif num6<=75:
        st.write('OK')
    st.write(num6)
button7 = st.button('90High')
if button7:
    num7=random.randint(1,100)
    if num7>=90:
            st.write('OK')
    elif num7<90:
        st.write('NO')
    st.write(num7)
button8 = st.button('10Low')
if button8:
    num8=random.randint(1,100)
    if num8>10:
        st.write('NO')
    elif num8<=10:
        st.write('OK')
    st.write(num8)