<template>
  <div class="howto">
    <div class='howtoheader'>Learn Python</div>
    To Learn the basics of the python programming language, we recommend to pick up one of the following
    books:
    <ol>
      <li>Mark Lutz - Learning Python</li>
      <li>Automate with Python</li>
      <li>Python for dummies</li>
    </ol>
    <hr>
    <div class='howtoheader'>Practice Projects</div>
    To get hands-on practice on python
    <ol>
      <li>The Binary Search Algorithm</li>
      <li>WhatsApp for Python - A Web Messaging System</li>
      <li>Contribute to Open Source</li>
      <li>Build facebook</li>
    </ol>
    <hr>
    <div class='howtoheader'>Tools of Specialization</div>
    Below are a list of python libraries and frameworks for various programming specialization:
    <table>
      <th>Specialization</th>
      <th>Tools</th>
      <tr>
        <td>Web development</td>
        <td>Data Science</td>
      </tr>
    </table>
    <div v-for = "howto in howtos" :key="howto.ace_comp">
      <h3> Ace Competitions </h3>
      <p class='story'>{{ howto['ace_comp'] }}</p>
      <h3> Helpful Resources </h3>
      <p class='story'>{{ howto['ace_comp_res'] }}</p>
      <br>
      <h3> Get Projects </h3>
      <p class='story'>{{ howto['get_proj'] }}</p>
      <h3> Helpful Resources </h3>
      <p class='story'>{{ howto['get_proj_res'] }}</p>
      <br>
    </div>
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
  },
  computed: {
    howtos () {
      return this.$store.state.howtos
    }
  },
  mounted () {
    this.$store.dispatch('getHowTos')
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

.howtoheader {
  font-size: 25px;
}

.howtoheader::first-letter {
  font-size: 35px;
  // font-weight: bold;
}
</style>
