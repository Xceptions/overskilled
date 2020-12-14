<template>
  <div>
    <div class="projects">
      <h1>{{ projectdetails.project_header }}</h1>
      <br>
      <div>{{ projectdetails.project_body }}</div>
      <br>
      <div>Amount: {{ projectdetails.amount }}</div>
      <div>Bargain: {{ projectdetails.bargain }}</div>
      <div>Location: {{ projectdetails.location }}</div>
      <div>Date Posted: {{ new Date(projectdetails.date).toDateString() }}</div>
      <br>
      <b-btn variant='primary' @click="contact_url(projectdetails)" id='btn-apply'>Apply</b-btn>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProjectDetails',
  methods: {
    contact_url (details) {
      const contact = details.contact_me
      const subject = 'APPLICATION FOR ' + details.project_header
      const body = 'Hi, I saw your post on OverSkilled.io and I would like to help you with your project'
      // if email, send mail, else redirect to url
      if (/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(contact)) {
        window.open('mailto:' + contact + '?subject=' + subject + '&body=' + body)
      } else {
        window.open(contact)
      }
    }
  },
  computed: {
    projectdetails () {
      return this.$store.state.projectdetails
    }
  },
  mounted () {
    const projectId = this.$route.query.projectId
    this.$store.dispatch('getProjectDetails', projectId)
  }
}
</script>

<style scoped lang='scss'>
.projects {
  padding: 15px;
  max-width: 750px;
  margin-left: auto;
  margin-right: auto;
  text-align: left;
  border-left: 1px solid #0099ff;
  border-right: 1px solid #0099ff;
}

#btn-apply {
  width: 200px;
}
</style>
