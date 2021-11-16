<template>
  <div>
    <div v-if="!todos.length">해야할 일이 없어요!</div>
    <ul>
      <li v-for="(todo, idx) in todos" :key="idx">
        <span 
          @click="updateTodoStatus(todo)" 
          :class="{ completed: todo.completed }"
        >
        {{ todo.title }}
        </span>
        <button @click="deleteTodo(todo)" class="todo-btn">X</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'TodoList',
  data: function () {
    return {
      todos: null,
    }
  },
  methods: {
    setHeader: function () {
      const token = localStorage.getItem('JWT')
      const header = {
        Authorization: `Bearer ${token}`
      }
      return header 
    },
    getTodos: function () {
      axios({
        method: 'get',
        url: `${SERVER_URL}/todos/`,
        headers: this.setHeader()
      })
      .then(res => {
        this.todos = res.data
      })
    },
    deleteTodo: function (todo) {
      axios({
        method: 'delete',
        url: `${SERVER_URL}/todos/${todo.id}/`,
        headers: this.setHeader()
      })
      .then(res => {
        if (res.status === 204) {
          this.getTodos()
        }
      })
    },
    updateTodoStatus: function (todo) {
      const temp = {
        ...todo,
        completed: !todo.completed
      }
      axios({
        method: 'put',
        url: `${SERVER_URL}/todos/${todo.id}/`,
        headers: this.setHeader(),
        data: temp
      })
      .then(() => {
        todo.completed = !todo.completed
      })
    },
  },
  created: function () {
    this.getTodos()
  }
}
</script>

<style scoped>
  .todo-btn {
    margin-left: 10px;
  }

  .completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
</style>
