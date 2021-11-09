<template>
  <div>
    <h1>점심메뉴</h1>
    <button @click="getMenu">Pick Lunch</button>
    <p>{{ selectedMenu }}</p>
    <br>
    <h2>로또를 뽑아보자</h2>
    <button @click="goLottoPage">Pick Lotto</button>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'TheLunch',
  props: {
    // msg: String
  },
  data: function () {
    return {
      menuList: ['국밥', '치킨', '떡볶이', '피자'],
      selectedMenu: '',
    }
  },
  methods: {
    getMenu: function() {
      this.selectedMenu = _.sample(this.menuList)
    },
    goLottoPage: function() {
      this.$router.push({ name: 'TheLotto' })
    }
  }
}
</script>
