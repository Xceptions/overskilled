<template>
  <div class="app_header">
    <div class='app_header_tops'>
      <div id="app_name">OverSkilled</div>
      <ul id="app_nav">
        <li><router-link to="/home">Home</router-link></li>
        <li><router-link to="/about">About</router-link></li>
        <li><router-link to="/post">Post</router-link></li>
        <li><router-link to="/howto">How-To</router-link></li>
      </ul>
    </div>
    <b-container class="bv-example-row">
      <b-row>
        <b-col>1 of 3</b-col>
        <b-col>2 of 3</b-col>
        <b-col>3 of 3</b-col>
      </b-row>
    </b-container>
    <div class='app_header_content'>
      <div class="app_header_content_writeup">Make Money With Your Tech Skills</div>
      <div>Search box</div>
    </div>
  </div>
  <router-view/>
</template>

<style lang="scss">
// @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400&display=swap');
$theme : #42b983;

body, html {
  margin: 0;
  padding: 0;
//     font-family: 'Open Sans', sans-serif;
}

.app_header {
  background-color: $theme;
  padding: 10px;
}


#app {
  // font-family: 'Open Sans', sans-serif;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: rgba(250, 250, 250, 0.7)
}

.app_header_tops {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

#app_name {
  font-size: 32px;
  color: #fff;
  font-weight: bold;
}

#app_nav {
  display: flex;
  // flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

.app_header_content_writeup {
  margin-top: 20px;
  font-size: 30px;
  font-weight: bold;
  color: #fff;
}
</style>
