<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- <Header msg="get more from us"/> -->
    <div id="home_nav">
      <b-icon-arrow-up></b-icon-arrow-up>
      <router-link to="/home/competitions">Competitions</router-link> |
      <router-link to="/home">Projects</router-link> |
      <!-- <router-link to="/home/talks">Talks</router-link> | -->
      <router-link to="/home/jobs">Jobs</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
// import Header from '@/components/Header.vue'
// import Footer from '@/components/Footer.vue'

export default {
  name: 'Home'
  // components: {
  //   Header
  // }
}
</script>

<style scoped lang="scss">
$theme: #7209b7;
#home_nav {
  background-color: $theme;
  border: 1px solid $theme;
  height: 50px;
  line-height: 50px;
  vertical-align: middle;
  color: #fff;
}

a {
    font-weight: bold;
    color: #fff;

    &.router-link-exact-active {
      color: #f72585;
    }
  }
</style>
