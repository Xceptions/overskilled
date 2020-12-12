<template>
  <div class="projects">
    <div class='project_header'>
        <h2>Projects</h2>
        <p>
          <router-link to="/howto">Learn how to get and approach projects here</router-link>
        </p>
    </div>
    <div id="">
        <div v-for="item in projects" :key="item.id" class="item_card">
            <div @click="viewprojectdetails(item.id)">
            <b-row>
                <b-col class='proj_img'>
                    <!-- {{ item.project_header.charAt(0) }} -->
                    <svg height="100" width="100">
                      <circle cx="50" cy="50" r="40" stroke-width="3" stroke="red" fill="red" />
                    </svg>
                </b-col>
                <b-col id='b' cols="5">
                    <!-- <div>{{ idx }}</div> -->
                    <div id='item_proj'>{{ item.project_header }}</div>
                    <div>{{ item.project_body.slice(0, 100) }}... <span>view more</span></div>
                </b-col>
                <b-col id='c'>
                    <div>{{ item.amount }}</div>
                    <div><b-badge variant="primary">{{ item.bargain }}</b-badge></div><!-- / Fixed-->
                </b-col>
                <b-col>
                    <div>{{ item.location }}</div>
                    <div>{{ new Date(item.date).toDateString() }}</div>
                </b-col>
                <b-col></b-col>
            </b-row>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
export default {
  name: 'Projects',
  computed: {
    projects () {
      return this.$store.state.projects
    }
  },
  mounted () {
    this.$store.dispatch('getProjects')
  },
  methods: {
    viewprojectdetails (projectId) {
      this.$router.push({ path: 'projectdetails', query: { projectId: projectId } })
    }
  }
}
</script>

<style scoped lang="scss">
$theme : rgb(25, 10, 167);
.project_header {
    padding-top: 30px;
    padding-bottom: 5px;
    text-align: center;
}

.item_card {
    border-top: 1px solid #ededed;
    width: 80%;
    // height: 40px;
    margin-left: auto;
    margin-right: auto;
    align-items: center;
    text-align: left;
    padding-top: 15px;
    padding-bottom: 15px;
}

.item_card:hover {
    box-shadow: 0 0 30px rgba(0, 0, 0, 0.15);
}

#item_proj {
    font-size: 23px;
    font-weight: bold;
}

svg {
    text-align: center;
    margin-left: 5px;
}
</style>
