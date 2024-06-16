import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    mov_index = final_data[final_data['title'] == movie].index[0]
    distances = similarities[mov_index]
    mov_list = sorted(list(enumerate(distances)),
                      reverse=True, key=lambda x: x[1])[1:15]

    recommended_movies = []
    for i in mov_list:
        movie_id = i[0]
        #fetch poster using api
        recommended_movies.append(final_data.iloc[i[0]].title)
    return recommended_movies

final_data = pickle.load(open('final_df.pkl', 'rb'))
print(final_data)
movies_name = final_data['title'].values
# print(movies_name)

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
print(movies_dict)
similarities = pickle.load(open('similarities.pkl', 'rb'))
print(similarities)

st.title("Movie Recommender System")

option = st.selectbox(
    'Select Movie which you have watched:',
    movies_name
)

if st.button('Recommend'):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)
