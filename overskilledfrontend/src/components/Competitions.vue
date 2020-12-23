<template>
  <div class="competitions">
    <div class='competition_header'>
        <h2>Competitions</h2>
        <p>
            <router-link to="/howto">Learn how to get and approach competitions here</router-link>
        </p>
    </div>
    <div id="">
        <div v-for="item in competitions" :key="item.platform" class="item_card">
            <div @click="gotocompetition(item)">
            <b-row>
                <b-col id='a'>
                    <svg height="100" width="100">
                      <circle cx="50" cy="50" r="10" stroke-width="3" stroke="#7209b7" fill="#7209b7" />
                    </svg>
                </b-col>
                <b-col id='b' cols="5">
                    <div id='item_comp'>{{ item.title }}</div>
                    <div>{{ item.specialization }}</div>
                </b-col>
                <b-col id='c'>
                    <div>{{ item.platform }}</div>
                    <div><b-badge>{{ item.prize }}</b-badge></div>
                </b-col>
                <b-col>
                  <div>Deadline</div>
                  <div>{{ item.end }}</div>
                </b-col>
            </b-row>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

// eslint-disable-next-line no-unused-vars
export default {
  name: 'competitions',
  computed: {
    competitions () {
      return this.$store.state.competitions
    }
  },
  mounted () {
    this.$store.dispatch('getCompetitions')
  },
  methods: {
    gotocompetition (item) {
      axios.put('http://127.0.0.1:8000/gotocompetition/' + item.id + '/')
        .then((res) => {
          window.open(item.url)
        })
        .catch((err) => {
          console.log(err)
          alert('unable to go to competition. Please try again later...')
        })
    }
  }
}
</script>

<style scoped lang="scss">

.competition_header {
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
    box-shadow: 0px 0px 20px 10px rgba(230, 230, 230, 0.7);
  }
}

#item_comp {
    font-size: 23px;
    font-weight: bold;
}

svg {
    text-align: center;
    margin-left: 5px;
}
</style>
