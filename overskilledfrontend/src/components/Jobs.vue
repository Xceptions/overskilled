<template>
  <div class="jobs">
    <h1>Jobs</h1>
    <ul id="">
        <li v-for="(item, idx) in talks" :key="item.job">
            <b>Job: </b> {{ item.job }}
            <b>Title: </b> {{ item.Title }}
            <b>Prize: </b> {{ item.Prize }}
        </li>
    </ul>
    <div>here</div>
  </div>
</template>


<script>
export default {
    name: 'Talks',
    data() {
        return {
            talks: [
                {'job': "Python Developer", 'Title': "Coming to code for us", 'Prize': "$400/month"},
                {'job': "Python Developer", 'Title': "Coming to code for us", 'Prize': "$400/month"},
                {'job': "Python Developer", 'Title': "Coming to code for us", 'Prize': "$400/month"},
                {'job': "Python Developer", 'Title': "Coming to code for us", 'Prize': "$400/month"},
                {'job': "Python Developer", 'Title': "Coming to code for us", 'Prize': "$400/month"}
            ]
        }
    }
}
</script>