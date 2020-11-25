<template>
  <div class="about">
    <h3> The Short. </h3>
    <p class='story'> {{ short }} </p>
    <h3> The Long. </h3>
    <p class='story'> {{ long }} </p>
  </div>
</template>

<script>
export default {
  name: 'About',
  data () {
    return {
      short: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
      long: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
    }
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
