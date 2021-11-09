<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" v-model="appData">
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
    <br>
    <parent 
      :app-data="appData"
      @child-data-change="childDataGet"
      @parent-data-change="parentDataGet"
    ></parent>
  </div>
</template>

<script>
import Parent from '@/components/Parent.vue'
export default {
  name: 'App',
  components: {
    Parent,
  },
  data: function () {
    return {
      appData: null,
      childData: null,
      parentData: null,
    }
  },
  methods: {
    childDataGet: function (data) {
      this.childData = data
    },
    parentDataGet: function (data) {
      this.parentData = data
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;

  border: 1px solid black;
}
</style>
