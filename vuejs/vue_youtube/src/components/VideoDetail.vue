<template>
  <div v-if="Object.keys(video).length">
    <iframe 
      :src="getUrl"
      type="text/html" 
      width="480" 
      height="320"
      frameborder="0"
    >
    </iframe>
    <h4>{{ video.snippet.title | unescapeTitle }}</h4>
    <p>{{ video.snippet.description }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoDetail',
  props: {
    video: Object,
  },
  computed: {
    getUrl: function () {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  },
  filters: {
    unescapeTitle: function (title) {
      return _.unescape(title)
    }
  }
}
</script>

<style>
</style>