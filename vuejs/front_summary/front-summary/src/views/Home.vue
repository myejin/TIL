<template>
  <div>
    <div class="my-5">
      <today-movies></today-movies>
    </div>
    <div class="my-5" style="background-color: beige;">
      <movie-slide></movie-slide>
    </div>
  </div>
</template>

<script>
import TodayMovies from '@/components/home/TodayMovies'
import MovieSlide from '@/components/home/MovieSlide'

  export default {
    name: 'Home',

    components: {
      TodayMovies,
      MovieSlide,
    },
  }
</script>
