<template>
  <div id="app">
    <div class="app_header" sticky>
      <b-navbar toggleable="lg" sticky>
        <b-navbar-brand href="#" id="logo"><h2>OverSkilled</h2></b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav>

          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-nav-item :active="tab === 1" @click="tab = 1">
              <router-link to="/home" class="header_links">Home</router-link>
            </b-nav-item>
            <b-nav-item :active="tab === 2" @click="tab = 2">
              <router-link to="/about" class="header_links">About</router-link>
            </b-nav-item>
            <!-- <b-nav-item :active="tab === 3" @click="tab = 3">
              <router-link to="/post" class="header_links">Post</router-link>
            </b-nav-item> -->
            <b-nav-item :active="tab === 4" @click="tab = 4">
              <router-link to="/howto" class="header_links">How-To</router-link>
            </b-nav-item>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
      <div class='app_header_content'>
        <span id="app_header_content_text">Make Money with Your Tech Skills</span>
      </div>
    </div>

    <router-view/>

    <div class="app_footer">
      <h1>Contact Us</h1>
      <div>Questions, Complaints, Enquiries</div>
      <b-form class="b-form">
        <b-form-group id="input-group-1">
          <b-form-input v-model="text" placeholder="Email Address"></b-form-input>
          <br>
          <b-form-textarea placeholder="Tell us!"></b-form-textarea>
        </b-form-group>
      </b-form>
      <p>
        <b>OverSkilled</b> was built by Kene Agbo, for the community
        <p> Copyright {{ currentDate.getFullYear() }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      currentDate: new Date()
    }
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400&display=swap');
// $theme : rgba(89, 99, 94, 0.8);
$theme: rgba(230, 230, 230, 1);
// $theme: #fff;

body, html {
  margin: 0;
  padding: 0;
//     font-family: 'Open Sans', sans-serif;
}

div {
  display: block;
}

.app_header {
  background-color: $theme;
  margin: 0;
}

#logo {
  color: #7209b7;
}

#app {
  font-family: 'Open Sans', sans-serif;
  // font-family: Avenir, Helvetica, Arial, sans-serif;
  // -webkit-font-smoothing: antialiased;
  // -moz-osx-font-smoothing: grayscale;
  text-align: center;
  // color: #2c3e50;
  // background-color: #fff;
}

.app_header_tops {
  display: flex;
  flex-direction: row;
  justify-content: left;
}

#app_name {
  font-size: 32px;
  color: #aaa;
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

.app_header_content {
  padding-top: 10%;
  padding-bottom: 10%;
  color: #7209b7;
}

#app_header_content_text {
  font-size: 60px;
}

.header_links {
  color: #fff;
}

.app_footer {
  height: 100px;
  background-color: #ddd;
}

.b-form {
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
}
</style>
