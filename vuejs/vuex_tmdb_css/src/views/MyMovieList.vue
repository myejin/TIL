<template>
  <div class="mx-3">
    <div class="bg-blue py-3">
      <h2>My Movie List</h2>
      <my-list-form></my-list-form>
    </div>
    <my-list></my-list>
  </div>
</template>

<script>
import MyListForm from '@/components/MyListForm'
import MyList from '@/components/MyList.vue'

export default {
  name:'MyMovieList',
  components: {
    MyListForm,
    MyList
  }
}
</script>

<style scoped>
.bg-blue {
  background-color: lightblue;
}
.py-3 {
  padding: 1em 0;
}
</style>