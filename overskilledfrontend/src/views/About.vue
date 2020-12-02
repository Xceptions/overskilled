<template>
  <div class="about">
    <div v-for = "about in abouts" :key="about.short">
      <h3> The Short. </h3>
      <p class='story'>{{ about['the_short'] }}</p>
      <h3> The Long. </h3>
      <p class='story'>{{ about['the_long'] }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'About',
  data () {
    return {
      short: 'Default Short. Data is not coming from the db',
      long: 'Default Long. Data is not coming from the db'
    }
  },
  computed: {
    abouts () {
      return this.$store.state.abouts
    }
  },
  mounted () {
    this.$store.dispatch('getAbouts')
  }
}
</script>

<style scoped lang='scss'>

.about {
  padding: 15px;
  max-width: 750px;
  margin-left: auto;
  margin-right: auto;
  text-align: left;
}

.story::first-letter {
  font-size: 32px;
  font-weight: bold;
}

</style>
