<template>
  <div id="parent">
    <h1>AppParent</h1>
    <input type="text" v-model="parentData" @keyup="parentDataChange">
    <p>appData: {{ appData }}</p>
    <p>childData: {{ childData }}</p>
    <br>
    <child 
      :app-data="appData" 
      :parent-data="parentData"
      @child-data-change="childDataGet"
    ></child>
  </div>
</template>

<script>
import Child from '@/components/Child.vue'
export default {
  name: 'Parent',
  components: {
    Child,
  },
  data: function () {
    return {
      parentData: null,
      childData: null,
    }
  },
  props: {
    appData: String,
  },
  methods: {
    childDataGet: function (data) {
      this.childData = data
      this.$emit('child-data-change', this.childData)
    },
    parentDataChange: function () {
      this.$emit('parent-data-change', this.parentData)
    }
  }
}
</script>

<style>
#parent {
  border: 1px solid red;
}
</style>