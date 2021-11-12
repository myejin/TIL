<template>
  <div>
    <button @click="pickMovie">Pick Movie</button>
    <br><br>
    <div v-if="Object.keys(movie).length" >
      <img v-if="Object.keys(movie).length" :src="url" alt="movie" height="350">
      <p>{{ movie.title }}</p>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name:'Random',
  data: function () {
    return {
      movie: {}
    }
  },
  methods: {
    pickMovie: function () {
      const movielist = this.$store.state.topMovieList
      this.movie = _.sample(movielist)
    }
  },
  computed: {
    url: function () {
      return `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
    },
  }
}
</script>

<style>

</style>