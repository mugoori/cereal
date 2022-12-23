import streamlit as st
import pandas as pd
import numpy as np

def userchoice () :
    df = pd.read_csv('cereal/cereal.csv')
    # ------------------ 데이터 프레임 불러오기
    df.rename(columns={'mfr':'제조사'},inplace=True)
    df.rename(columns={'type':'차갑게/뜨겁게'},inplace=True)
    df.rename(columns={'calories':'칼로리'},inplace=True)
    df.rename(columns={'protein':'단백질'},inplace=True)
    df.rename(columns={'fat':'지방'},inplace=True)
    df.rename(columns={'sodium':'나트륨'},inplace=True)
    df.rename(columns={'fiber':'식이섬유'},inplace=True)
    df.rename(columns={'carbo':'복합 탄수화물'},inplace=True)
    df.rename(columns={'sugars':'설탕'},inplace=True)
    df.rename(columns={'potass':'칼륨'},inplace=True)
    df.rename(columns={'vitamins':'비타민'},inplace=True)
    df.rename(columns={'shelf':'선반'},inplace=True)
    df.rename(columns={'weight':'1인분 무게(온스)'},inplace=True)
    df.rename(columns={'cups':'1회 제공량 (컵수)'},inplace=True)
    df.rename(columns={'rating':'점수'},inplace=True)

    column_list = df.columns[3:]
    # ------------------ 조건 컬럼 만들기

    st.subheader('맞춤 시리얼 찾기!')
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