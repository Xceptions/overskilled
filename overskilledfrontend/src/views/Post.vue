<template>
  <div class="post">
    <div class='post-body'>
      <b>Post a Project</b>
      <hr/>
      <b-form v-on:submit.prevent="postProject" class="b-form">
        <b-form-group label="Header">
          <b-form-input v-model="form.header"></b-form-input>
        </b-form-group>
        <br>
        <b-form-group label='Description'>
          <b-form-textarea v-model="form.description"></b-form-textarea>
        </b-form-group>
        <br>
        <b-form-group label="Amount">
          <b-form-input v-model="form.amount"></b-form-input>
        </b-form-group>
        <b-form-group>
          <b-form-radio v-model="form.bargain" name="some-radios" value="A">Negotiable</b-form-radio>
          <b-form-radio v-model="form.bargain" name="some-radios" value="B">Fixed</b-form-radio>
        </b-form-group>
        <br>
        <b-form-group label="Location">
          <b-form-input v-model="form.location"></b-form-input>
        </b-form-group>
        <br>
        <b-form-group label='Contact Mail'>
          <b-form-input v-model="form.contact"></b-form-input>
        </b-form-group>
        <b-button type='submit' variant="success">Post Project</b-button>
      </b-form>
    </div>
    <br/>
    <div class='post-body'>
      <b>Post a Job</b>
      <hr/>
      <b-form class="b-form">
        <b-form-group id="input-group-1">
          <label>Header</label>
          <b-form-input v-model="form.header"></b-form-input>
          <br>
          <label>Description</label>
          <b-form-textarea v-model="form.description"></b-form-textarea>
          <br>
          <label>Amount</label>
          <b-form-input v-model="form.amount"></b-form-input>
          <br>
          <label>Bargain</label>
          <b-form-input v-model="text"></b-form-input>
          <br>
          <label>Location</label>
          <b-form-input v-model="text"></b-form-input>
          <br>
          <label>Contact Mail</label>
          <b-form-input v-model="text"></b-form-input>
          <br>
          <label>Image</label>
          <b-form-file v-model="file1" @change="onFileSelected"></b-form-file>
        </b-form-group>
        <b-button variant="success">Submit</b-button>
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
        header: '',
        description: '',
        amount: '',
        bargain: '',
        location: '',
        contact: ''
      }
    }
  },
  methods: {
    postProject () {
      axios.post('127.0.0.1:8000/viewprojects', this.form)
        .then((res) => {
          alert(res)
        })
        .catch((err) => {
          alert(err)
          alert(this.form)
        })
    }
  }
  // methods: {
  //   onFileSelected (e) {
  //     this.selectedFile = event.target.files[0]
  //   },
  //   onUpload () {
  //     const fd = new FormData();
  //     fd.append('image', this.selectedFile, this.selectedFile.name)
  //     axios.post('http://127.0.0.1:8000/viewproject', fd, {
  //       // third argument can be used to show upload
  //       onUploadProgress: uploadEvent => {
  //         console.log('Upload Progress: ' + Math.round(uploadEvent.loaded * 100/ uploadEvent.total))
  //       }
  //     })
  //     .then(res => {
  //       // get response to know if it worked
  //       console.log(res)
  //     })
  //   }
  // }
}
</script>

<style scoped>
.post {
  padding-top: 15px;
}

.post-body {
  box-shadow: 0px 0px 30px rgba(230, 230, 230, 0.7);
  border-radius: 5px;
  max-width: 850px;
  margin-left: auto;
  margin-right: auto;
  padding-left: 15px;
  padding-right: 15px;
  padding-top: 10px;
  padding-bottom: 10px;
  margin-bottom: 10px;
}

/* label {
  align-content: left;
} */
</style>
