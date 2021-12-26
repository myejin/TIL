<template>
  <v-container>
    <h1 class="mx-5">Movie Slide</h1>
    <v-slide-group
      show-arrows
      class="pa-4 mx-auto"
      style="width:100%;"
    >
      <v-slide-item
        v-for="(src, i) in movieSrc"
        :key="i"
      >
        <v-card
          width="240"
          height="200"
          style="margin: 0 0.5rem;"
        >
          <v-img
            class="white--text align-end"
            :src="src"
            gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
          />
          <v-card-title  class="cardTitle  font-style">
            <v-spacer />
            <div class="cardTitlee">{{ src }}</div>
            <v-spacer />
          </v-card-title>
        </v-card>
      </v-slide-item>
    </v-slide-group>
  </v-container>
</template>

<script>
  export default {
    name: 'MovieSlide',

    data: () => ({
      movieSrc: [
        require('@/assets/todaymovies/spiderman.jpg'),
        require('@/assets/todaymovies/harrypotter.jpg'),
        require('@/assets/todaymovies/spiderman.jpg'),
        require('@/assets/todaymovies/harrypotter.jpg'),
        require('@/assets/todaymovies/spiderman.jpg'),
        require('@/assets/todaymovies/harrypotter.jpg')
      ],
    }),
  }
</script>
