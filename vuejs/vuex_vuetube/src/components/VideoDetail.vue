<template>
  <div>
    <div v-if="Object.keys(selectedVideo).length">
      <iframe 
        :src="videoSrc"
        type="text/html" 
        width="480" 
        height="320"
        frameborder="0"
      >
      </iframe>
      <h4>{{ selectedVideo.snippet.title | unescapeTitle }}</h4>
      <p>{{ selectedVideo.snippet.description }}</p>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import { mapState, mapGetters } from 'vuex'

export default {
  name: 'VideoDetail',
  computed: {
    ...mapState([
      'selectedVideo'
    ]),
    ...mapGetters([
      'videoSrc',
    ]),
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