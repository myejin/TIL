<template>
  <div>
    <input 
      @keyup.enter="addTodo"
      v-model.trim="inputData" 
      class="my-3" 
      type="text" 
    >
    <button @click="addTodo">Add</button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data: function () {
    return {
      inputData: '',
    }
  },
  methods: {
    addTodo: function () {
      if(this.inputData.length) {
        this.$store.dispatch("addTodo", this.inputData)        
      this.inputData = ''
      } else {
        alert('할 일을 입력해주세요.')
      }
    }
  }
}
</script>

<style scoped>
.my-3 {
  margin: 1rem 0;
}
</style>