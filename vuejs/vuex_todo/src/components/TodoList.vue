<template>
  <div>
    <h2>TodoList</h2>
    <h4>All Todos: {{ allTodoCnt }}</h4>
    <h4>Completed Todo: {{ completedTodoCnt }}</h4>
    <h4>Uncompleted Todo: {{ unCompletedTodoCnt }}</h4>
    <todo-list-item
      v-for="(todo, idx) in todoList"
      :key="idx"
      :todo="todo"
    >
    </todo-list-item>
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem.vue'
import { mapState, mapGetters } from 'vuex'
export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  computed: {
    ...mapState([
      'todoList',
    ]),
    ...mapGetters([
      'allTodoCnt',
      'completedTodoCnt',
      'unCompletedTodoCnt',
    ])
  },
}
</script>

<style>

</style>