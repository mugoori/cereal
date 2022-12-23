import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def run_eda_app() :
    st.sidebar.image('https://t1.daumcdn.net/cfile/tistory/237A284258A43F2F34')
    df = pd.read_csv('cereal/cereal.csv')
    # --------------------------- 사이드바 이미지 / 데이터 프레임 불러오기

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

    selected_list = st.multiselect('평점 증감 유무를 알고싶은 컬럼을 선택하세요',column_list2,default='rating')

    if len(selected_list) >= 2 :

        df_corr = df[selected_list].corr()

        fig2 = plt.figure()
        sb.heatmap(data=df_corr,annot=True, fmt='.2f',cmap='coolwarm',vmin=-1,vmax=1,linewidths=0.5,)
        st.pyplot(fig2)
    #------------------------  상관관계

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
    # -------------------  컬럼 별 의미