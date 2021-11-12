<template>
  <div>
    <h1>Top Movies</h1>
    <div class="row row-cols-2 row-cols-md-3 row-cols-xl-6 g-2 mx-3">
      <movie-card
        v-for="movie of topMovies"
        :key="movie.id"
        :movie="movie"
      ></movie-card>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'

export default {
  name:'Home',
  components: {
    MovieCard
  },
  created: function () {
    this.$store.dispatch('getMovies')
  },
  computed: {
    topMovies: function () {
      return this.$store.state.topMovieList
    }
  }
}
</script>

<style>

</style>