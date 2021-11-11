import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todoList: [],
  },
  mutations: {
    ADD_TODO: function (state, data) {
      const todo = {
        content: data,
        isCompleted: false,
      }
      state.todoList.push(todo)
    },
    UPDATE_TODO: function (state, data) {
      state.todoList = state.todoList.map(todo => {
        if(todo === data) {
          const temp = {
            ...todo,
            isCompleted: !todo.isCompleted
          }
          return temp
        } else {
          return todo
        }
      })
    },
    DELETE_TODO: function (state, data) {
      const idx = state.todoList.indexOf(data)
      state.todoList.splice(idx, 1)
    }
  },
  actions: {
    addTodo: function(context, data) {
      context.commit('ADD_TODO', data)
    },
    updateTodo: function (context, data) {
      context.commit('UPDATE_TODO', data)
    },
    deleteTodo: function (context, data) {
      context.commit('DELETE_TODO', data)
    }
  },
  getters: { // Vuex 의 computed 역할
    allTodoCnt: function (state) {
      return state.todoList.length
    },
    completedTodoCnt: function (state) {
      const temp = state.todoList.filter(todo => {
        return todo.isCompleted
      })
      return temp.length
    },
    unCompletedTodoCnt: function (state) {
      const temp = state.todoList.filter(todo => {
        return !todo.isCompleted
      })
      return temp.length
    }
  },
  modules: {
  }
})
