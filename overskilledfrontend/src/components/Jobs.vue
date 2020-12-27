<template>
  <div class="jobs">
    <div class='job_header'>
        <h2>Jobs</h2>
        <!-- <p>
          <router-link to="/howto">Learn how to get jobs here</router-link>
        </p> -->
    </div>
    <div id="">
        <div v-for="item in jobs" :key="item.id" class="item_card">
            <div @click="viewjobdetails(item.id)">
            <b-row>
                <b-col class='proj_img'>
                    <!-- {{ item.job_header.charAt(0) }} -->
                    <svg height="100" width="100">
                      <circle cx="50" cy="50" r="10" stroke-width="3" stroke="#7209b7" fill="#7209b7" />
                    </svg>
                </b-col>
                <b-col id='b' cols="5">
                    <!-- <div>{{ idx }}</div> -->
                    <div class='item_header'>{{ item.job_header.slice(0, 30) }}...</div>
                    <div>{{ item.job_body.slice(0, 50) }}...</div>
                </b-col>
                <b-col id='c'>
                    <div>{{ item.amount }}</div>
                    <div><b-badge variant="primary">{{ item.bargain }}</b-badge></div><!-- / Fixed-->
                </b-col>
                <b-col>
                    <div>{{ item.location }}</div>
                    <div>{{ new Date(item.date).toDateString() }}</div>
                </b-col>
                <!-- <b-col></b-col> -->
            </b-row>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
export default {
  name: 'Jobs',
  computed: {
    jobs () {
      return this.$store.state.jobs
    }
  },
  mounted () {
    this.$store.dispatch('getJobs')
  },
  methods: {
    viewjobdetails (jobId) {
      this.$router.push({ path: 'jobdetails', query: { jobId: jobId } })
    }
  }
}
</script>

<style scoped lang="scss">
$theme : rgb(25, 10, 167);
.job_header {
    padding-top: 30px;
    padding-bottom: 5px;
    text-align: center;
}

.item_card {
    border-top: 1px solid #ededed;
    width: 60%;
    margin-left: auto;
    margin-right: auto;
    align-items: center;
    text-align: left;
    padding-top: 15px;
    padding-bottom: 15px;
}

@media (hover: hover) and (pointer: fine) {
  .item_card:hover {
    box-shadow: 0 0 30px rgba(0, 0, 0, 0.15);
  }
}

.item_header {
    font-size: 23px;
    color: #777;
    font-weight: bold;
}

svg {
    text-align: center;
    margin-left: 5px;
}
</style>
