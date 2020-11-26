<template>
  <div class="post">
    <div class='post-body'>
      <b>Post a Project</b>
      <hr/>
      <b-form class="b-form">
        <b-form-group id="input-group-1">
          Name
          <b-form-input v-model="text" placeholder="Email Address"></b-form-input>
          <br>
          <b-form-textarea placeholder="Tell us!"></b-form-textarea>
        </b-form-group>
      </b-form>
    </div>
    <br/>
    <div class='post-body'>
      <b>Post a Job</b>
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
}
</style>
