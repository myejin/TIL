<template>
  <div>
    <video-item v-for="video of videos" 
      :key="video.id.videoId" 
      :video="video"
      @video-select="videoSelect"
    >
    </video-item>
  </div>
</template>

<script>
import VideoItem from '@/components/VideoItem.vue'
export default {
  name: 'VideoList',
  components: {
    VideoItem
  },
  props: {
    videos: Array,
  },
  methods: {
    videoSelect: function (video) {
      this.$emit('video-select', video)
    }
  }
}
</script>

<style>
</style>