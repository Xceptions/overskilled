<template>
  <div class="jobs">
    <div class='job_header'>
        <h2><b>Jobs</b></h2>
        <p>
            <router-link to="/howto/jobs">Learn how to get jobs here</router-link>
        </p>
    </div>
    <div id="">
        <div v-for="item in jobs" :key="item.title" class="item_card">
            <b-row>
                <!-- <b-col id='a'>
                    <img alt="Vue logo" src="../../../overskilledbackend/media/images/company-5.png" + id="job_img">
                </b-col> -->
                <b-col id='b' cols="5">
                    <div id='item_job'>{{ item.title }}</div>
                    <div>{{ item.company }}</div>
                </b-col>
                <b-col id='c'>
                    <!-- <div>{{ item.job }}</div> -->
                    <div><b-badge>{{ item.location }}</b-badge></div><!-- / Fixed-->
                    <div>{{ new Date(item.date).toDateString() }}</div>
                </b-col>
                <!-- <b-col></b-col>
                <b-col></b-col> -->
            </b-row>
        </div>
    </div>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
export default {
  name: 'Jobs',
  // data () {
  //   return {
  //     jobs: [
  //       { title: 'Python Developer', company: 'Google', location: 'Anywhere', date: '25/09/2020' },
  //       { title: 'Python Developer', company: 'Google', location: 'America', date: '25/09/2020' },
  //       { title: 'Python Developer', company: 'Google', location: 'Anywhere', date: '25/09/2020' },
  //       { title: 'Python Developer', company: 'Google', location: 'EMEA', date: '25/09/2020' },
  //       { title: 'Python Developer', company: 'Google', location: 'Anywhere', date: '25/09/2020' }
  //     ]
  //   }
  // },
  computed: {
    jobs () {
      return this.$store.state.jobs
    }
  },
  mounted () {
    this.$store.dispatch('getJobs')
  }
}
</script>

<style scoped lang="scss">

.job_header {
    padding-top: 30px;
    padding-bottom: 5px;
    text-align: center;
}

.item_card {
    border-top: 1px solid #ededed;
    width: 80%;
    margin-left: auto;
    margin-right: auto;
    align-items: center;
    text-align: left;
    padding-top: 15px;
    padding-bottom: 15px;
}

.item_card:hover {
    box-shadow: 0px 0px 20px 10px rgba(230, 230, 230, 0.7);
}

#item_job {
    font-size: 23px;
    font-weight: bold;
}
</style>
