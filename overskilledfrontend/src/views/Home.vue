<template>
  <div class="home">
    <div id="home_nav">
      <b-icon-arrow-up></b-icon-arrow-up>
      <router-link to="/home/competitions">Competitions</router-link> |
      <!-- <router-link to="/home">Projects</router-link> -->
      <!-- <router-link to="/home/talks">Talks</router-link> | -->
      <router-link to="/home/jobs">Jobs</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped lang="scss">

$theme: #7209b7;

#home_nav {
  // background-color: $theme;
  // border-top: 1px solid #ddd;
  border-bottom: 1px solid #ddd;
  height: 50px;
  line-height: 50px;
  vertical-align: middle;
  color: #000;
  text-align: center;
}

a {
    font-weight: bold;
    color: #000;

    &.router-link-exact-active {
      color: $theme;
    }
  }
</style>
