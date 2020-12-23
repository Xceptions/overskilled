<template>
  <div>
    <div class="jobs">
      <h1>{{ jobdetails.job_header }}</h1>
      <br>
      <div>{{ jobdetails.job_body }}</div>
      <br>
      <div><b>Company</b>: {{ jobdetails.company }}</div>
      <div><b>Category</b>: {{ jobdetails.category }}</div>
      <div><b>Amount</b>: {{ jobdetails.amount }}</div>
      <div><b>Location</b>: {{ jobdetails.location }}</div>
      <div><b>Date Posted</b>: {{ new Date(jobdetails.date).toDateString() }}</div>
      <br>
      <b-btn variant='primary' @click="contact_url(jobdetails)" id='btn-apply'>Apply</b-btn>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'JobDetails',
  methods: {
    contact_url (details) {
      axios.put('http://127.0.0.1:8000/jobapply/' + details.id + '/')
        .then((res) => {
          const contact = details.contact_me
          const subject = 'APPLICATION FOR ' + details.job_header
          const body = 'Hi, I saw your post on OverSkilled.io and I would like to help you with your job'
          // if email, send mail, else redirect to url
          if (/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(contact)) {
            window.open('mailto:' + contact + '?subject=' + subject + '&body=' + body)
          } else {
            window.open(contact)
          }
        })
        .catch((err) => {
          console.log(err)
          alert('unable to apply for job. Please try again later...')
        })
    }
  },
  computed: {
    jobdetails () {
      return this.$store.state.jobdetails
    }
  },
  mounted () {
    const jobId = this.$route.query.jobId
    this.$store.dispatch('getJobDetails', jobId)
  }
}
</script>

<style scoped lang='scss'>
.jobs {
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
