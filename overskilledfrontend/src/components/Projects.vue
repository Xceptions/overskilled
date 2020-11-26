<template>
  <div class="projects">
    <div class='project_header'>
        <h2>Projects</h2>
        <p>
            <router-link to="/howto">Learn how to get and approach projects here</router-link>
        </p>
    </div>
    <div id="">
        <div v-for="(item, idx) in projects" :key="item.proj" class="item_card">
            <b-row>
                <b-col id='a'>
                    <img alt="Vue logo" src="../assets/company-1.png" id="proj_img">
                </b-col>
                <b-col id='b' cols="5">
                    <!-- <div>{{ idx }}</div> -->
                    <div id='item_proj'>{{ item.proj }}</div>
                    <div>{{ item.description }}</div>
                </b-col>
                <b-col id='c'>
                    <div>{{ item.amount }}</div>
                    <div><b-badge variant="primary">Negotiable</b-badge></div><!-- / Fixed-->
                </b-col>
                <b-col>
                    <div>Anywhere</div>
                </b-col>
                <b-col></b-col>
                <b-col></b-col>
            </b-row>
        </div>
    </div>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
export default {
  name: 'Projects',
  data () {
    return {
      projects: [
        { proj: 'Build my assignment', description: 'fjaodjfadjfaof', amount: '$1000' },
        { proj: 'Build my assignment', description: 'fjaodjfadjfaof', amount: '$1000' },
        { proj: 'Build my assignment', description: 'fjaodjfadjfaof', amount: '$1000' },
        { proj: 'Build my assignment', description: 'fjaodjfadjfaof', amount: '$1000' },
        { proj: 'Build my assignment', description: 'fjaodjfadjfaof', amount: '$1000' },
        { proj: 'Build my assignment', description: 'fjaodjfadjfaof', amount: '$1000' }
      ]
    }
  }
}
</script>

<style scoped lang="scss">

.project_header {
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
    box-shadow: 0 0 30px rgba(0, 0, 0, 0.15);
}

// #a {
//     background-color: blue;
// }

#item_proj {
    font-size: 23px;
    font-weight: bold;
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
