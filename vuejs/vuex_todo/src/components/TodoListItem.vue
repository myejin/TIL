<template>
  <div>
    <span class="mx-3" :class="{ completed: todo.isCompleted }" @click="updateTodo">{{ todo.content }}</span>
    <button @click="deleteTodo">Delete</button>
  </div>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  },
  methods: {
    updateTodo: function () {
      this.$store.dispatch('updateTodo', this.todo)
    },
    deleteTodo: function () {
      this.$store.dispatch('deleteTodo', this.todo)
    }
  },
}
</script>

<style scoped>
.mx-3 {
  margin: 0 1rem;
}
.completed {
  text-decoration: line-through;
}
</style>