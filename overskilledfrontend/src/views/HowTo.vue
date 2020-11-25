<template>
  <div class="howto">
    <h3> Ace Competitions </h3>
    <p class='story'> {{ competitions_story }} </p>
    <b>Helpful Resources</b>
    <p v-for="item in competitions_links" :key="item">
      <a href= item>{{ item }}</a>
    </p>
    <br>
    <h3> Get Projects </h3>
    <p class='story'> {{ projects_story }} </p>
    <b>Helpful Resources</b>
    <p v-for="item in projects_links" :key="item">
      <a href= item>{{ item }}</a>
    </p>
    <br>
    <h3> Get Jobs </h3>
    <p class='story'> {{ jobs_story }} </p>
    <b>Helpful Resources</b>
    <p v-for="item in jobs_links" :key="item">
      <a href= item>{{ item }}</a>
    </p>
    <br>
  </div>
</template>

<script>
export default {
  name: 'HowTo',
  data () {
    return {
      competitions_story: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
      projects_story: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
      jobs_story: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
      competitions_links: ['http://www.sawa.com', 'www.adfaodj.com', 'www.afoihfaoj.com'],
      projects_links: ['www.sawa.com', 'www.adfaodj.com', 'www.afoihfaoj.com'],
      jobs_links: ['www.sawa.com', 'www.adfaodj.com', 'www.afoihfaoj.com']
    }
  }
}
</script>

<style scoped lang='scss'>

.howto {
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
