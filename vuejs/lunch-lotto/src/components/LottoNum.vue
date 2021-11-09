<template>
  <div>
    <h1>로또</h1>
    <button @click="getNum">Get Lucky Numbers</button>
    <p v-if="selectedNums.length">{{ selectedNums }}</p>
    <br>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'TheLunch',
  data: function () {
    return {
      selectedNums: [],
    }
  },
  methods: {
    getNum: function() {
      this.selectedNums = _.sampleSize(_.range(1, 46), 6)
    }
  }
}
</script>
