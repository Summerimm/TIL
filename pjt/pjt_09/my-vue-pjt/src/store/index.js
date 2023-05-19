import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'

const API_URL = 'https://api.themoviedb.org/3/movie'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: [],
    randomMovie: null,
    movielist: [],
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    GET_RANDOM_MOVIE(state, movies) {
      const randomMovie = movies[Math.floor(Math.random() * movies.length)];
      state.randomMovie = randomMovie
    },

    CREATE_MOVIE(state, movieItem) {
      state.movielist.push(movieItem)
    },
    UPDATE_MOVIE(state, movieItem) {
      state.movielist = state.movielist.map((movie) => {
        if (movie === movieItem) {
          movie.isCompleted = !movie.isCompleted
        }
        return movie
      })
    },
    LOAD_MOVIES(state) {
      const localStorageMovielist = localStorage.getItem('movielist')
      const parsedMovielist = JSON.parse(localStorageMovielist)

      state.movielist = parsedMovielist
    }
  },

  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/top_rated?api_key=05eaffff517bc5c090ca1db21d475be2&language=ko-KR&page=1`
      })
        .then((res) => {
          context.commit('GET_MOVIES', res.data.results)
          context.commit('GET_RANDOM_MOVIE', res.data.results)
        })
        .catch((err) => {
          console.log(err);
        })
    },

    createMovie(context, movieTitle) {
      const movieItem = {
        title: movieTitle,
        isCompleted: false
      }
      context.commit('CREATE_MOVIE', movieItem)
      context.dispatch('saveMoviesToLocalStorage')
    },
    updateMovie(context, movieItem) {
      context.commit('UPDATE_MOVIE', movieItem)
      context.dispatch('saveMoviesToLocalStorage')
    },
    saveMoviesToLocalStorage(context) {
      const jsonMovies = JSON.stringify(context.state.movielist)
      localStorage.setItem('movielist', jsonMovies)
    },
    loadMovies(context) {
      context.commit('LOAD_MOVIES')
    }
  },
  modules: {
  }
})
