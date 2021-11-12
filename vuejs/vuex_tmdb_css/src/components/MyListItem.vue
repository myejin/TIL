<template>
  <div>
    <div
      class="py-1" 
      :class="{ lightgrey: idx % 2, whitesmoke: !(idx % 2) }"
    >
      <span 
        class="mx-3" 
        :class="{watched: movie.isWatched}" 
        @click="updateMovie(movie)"
      >
      {{movie.title}}
      </span>
      <button @click="deleteMovie(movie)">del</button>
    </div>
  </div>
</template>

<script>
import {mapActions} from 'vuex'
export default {
  name:'MyListItem',
  props: {
    movie: Object,
    idx: Number
  },
  methods: {
    ...mapActions([
      'deleteMovie',
      'updateMovie'
    ])
  }
}
</script>

<style scoped>
.watched {
  text-decoration: line-through;
}

.lightgrey {
  background: lightgrey;
}
.whitesmoke {
  background: whitesmoke;
}
.py-1 {
  padding: 0.3em 0;
}
</style>