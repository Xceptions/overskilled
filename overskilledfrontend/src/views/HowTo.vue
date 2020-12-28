<template>
  <div class="howto">
    <div class='howtoheader'>Learn Python</div>
    To Learn the basics of the python programming language, we recommend to pick up one of the following
    books:
    <ol>
      <li>Mark Lutz - Learning Python</li>
      <li>Automate the boring stuff with Python</li>
      <li>Python for dummies</li>
      <li>Think Python</li>
      <li>Learn Python 3 the hard way</li>
    </ol>
    <hr>
    <div class='howtoheader'>Practice Projects</div>
    To get hands-on practice on python
    <ol>
      <li>The Binary Search Algorithm</li>
      <li>WhatsApp for Python - A Web Messaging System</li>
      <li>Contribute to Open Source</li>
      <li>Tic Tac Toe</li>
      <li>Scientific Calculator to solve a science problem</li>
    </ol>
    <hr>
    <div class='howtoheader'>Tools of Specialization</div>
    Below are a list of python libraries and frameworks for various programming specializations:
    <b-table striped hover :items="items"></b-table>
    <p>Know anything else we can add? Feel free to use the contact form</p>
    <!-- <div v-for = "howto in howtos" :key="howto.ace_comp">
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
    </div> -->
  </div>
</template>

<script>
export default {
  name: 'HowTo',
  data () {
    return {
      items: [
        { Specialization: 'Web development', Tools: 'Django, Flask, WSGI' },
        { Specialization: 'Mobile development', Tools: 'Kivy' },
        { Specialization: 'Desktop Applications', Tools: 'Tkinter, PyQt' },
        { Specialization: 'Data Science', Tools: 'Pandas, Numpy, Statsmodels' },
        { Specialization: 'Machine Learning', Tools: 'TensorFlow, Pytorch' },
        { Specialization: 'Network Programming', Tools: 'Asyncio, Diesel' },
        { Specialization: 'Bioinformatics', Tools: 'Biopython' }
      ]
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
