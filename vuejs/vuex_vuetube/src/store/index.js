import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)
const URL = 'https://www.googleapis.com/youtube/v3/search/'

export default new Vuex.Store({
  state: {
    queryResult: Array,
    selectedVideo: Object,
  },
  mutations: {
    SAVE_SEARCH_DATA: function (state, data) {
      state.queryResult = data
    },
    SELECT_VIDEO: function (state, data) {
      state.selectedVideo = data
    }
  },
  actions: {
    searchData: function (context, data) {
      axios({
        method: 'get',
        url: URL,
        params: {
          part: 'snippet',
          q: data,
          type: 'video',
          key: '#',
        }
      })
      .then(res => {
        context.commit('SAVE_SEARCH_DATA', res.data.items)
      })
    },
    selectVideo: function (context, data) {
      context.commit('SELECT_VIDEO', data)
    },
  },
  getters: {
    videoSrc: function (state) {
      const videoId = state.selectedVideo.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  }
})
