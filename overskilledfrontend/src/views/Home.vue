<template>
  <div class="home">
    <div id="home_nav">
      <div class="options_div">
        <!-- <div><b-icon icon="view-stacked" class="options_icon"></b-icon></div> -->
        <div><router-link to="/home/competitions">Competitions</router-link> |</div>
      </div>
      <div class="options_div">
        <!-- <b-icon icon="bullseye" class="options_icon"></b-icon> -->
        <div>| <router-link to="/home">Jobs</router-link></div>
      </div>
    </div>
    <router-view/>
  </div>
</template>

<script>
/* eslint-disable */

import { BIcon, BIconArrowUp, BIconBullseye, BIconViewStacked } from 'bootstrap-vue'
export default {
  name: 'Home',
  components: {
    BIcon,
    BIconArrowUp,
    BIconBullseye,
    BIconViewStacked
  }
}
</script>

<style scoped lang="scss">

$theme: #f8f8f8;
$designtheme: #369df1;

#home_nav {
  display: flex;
  justify-content: center;
  background-color: $theme;
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
      color: $designtheme;
    }
  }

.options_icon {
  width: 30px;
  height: 30px;
  color: $designtheme;
}

@media (hover: hover) and (pointer: fine) {
  .options_div:hover {
    background-color: $designtheme;
    color: #fff;
    .options_icon {
      color: #fff;
    }
  }
}
</style>
