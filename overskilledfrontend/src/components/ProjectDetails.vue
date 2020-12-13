<template>
  <div>
    <h1>{{ projectdetails.project_header }}</h1>
    <div>{{ projectdetails.project_body }}</div>
    <div>Amount: {{ projectdetails.amount }}</div>
    <div>Bargain: {{ projectdetails.bargain }}</div>
    <div>Location: {{ projectdetails.location }}</div>
    <div>Contact: {{ projectdetails.contact_me }}</div>
    <div>Date Posted: {{ projectdetails.date }}</div>
    <b-btn variant='primary' @click="contact_url(projectdetails)">Apply</b-btn>
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
