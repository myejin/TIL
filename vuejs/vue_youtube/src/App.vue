<template>
  <div id="app">
    <the-search-bar @search="requestYoutube"></the-search-bar>
    <br>
    <video-detail :video="selectedVideo"></video-detail>
    <video-list 
      :videos="results"
      @video-select="videoSelect"
    >
    </video-list>
  </div>
</template>

<script>
import axios from 'axios'
import TheSearchBar from '@/components/TheSearchBar.vue'
import VideoList from '@/components/VideoList.vue'
import VideoDetail from '@/components/VideoDetail.vue'

const URL = 'https://www.googleapis.com/youtube/v3/search/'
export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail,
  },
  data: function () {
    return {
      results: [],
      selectedVideo: {},
    }
  },
  methods: {
    requestYoutube: function (data) {
      axios({
        method: 'get',
        url: URL,
        params: {
          part: 'snippet',
          q: data,
          type: 'video',
          key: process.env.VUE_APP_YOUTUBE_KEY,
        }
      })
      .then(res => {
        this.results = res.data.items
        this.selectedVideo = res.data.items[0]
      })
    },
    videoSelect: function (video) {
      this.selectedVideo = video
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
