import streamlit as st
import pandas as pd
import numpy as np

def userchoice () :
    df = pd.read_csv('cereal/cereal.csv')
    # ------------------ 데이터 프레임 불러오기

    column_list = df.columns[3:]
    # ------------------ 조건 컬럼 만들기

    st.subheader('원하는 조건의 시리얼 찾기')
    choice = st.selectbox('컬럼을 선택하세요',column_list)
    # ------------------ 조건 컬럼 선택하기

    st.text('내림차순')
    st.dataframe(df.sort_values(by=choice,ascending=False).head(10))
    st.text('오름차순')
    st.dataframe(df.sort_values(by=choice,ascending=True).head(10))
    # ------------------ 오름 차순 내림 차순 보여주기

    show_img = st.sidebar.checkbox('평점이 가장 높은 시리얼 TOP3')
    show_img2 = st.sidebar.checkbox('칼로리가 가장 낮은 시리얼 TOP3')
    # ------------------- 사이드에 평점 칼로리 TOP 3 보여주기

    if show_img :
        st.sidebar.image('https://images.kglobalservices.com/www.all-bran.com/en_us/product/product_4508444/kicproductimage-124883_kicproductimage-124883.png')
        st.sidebar.image('https://www.postconsumerbrands.ca/wp-content/uploads/2016/09/shredded-wheat-bran-spoon-size.jpg')
        st.sidebar.image('https://www.postconsumerbrands.ca/wp-content/uploads/2016/09/shredded-wheat-original-spoon-size.jpg')
    if show_img2 :
        st.sidebar.image('https://images.kglobalservices.com/www.all-bran.com/en_us/product/product_4508444/kicproductimage-124883_kicproductimage-124883.png')
        st.sidebar.image('https://i5.walmartimages.com/asr/02280b42-79b7-4d59-bae9-3d9a06ef082f_1.b880653e52f69b76a813cb8075a112fb.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF')
        st.sidebar.image('https://www.kroger.com/product/images/large/back/0003000006410')
    # ----------------- 사이드 평점 칼로리 TOP 3 사진 보여주기
    
    st.subheader('컬럼 별 의미')
    st.text('mfr: 시리얼 제조사')
    st.text('A = American Home Food Products')
    st.text('G = General Mills')
    st.text('K = Kelloggs')
    st.text('N = Nabisco')
    st.text('P = Post')
    st.text('Q = Quaker Oats')
    st.text('R = Ralston Purina')
    st.text('type : c (cold) / h (hot)')
    st.text('cup : 1회 제공량')
    # ------------------ 컬럼 별 의미

