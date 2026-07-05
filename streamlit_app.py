
import streamlit as st
import pickle
import pandas as pd

movies_dict = pickle.load(open('movies_dict', 'rb'))
movies =pd.DataFrame(movies_dict)

st.title(   "Content Recommender for Netflix ",text_alignment="center" )

st.markdown("""
    <style>
    [data-testid="stWidgetLabel"] p {
        font-size: 1.75rem;
    }
    </style>
""", unsafe_allow_html=True)

#  Adding option to select the movie
selected_movie= st.selectbox("Select a Movie", movies['title'].values)

# importing a file named "similar"
similar =pickle.load(open("similar","rb"))
# def recommend(selected_movie):
#         index = movies[movies['title'] == selected_movie].index[0]

#         distance = similar[index]

#         movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
#         l =[]
#         duration =[]
#         year =[]
#         for j in movies_list:
#             l.append(movies.iloc[j[0]].title)
#             duration.append(movies.iloc[j[0]].duration)
#             year.append(movies.iloc[j[0]].release_year)
#         return l,duration,year
def recommend(selected_movie):
    index = movies[movies['title'] == selected_movie].index[0]
    movies_list = similar[index][:5]   #

    l, duration, year = [], [], []
    for j in movies_list:
        l.append(movies.iloc[j[0]].title)
        duration.append(movies.iloc[j[0]].duration)
        year.append(movies.iloc[j[0]].release_year)
    return l, duration, year


if st.button("Recommend", type="primary"):
    st.write("#### You have selected:", selected_movie)
    st.write("#### Based on your interest ")
    rec_content,duration,year  =recommend(selected_movie)

    for k, d,p in zip(rec_content, duration, year):
        col1, col2 ,col3 = st.columns([3, 1,2])  # Movie name gets 3x more space
        with col1:
            st.write(f"#### {k}")
        with col2:
            st.write(f"#### {d}")
        with col3:
            st.write(f"#### {p}")
