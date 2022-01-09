<template>
  <div @click="selectVideo">
    <hr>
    <img 
      :src="video.snippet.thumbnails.default.url" 
      alt="thumbnail"
    >
    <p>{{ video.snippet.title | unescapeTitle }}</p>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  methods: {
    selectVideo: function () {
      this.$store.dispatch('selectVideo', this.video)
    },
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