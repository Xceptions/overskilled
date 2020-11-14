<template>
  <div class="howto">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- <Header msg="get more from us"/> -->
    <div id="nav">
      <router-link to="/howto/competitions">Ace Competitions</router-link> |
      <router-link to="/howto">Get Projects</router-link> |
      <router-link to="/howto/talks">Get Talks</router-link> |
      <router-link to="/howto/jobs">Get Jobs</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import Header from '@/components/Header.vue'

export default {
  name: 'HowTo',
  components: {
    Header
  }
}
</script>

<style lang="scss">
body {
  // background-color: rgba(230, 230, 230, 0.7);
  background-color: #fff;
}
.nav {
  border: 1px solid red;
}
</style>
