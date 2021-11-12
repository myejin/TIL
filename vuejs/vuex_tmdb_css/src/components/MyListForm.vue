<template>
  <div>
    <input type="text" v-model.trim="inputData" @keyup.enter="addMovie">
    <button @click="addMovie">Add</button>
  </div>
</template>

<script>
export default {
  name:'MyListForm',
  data: function () {
    return {
      inputData: '',
    }
  },
  methods: {
    addMovie: function () {
      if (this.inputData.length) {
        this.$store.dispatch('addMovie', this.inputData)
        this.inputData = ''
      } else {
        alert('영화를 입력해주세요.')
      }
    }
  }
}
</script>

<style>

</style>