import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    index_of_movie_name = movies[movies['title'] == movie]['index'].values[0]
    similarity_score = list(enumerate(similarity[index_of_movie_name]))
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    print('Movies Recommended based on your favourite movie:')
    i = 1
    recommended_movies = []
    for movie_name in sorted_similar_movies:
        index = movie_name[0]
        movie_name_recommended = movies[movies['index'] == index]['title'].values[0]
        if i <= 10:
            recommended_movies.append(movie_name_recommended)
            i += 1
    return recommended_movies


movies_list = pickle.load(open('movies_list.pkl', 'rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity_score.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie = st.selectbox(
    'Select Your Favourite movie', movies['title'].values)

if st.button('Recommend'):
    recommendations_list = recommend(selected_movie)
    st.write("Movies Recommended for you:")
    for i in recommendations_list:
        st.write(i)


