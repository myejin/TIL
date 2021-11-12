<template>
  <div>
    <div class=my-2>
      <span>All Movies: {{allMovies}}</span>
      <span> / Watched Movies: {{watchedMovies}}</span>
      <span> / Unwatched Movies: {{unwatchedMovies}}</span>
    </div>
    <my-List-item
      v-for="(movie, index) in movieList"
      :key="index"
      :idx="index"
      :movie="movie"
    ></my-List-item>
  </div>
</template>

<script>
import MyListItem from '@/components/MyListItem'
import {mapState, mapGetters} from 'vuex'
export default {
  name:'MyList',
  components: {
    MyListItem
  },
  computed: {
    ...mapState([
      'movieList'
    ]),
    ...mapGetters([
      'allMovies',
      'watchedMovies',
      'unwatchedMovies'
    ])
  }
}
</script>

<style>
</style>