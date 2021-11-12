<template>
  <div class="col">
    <b-card
      class="mb-2"
      :title="movie.title"
      :img-src="url"
      img-alt="Movie Image"
    >
      <b-card-text class="card-text">
        {{movie.overview}}
      </b-card-text>
    </b-card>
  </div>
</template>

<script>
export default {
  name:'MovieCard',
  props: {
    movie: Object
  },
  computed: {
    url: function () {
      return `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
    }
  }
}
</script>

<style>
.card-text {
  font-size:15px;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
</style>