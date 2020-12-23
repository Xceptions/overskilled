<template>
  <div class="post">
    <div id='post-write-up'>
      <p>Only Python related jobs are allowed</p>
      <h4>Job Postings last for 1 week</h4>
    </div>
    <div class='post-body'>
      <b>Post a Job</b>
      <hr/>
      <b-form v-on:submit.prevent="postJob" class="b-form">
        <b-form-group>
          <label>Header</label>
          <b-form-input v-model="form.job_header"></b-form-input>
        </b-form-group>
        <br>
        <b-form-group>
          <label>Description</label>
          <b-form-textarea v-model="form.job_body"></b-form-textarea>
        </b-form-group>
        <br>
        <b-form-group>
          <label>Company</label>
          <b-form-input v-model="form.company"></b-form-input>
        </b-form-group>
        <br>
        <b-form-group>
          <label>Category</label>
          <b-form-input v-model="form.category"></b-form-input>
        </b-form-group>
        <br>
        <b-form-group>
          <label>Amount</label>
          <b-form-input v-model="form.amount"></b-form-input>
        </b-form-group>
        <!-- <b-form-group>
          <b-form-radio v-model="form.bargain" name="some-radios" value="negotiable">Negotiable</b-form-radio>
          <b-form-radio v-model="form.bargain" name="some-radios" value="fixed">Fixed</b-form-radio>
        </b-form-group> -->
        <br>
        <b-form-group>
          <label>Location</label>
          <b-form-input v-model="form.location"></b-form-input>
        </b-form-group>
        <br>
        <b-form-group>
          <label>Contact (Mail / URL)</label>
          <b-form-input v-model="form.contact_me"></b-form-input>
        </b-form-group>
        <b-button type='submit' variant="success">Post Project</b-button>
      </b-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Post',
  data () {
    return {
      selectedFile: null,
      form: {
        job_header: '',
        job_body: '',
        company: '',
        category: '',
        amount: '',
        location: '',
        contact_me: ''
      }
    }
  },
  methods: {
    postJob () {
      axios.post('http://127.0.0.1:8000/viewjobs', this.form)
        .then((res) => {
          window.location.href = '/home'
        })
        .catch((err) => {
          console.log(err)
          alert('unable to post project. Please try again later...')
        })
    }
  }
}
</script>

<style scoped>
.post {
  padding-top: 15px;
}

#post-write-up {
  text-align: center;
}

.post-body {
  box-shadow: 0px 0px 30px 10px #ededed;
  border-radius: 5px;
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
  padding-left: 15px;
  padding-right: 15px;
  padding-top: 10px;
  padding-bottom: 10px;
  margin-bottom: 10px;
}

label {
  font-weight: bold;
  font-size: 13px;
}
</style>
