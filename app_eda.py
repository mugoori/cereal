import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import platform
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

def run_eda_app() :
    st.sidebar.image('https://t1.daumcdn.net/cfile/tistory/237A284258A43F2F34')
    df = pd.read_csv('cereal/cereal.csv')
    # --------------------------- 사이드바 이미지 / 데이터 프레임 불러오기

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
    # --------------------------- 컬럼 이름 수정

    st.subheader('사용된 데이터 프레임 및 기초 통계')
    show_df = st.checkbox('사용된 데이터 프레임')
    if show_df :
        st.dataframe(df.head(5))
    show_df2 = st.checkbox('기초 통계')
    if show_df2 :
        st.dataframe(df.describe())
    # ----------------------------  데이터 프레임 / 기초 통계 보여주기

    column_list = df.columns[1:-1]
    column_list2 = df.columns[:]
    st.subheader('컬럼 별 히스토그램')

    histogram_column = st.selectbox('히스토그램 확인할 컬럼을 선택하세요.',column_list)
    my_bins = st.number_input('빈의 갯수를 입력하세요', 10, 30, value=10, step=1)

    fig1 = plt.figure()
    plt.hist(data=df , x= histogram_column, rwidth=0.8, bins=my_bins)
    plt.title(histogram_column+' Histogram')
    plt.xlabel(histogram_column)
    plt.ylabel('Count')
    st.pyplot(fig1)
    #--------------------------- 컬럼 별 히스토그램

    st.subheader('상관 관계 분석')

    selected_list = st.multiselect('평점 증감 유무를 알고싶은 컬럼을 선택하세요',column_list2,default='점수')

    if len(selected_list) >= 2 :

        df_corr = df[selected_list].corr()

        fig2 = plt.figure()
        sb.heatmap(data=df_corr,annot=True, fmt='.2f',cmap='coolwarm',vmin=-1,vmax=1,linewidths=0.5,)
        st.pyplot(fig2)
    #------------------------  상관관계