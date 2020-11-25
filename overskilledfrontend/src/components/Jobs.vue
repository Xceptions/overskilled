<template>
  <div class="jobs">
    <div class='job_header'>
        <h2><b>Jobs</b></h2>
        <p>
            <router-link to="/howto/jobs">Learn how to get jobs here</router-link>
        </p>
    </div>
    <div id="">
        <div v-for="(item, idx) in jobs" :key="item.job" class="item_card">
            <b-row>
                <b-col id='a'>
                    <img alt="Vue logo" src="../assets/company-3.png" id="job_img">
                </b-col>
                <b-col id='b' cols="5">
                    <div id='item_job'>{{ item.title }}</div>
                    <div>{{ item.focus_area }}</div>
                </b-col>
                <b-col id='c'>
                    <div>{{ item.job }}</div>
                    <div><b-badge>{{ item.focus_area }}</b-badge></div><!-- / Fixed-->
                    <div>{{ item.salary }}</div>
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
  data () {
    return {
      jobs: [
        { title: 'Python Developer', focus_area: 'Backend Engineer', salary: '$25,000' },
        { title: 'Python Developer', focus_area: 'Backend Engineer', salary: '$25,000' },
        { title: 'Python Developer', focus_area: 'Backend Engineer', salary: '$25,000' },
        { title: 'Python Developer', focus_area: 'Backend Engineer', salary: '$25,000' },
        { title: 'Python Developer', focus_area: 'Backend Engineer', salary: '$25,000' }
      ]
    }
  }
}
</script>

<style scoped lang="scss">

.jobetition_header {
    padding-top: 30px;
    padding-bottom: 5px;
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
