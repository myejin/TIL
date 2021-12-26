<template>
  <div>
    <v-carousel
      cycle
      height="500"
      hide-delimiter-background
      show-arrows-on-hover
    >
      <v-carousel-item
        v-for="(src, i) in movieSrc"
        :key="i"
        :src="src"
      >
      </v-carousel-item>
    </v-carousel>
  </div>
</template>

<script>
  export default {
    name: 'TodayMovies',

    data: () => ({
      movieSrc: [
        require('@/assets/todaymovies/spiderman.jpg'),
        require('@/assets/todaymovies/harrypotter.jpg')
      ],
    }),
  }
</script>
