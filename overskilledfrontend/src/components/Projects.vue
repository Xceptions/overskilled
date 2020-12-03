<template>
  <div class="projects">
    <div class='project_header'>
        <h2>Projects</h2>
        <p>
            <router-link to="/howto">Learn how to get and approach projects here</router-link>
        </p>
    </div>
    <div id="">
        <div v-for="item in projects" :key="item.project_header" class="item_card">
            <b-row>
                <b-col class='proj_img'>
                    <!-- <img alt="Vue logo" src="../assets/company-1.png" id="proj_img"> -->
                    {{ item.project_header.charAt(0) }}
                </b-col>
                <b-col id='b' cols="5">
                    <!-- <div>{{ idx }}</div> -->
                    <div id='item_proj'>{{ item.project_header }}</div>
                    <div>{{ item.project_body }}</div>
                </b-col>
                <b-col id='c'>
                    <div>{{ item.amount }}</div>
                    <div><b-badge variant="primary">{{ item.bargain }}</b-badge></div><!-- / Fixed-->
                </b-col>
                <b-col>
                    <div>{{ item.location }}</div>
                    <!-- <a :href="item.contact">{{ item.contact_me }}</a> -->
                    <b-button :href="item.contact_me" variant='primary'> Apply </b-button>
                </b-col>
                <b-col></b-col>
                <!-- <b-col></b-col> -->
            </b-row>
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
    // alert(this.$store.state.projects)
  }
}
</script>

<style scoped lang="scss">

.project_header {
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
    box-shadow: 0 0 30px rgba(0, 0, 0, 0.15);
}

// #a {
//     background-color: blue;
// }

#item_proj {
    font-size: 23px;
    font-weight: bold;
}

.proj_img {
    height: 100%;
    width: 100;
    color: red;
}
// #b {
//     background-color: green;
// }

// #c {
//     background-color: yellow;
// }
// .item_card {
//     box-shadow: 0px 0px 5px 1px rgba(230, 230, 230, 0.7);
//     width: 60%;
//     margin-left: auto;
//     margin-right: auto;
//     margin-top: 20px;
//     margin-bottom: 20px;
//     padding: 20px;
//     display: flex;
//     flex-direction: row;
    // justify-content: center;
// }

// #proj_img {
//     width: 100%;
//     height: 100%;
// }
</style>
