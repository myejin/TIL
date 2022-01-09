<template>
  <div>
    <div v-for="video of videos" :key="video.id.videoId">
      <video-list-item :video="video"></video-list-item>
    </div>
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem.vue'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  computed: {
    videos: function () {
      return this.$store.state.queryResult
    }
  }
}
</script>

<style>

</style>