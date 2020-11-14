<template>
  <div class="competitions">
    <h2>Competitions</h2>
    <div id="">
        <div v-for="(item, idx) in competitions" :key="item.comp" class="item_card">
            <img alt="Vue logo" src="../assets/logo.png" id="comp_img">
            <div>
                <h3>Platform: {{ item.comp }}</h3>
                <h3>Title: {{ item.title }}</h3>
                <h3>Focus: {{ item.focus_area }}</h3>
                <h3>Prize: {{ item.prize }}</h3>
                <button>Apply</button>
            </div>
        </div>
    </div>
    <div>here</div>
  </div>
</template>


<script>
export default {
    name: 'Competitions',
    data() {
        return {
            competitions: [
                {'comp': "Kaggle", 'focus_area': "computer vision, NLP, regression",  'title': "Titanic Competition", 'prize': "$25,000"},
                {'comp': "Kaggle", 'focus_area': "computer vision, NLP, regression",  'title': "Titanic Competition", 'prize': "$25,000"},
                {'comp': "Kaggle", 'focus_area': "computer vision, NLP, regression",  'title': "Titanic Competition", 'prize': "$25,000"},
                {'comp': "Kaggle", 'focus_area': "computer vision, NLP, regression",  'title': "Titanic Competition", 'prize': "$25,000"},
                {'comp': "Kaggle", 'focus_area': "computer vision, NLP, regression",  'title': "Titanic Competition", 'prize': "$25,000"},
                {'comp': "Kaggle", 'focus_area': "computer vision, NLP, regression",  'title': "Titanic Competition", 'prize': "$25,000"}
            ]
        }
    }
}
</script>

<style scoped lang="scss">
.item_card {
    box-shadow: rgba(250, 250, 250, 0.7);
    width: 60%;
    background-color: #fff;
    margin-left: auto;
    margin-right: auto;
    margin-top: 20px;
    margin-bottom: 20px;
    padding: 20px;
    display: flex;
    flex-direction: row;
    // justify-content: center;
    
}

#comp_img {
    width: 20%;
    height: 20%;
}

</style>