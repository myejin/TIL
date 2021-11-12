import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movieList: [],
    topMovieList: []
  },
  mutations: {
    ADD_MOVIE: function(state, data) {
      const movie = {
        title: data,
        isWatched:false
      }
      state.movieList.push(movie)
    },
    DELETE_MOVIE: function(state, data) {
      const index = state.movieList.indexOf(data)
      state.movieList.splice(index, 1)
    },
    UPDATE_MOVIE: function (state, data) {
      state.movieList = state.movieList.map(movie => {
        if (movie === data) {
          const tmp = {
            ...movie,
            isWatched: !movie.isWatched
          }
          return tmp
        } else {
          return movie
        }
      })
    },
    GET_MOVIES: function (state, data) {
      state.topMovieList = data
    }
  },
  actions: {
    addMovie: function ({commit}, data) {
      commit('ADD_MOVIE', data)
    },
    deleteMovie: function ({commit}, data) {
      commit('DELETE_MOVIE', data)
    },
    updateMovie: function ({commit}, data) {
      commit('UPDATE_MOVIE', data)
    },
    getMovies: function ({commit}) {
      axios({
        method: 'get',
        url: 'https://api.themoviedb.org/3/movie/top_rated',
        params: {
          api_key: '[API_KEY]',
          language: 'ko-KR'
        }
      })
      .then(response => {
        commit('GET_MOVIES', response.data.results)
      })
    },
  },
  getters: {
    allMovies: function (state) {
      return state.movieList.length
    },
    watchedMovies: function (state) {
      return state.movieList.filter(movie => {
        return movie.isWatched
      }).length
    },
    unwatchedMovies: function (state) {
      return state.movieList.filter(movie => {
        return !movie.isWatched
      }).length
    },

  }
})
