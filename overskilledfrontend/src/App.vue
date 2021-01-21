<template>
  <div id="app">
    <div class="app_header" sticky>
      <b-navbar toggleable="lg" class='navbar' sticky>
        <b-navbar-brand href="/home" id="logo">
          <span id="brandname1">overski</span><span id="brandname2">lled.io</span>
        </b-navbar-brand>
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
        <div id="app_header_content_text">Python-Everything Board</div>
        <p>The number one place to find python jobs, competitions, and useful
          resources to get to the next step</p>
        <br><br>
        <div class='subscribediv'>
          <b-form v-on:submit.prevent="subscribe" class="subscribeform">
            <input ref='subscribeform' v-model="subscribeform.email" id="subscribeinput"
            placeholder="johndoe@anaconda.com"/>
            <button type='submit' id='subscribebtn'>Subscribe</button>
          </b-form>
        </div>
      </div>
      <div class="after_header">
        <div id='post-div'>
          <router-link to="/post">
            <button id='post-btn' type='button'>Post a Job $0.00</button>
          </router-link>
        </div>
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
          window.location.href = '/home'
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
$theme: #666;
$designtheme: #369df1;
$boxshadow: 0px 0px 30px 10px #ddd;
$fontcolor: #555;

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

#brandname {
  color: $theme;
}

#brandname2 {
  color: $designtheme;
}

.navbar {
  // box-shadow: $boxshadow;
  background-color: #fff;
  border-bottom: 1px solid #ddd;
}

#logo {
  color: $theme;
  font-size: 32px;
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
  color: $fontcolor;
  text-align: center;
}

.app_header_content {
  padding-top: 5%;
  padding-bottom: 5%;
  color: #fff;
  text-align: center;
  background-color: $theme;
  height: 400px;
}

#app_header_content_text {
  font-size: 50px;
}

.subscribediv {
  // background-color: #fff;
  padding-left: 10%;
  padding-right: 10%;
}

.subscribeform {
  // max-width: 70%;
  margin-left: auto;
  margin-right: auto;
  border: 1px solid #fff;
  border-radius: 5px;
  background-color:#fff;
  height: 60px;
  padding-top: 5px;
  padding-left: 10px;
  padding-right: 5px;
}

#subscribeinput {
  width: 90%;
  height: 34px;
  padding-top: 6px;
  border: 1px solid #fff;
}
#subscribeinput:focus {
  outline: none;
}

#subscribebtn {
  background-color: $designtheme;
  border: 1px solid $designtheme;
  border-radius: 3px;
  box-shadow: 0px 0px 5px 1px #eee;
  color: #fff;
  font-size: 20px;
  height: 45px;
}
#subscribebtn:focus {
  outline: none;
}

.after_header {
  background-color: #f8f8f8;
  padding-top: 20px;
  padding-bottom: 20px;
}

#post-div {
  // margin-top: 20px;
  margin-bottom: 20px;
  text-align: center;
}

#post-btn {
  width: 20%;
  height: 50px;
  border-radius: 4px;
  background-color: $designtheme;
  border: 2px solid $designtheme;
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
  background-color: #ddd;
  text-align: center;
}

.b-form {
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
}
</style>
