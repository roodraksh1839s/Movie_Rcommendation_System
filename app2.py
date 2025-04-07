import pickle
import pandas as pd
import streamlit as st 

import requests

data = pickle.load(open('data_dict.pkl',mode='rb'))
data = pd.DataFrame(data)

similarity = pickle.load(open('Similarity.pkl',mode='rb'))

st.header("_Movie_ :blue[_Recommendation_] :red[_System_]")
st.subheader('Find your next favorite movie!')

select_values = st.selectbox("Select movie from dropdown", data['title'].values)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path'] 
    full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path


def recommend(movie):
    index = data[data['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie=[]
    recommend_poster=[]
    
    
    for i in distance[0:6]:
        movies_id = data.iloc[i[0]].id
        recommend_movie.append(data.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    
    return recommend_movie, recommend_poster

if st.button("Recommend"):
    movie_name, movies_poster = recommend(select_values)
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.text(movie_name[0])
        st.image(movies_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movies_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movies_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movies_poster[3])
    with col5:
        st.text(movie_name[4])  
        st.image(movies_poster[4])
    with col6:
        st.text(movie_name[5])
        st.image(movies_poster[5])
        
    