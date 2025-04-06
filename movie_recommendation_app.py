import streamlit as st
import pandas as pd
import pickle

# Loaad the dataset

data = pickle.load(open('data_dict.pkl',mode='rb'))
data = pd.DataFrame(data)

# print(data)

similarity = pickle.load(open('Similarity.pkl',mode='rb'))


def recommend(movie):
    movie_index = data[data['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    # recommended_movies_posters = []

    for i in movie_list:
        movie_id = i[0]
        recommended_movies.append(data.iloc[movie_id]['title'])
        # recommended_movies_posters.append(data.iloc[movie_id]['poster_link'])

    return recommended_movies

movies = recommend('Avatar')
# print(movies)

# Streamlit Web App

st.title('_Movie_ :blue[_Recommendation_] :red[_System_]')
st.subheader('Find your next favorite movie!')
st.write('Enter the name of a movie you like, and we will recommend similar movies for you.')
st.write('---')
selected_movie = st.selectbox('Select a movie:', data['title'].values)
btn = st.button("recommend")


if btn:
    recommended_movies = recommend(selected_movie)
    
    for i in recommended_movies:
        st.write(i)
