import pickle
import streamlit as st
import requests
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",  # required
        options=["Home", "About page", "Contact"],  # required
        icons=["house", "book", "envelope"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
    )

if selected == "Home":
    st.header('Movie Recommender System')
    movies = pickle.load(open('movie_list.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))

    movie_list = movies['title'].values
    selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
    )
    def fetch_poster(movie_id):
        url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path


    def recommend(movie):
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []
        for i in distances[1:6]:
            # fetch the movie poster
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]].title)

        return recommended_movie_names, recommended_movie_posters




    if st.button('Show Recommendation'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
        col1, col2, col3, col4, col5 = st.columns ( 5 )
        with col1:
            st.text(recommended_movie_names[0])
            st.image(recommended_movie_posters[0])
        with col2:
            st.text(recommended_movie_names[1])
            st.image(recommended_movie_posters[1])

        with col3:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
        with col4:
            st.text(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
        with col5:
            st.text(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])

if selected == "About page":
    st.write ( "# Welcome to Movie Recommendation page!" )

    st.sidebar.success ( "Select a demo above." )

    st.markdown (
         """
         A recommendation system filters information by predicting ratings or preferences of customers for items that the customers would like to use. It tries to recommend items to the customers according to their needs and taste.? Select a demo from the sidebar** to see some examples
         of what book Recommendation  can do!
         ### Want to learn more?
         - Check out [Movie recommendation system ](https://medium.com/@amitdlmlai/book-recommendation-system-61bf9284f659)
         - Jump into our [documentation](https://cse.anits.edu.in/projects/projects2021B10.pdf)
         ### See more complex demos
         - DATA SET [Movies Data set](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
         - Project code [github](https://github.com/anilKumar-9/DT-Project)
         """
    )

if selected == "Contact":
    st.write ( "# Project By Batch No:- 13" )
    st.markdown ( "***" )
    st.write ( "## NAME  :   ROLL NUMBER" )
    st.markdown ( "***" )
    st.write ( "#### N.ANIL KUMAR   : 21R11A1243" )
    st.write ( "#### B.DEEPTHI        :21R15A1201" )
    st.write ( "#### M.GANESH       :  21R11A1240" )

