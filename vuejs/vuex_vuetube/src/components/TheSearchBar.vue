<template>
  <div class="my-3">
    <input type="text" @keyup.enter="searchData" v-model.trim="inputData">
    <button @click="searchData">검색</button>
  </div>
</template>

<script>
export default {
  name: 'TheSearchBar',
  data: function () {
    return {
      inputData: '',
    }
  },
  methods: {
    searchData: function () {
      this.$store.dispatch('searchData', this.inputData)
    }
  }
}
</script>

<style scoped>
.my-3 {
  margin: 1rem 0;
}
</style>