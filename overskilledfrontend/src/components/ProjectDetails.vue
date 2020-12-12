<template>
  <div>
    <h1>{{ projectdetails.project_header }}</h1>
    <div>{{ projectdetails.project_body }}</div>
    <div>Amount: {{ projectdetails.amount }}</div>
    <div>Bargain: {{ projectdetails.bargain }}</div>
    <div>Location: {{ projectdetails.location }}</div>
    <div>Contact: {{ projectdetails.contact_me }}</div>
    <div>Date Posted: {{ projectdetails.date }}</div>
    <b-btn variant='primary'>Apply</b-btn>
  </div>
</template>

<script>
export default {
  name: 'ProjectDetails',
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
