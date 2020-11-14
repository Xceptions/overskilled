<template>
  <div class="talks">
    <h1>Talks</h1>
    <ul id="">
        <li v-for="(item, idx) in talks" :key="item.talk">
            <b>Talk: </b> {{ item.talk }}
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
                {'talk': "Speakation", 'Title': "Coming to speak to us", 'Prize': "unknown"},
                {'talk': "Speakation", 'Title': "Coming to speak to us", 'Prize': "unknown"},
                {'talk': "Speakation", 'Title': "Coming to speak to us", 'Prize': "unknown"},
                {'talk': "Speakation", 'Title': "Coming to speak to us", 'Prize': "unknown"},
                {'talk': "Speakation", 'Title': "Coming to speak to us", 'Prize': "unknown"},
                {'talk': "Speakation", 'Title': "Coming to speak to us", 'Prize': "unknown"},
            ]
        }
    }
}
</script>