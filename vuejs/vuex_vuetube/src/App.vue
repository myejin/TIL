<template>
  <div id="app">
    <the-search-bar></the-search-bar>
    <video-detail></video-detail>
    <video-list></video-list>
  </div>
</template>

<script>
import TheSearchBar from './components/TheSearchBar.vue'
import VideoDetail from './components/VideoDetail.vue'
import VideoList from './components/VideoList.vue'

export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoDetail,
    VideoList,
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
