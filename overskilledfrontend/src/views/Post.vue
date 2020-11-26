<template>
  <div class="post">
    <div class='post-body'>
      <b>Post a Project</b>
      <hr/>
      <b-form class="b-form">
        <b-form-group id="input-group-1">
          <label>Title</label>
          <b-form-input v-model="text"></b-form-input>
          <br>
          <label>Description</label>
          <b-form-textarea></b-form-textarea>
          <br>
          <label>Amount</label>
          <b-form-input></b-form-input>
        </b-form-group>
        <b-button variant="success">Submit</b-button>
      </b-form>
    </div>
    <br/>
    <div class='post-body'>
      <b>Post a Job</b>
      <hr/>
      <b-form class="b-form">
        <b-form-group id="input-group-1">
          <label>Title</label>
          <b-form-input v-model="text"></b-form-input>
          <br>
          <label>Location</label>
          <b-form-input></b-form-input>
          <br>
          <label>Amount</label>
          <b-form-input></b-form-input>
        </b-form-group>
        <b-button variant="success">Submit</b-button>
      </b-form>
    </div>
  </div>
</template>

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
