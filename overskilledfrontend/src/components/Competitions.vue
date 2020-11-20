<template>
  <div class="competitions">
    <div class='competition_header'>
        <h2><b>Competitions</b></h2>
        <p>
            <router-link to="/howto">Learn how to get and approach competitions here</router-link>
        </p>
    </div>
    <div id="">
        <div v-for="(item, idx) in competitions" :key="item.comp" class="item_card">
            <b-row>
                <b-col id='a'>
                    <img alt="Vue logo" src="../assets/company-5.png" id="comp_img">
                </b-col>
                <b-col id='b' cols="5">
                    <div id='item_comp'>{{ item.title }}</div>
                    <div>{{ item.focus_area }}</div>
                </b-col>
                <b-col id='c'>
                    <div>{{ item.comp }}</div>
                    <div><b-badge>{{ item.length }}</b-badge></div><!-- / Fixed-->
                </b-col>
                <b-col cols="4">
                    <span>{{ item.start }}</span> - <span>{{ item.end }}</span>
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
  name: 'competitions',
  data () {
    return {
      competitions: [
        { comp: 'Kaggle', focus_area: 'computer vision, NLP, regression', title: 'Titanic Competition', prize: '$25,000', start: 'Jan 17, 2020', end: 'Mar 25, 2020' },
        { comp: 'Kaggle', focus_area: 'computer vision, NLP, regression', title: 'Titanic Competition', prize: '$25,000', start: 'Jan 17, 2020', end: 'Mar 25, 2020' },
        { comp: 'Kaggle', focus_area: 'computer vision, NLP, regression', title: 'Titanic Competition', prize: '$25,000', start: 'Jan 17, 2020', end: 'Mar 25, 2020' },
        { comp: 'Kaggle', focus_area: 'computer vision, NLP, regression', title: 'Titanic Competition', prize: '$25,000', start: 'Jan 17, 2020', end: 'Mar 25, 2020' },
        { comp: 'Kaggle', focus_area: 'computer vision, NLP, regression', title: 'Titanic Competition', prize: '$25,000', start: 'Jan 17, 2020', end: 'Mar 25, 2020' },
        { comp: 'Kaggle', focus_area: 'computer vision, NLP, regression', title: 'Titanic Competition', prize: '$25,000', start: 'Jan 17, 2020', end: 'Mar 25, 2020' }
      ]
    }
  }
}
</script>

<style scoped lang="scss">

.competition_header {
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

#item_comp {
    font-size: 23px;
    font-weight: bold;
}
</style>
