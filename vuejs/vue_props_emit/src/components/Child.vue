<template>
  <div id="child">
    <h1>AppChild</h1>
    <input type="text" v-model="childData" @keyup="childDataChange">
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
  </div>
</template>

<script>
export default {
  name: 'Child',
  props: {
    appData: String,
    parentData: String,
  },
  data: function () {
    return {
      childData: null,
    }
  },
  methods: {
    childDataChange: function () {
      this.$emit('child-data-change', this.childData)
    }
  }
}
</script>

<style>
#child {
  border: 1px solid blue;
}
</style>