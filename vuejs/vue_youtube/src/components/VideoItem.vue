<template>
  <div @click="videoSelect">
    <hr>
    <img id="thumbnail" 
      :src="video.snippet.thumbnails.default.url" 
      alt="thumbnail"
    >
    <p>{{ video.snippet.title | unescapeTitle }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoItem',
  props: {
    video: Object,
  },
  methods: {
    videoSelect: function () {
      this.$emit('video-select', this.video)
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