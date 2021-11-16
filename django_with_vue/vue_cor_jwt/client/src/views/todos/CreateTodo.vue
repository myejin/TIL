<template>
  <div>
    <input 
      type="text" 
      v-model="title" 
      @keyup.enter="createTodo"
    >
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
import axios from'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: null,
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
    createTodo: function () {
      axios({
        method: 'post',
        url: `${SERVER_URL}/todos/`,
        headers: this.setHeader(),
        data: {
          title: this.title,
        }
      })
      .then(() => {
        this.$router.push({name:'TodoList'})
      })
    }
  }
}
</script>
