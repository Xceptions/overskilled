<template>
  <div id="app">
    <div class="app_header" sticky>
      <b-navbar toggleable="lg" class='navbar' sticky>
        <b-navbar-brand href="/home" id="logo"><span>overskilled.io</span></b-navbar-brand>
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
            <b-nav-item :active="tab === 3" @click="tab = 3">
              <router-link to="/post" class="header_links">Post</router-link>
            </b-nav-item>
            <b-nav-item :active="tab === 4" @click="tab = 4">
              <router-link to="/howto" class="header_links">How-To</router-link>
            </b-nav-item>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
      <div class='app_header_content'>
        <div id="app_header_content_text">Python-Based Projects</div>
        <b>The number one place to find work from home projects</b>
        <b-form v-on:submit.prevent="subscribe" class="b-form">
          <b-form-input v-model="subscribeform.email"></b-form-input>
          <b-button type='submit' variant="primary">Subscribe</b-button>
        </b-form>
      </div>
      <div id='post-div'>
        <router-link to="/post">
          <button id='post-btn' type='button'>Post a Project $0.00</button>
        </router-link>
      </div>
      <router-view/>
    </div>

    <div class="app_footer">
      <h2>Contact Us</h2>
      <div>Questions, Complaints, Enquiries</div>
      <b-form  v-on:submit.prevent="contactus" class="b-form">
        <b-form-group id="input-group-1">
          <b-form-input v-model="contactusform.email" placeholder="Email Address"></b-form-input>
          <br>
          <b-form-textarea v-model="contactusform.message" placeholder="Tell us!" rows='7'></b-form-textarea>
          <br>
        </b-form-group>
        <b-button type='submit' variant='danger' size="lg">Submit</b-button>
      </b-form>
      <p>We typically reply in less than 24 hours, so expect us!</p>
      <b>overskilled.io</b> was built by Kene Agbo, for the community
      <div> Copyright {{ currentDate.getFullYear() }}</div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data () {
    return {
      currentDate: new Date(),
      subscribeform: {
        email: ''
      },
      contactusform: {
        email: '',
        message: ''
      }
    }
  },
  methods: {
    subscribe () {
      axios.post('http://127.0.0.1:8000/subscribe', this.subscribeform)
        .then((res) => {
          window.alert('subscribed!')
        })
        .catch((err) => {
          console.log(err)
          alert('unable to subscribe for email alerts. Please try again later...')
        })
    },
    contactus () {
      axios.post('http://127.0.0.1:8000/contactus', this.contactusform)
        .then((res) => {
          window.alert('Message received. Will revert in due time!')
        })
        .catch((err) => {
          alert(err)
          // alert('unable to reach us. Please try again later...')
        })
    }
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400&display=swap');
$theme: #7209b7;
$boxshadow: 0px 0px 30px 10px #ddd;

body, html {
  margin: 0;
  padding: 0;
  font-family: 'Open Sans', sans-serif;
}

div {
  display: block;
}

.app_header {
  margin: 0;
}

.navbar {
  // box-shadow: $boxshadow;
  background-color: #fff;
  border-bottom: 1px solid #ddd;
}

#logo {
  color: $theme;
  font-size: 42px;
  text-shadow: 2px 2px #eef;
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

.header_links {
  color: #333;
  font-weight: bold;
  text-align: center;
}

.app_header_content {
  padding-top: 5%;
  padding-bottom: 5%;
  color: #fff;
  text-align: center;
  background-color: $theme;
}

#app_header_content_text {
  font-size: 60px;
}

#subscribe_input {
  margin-top: 30px;
  width: 300px;
  border-radius: 4px;
  border: 2px solid #fff;
}

#post-div {
  margin-top: 20px;
  margin-bottom: 20px;
  text-align: center;
}

#post-btn {
  width: 30%;
  height: 50px;
  border-radius: 4px;
  background-color: $theme;
  border: 2px solid $theme;
  font-weight: bold;
  color: #fff;
}

@media (hover: hover) and (pointer: fine) {
  #post-btn:hover {
    box-shadow: $boxshadow;
    background-color: #fff;
    color: #000;
  }
}

.app_footer {
  margin-top: 10px;
  // height: 100px;
  background-color: #ddd;
  text-align: center;
}

.b-form {
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
}
</style>
