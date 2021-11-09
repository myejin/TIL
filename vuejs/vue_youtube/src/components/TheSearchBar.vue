<template>
  <div>
    <input type="text" v-model.trim="keyword" @keyup.enter="onSearch">
    <button @click="onSearch">검색</button>
  </div>
</template>

<script>
export default {
  name: 'TheSearchBar',
  data: function () {
    return {
      keyword: null,
    }
  },
  methods: {
    onSearch: function () {
      this.$emit('search', this.keyword)
    }
  }

}
</script>

<style>
</style>