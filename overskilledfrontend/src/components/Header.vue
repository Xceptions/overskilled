<template>
  <div class="header">
    {{ msg }}
  </div>
</template>

<script>

export default {
  name: 'Header',
  props: {
    msg: String
  }
}
</script>

<style scoped lang="scss">
.header {
    border: 1px solid red;
    background-color: rgb(0,250,154)
}
</style>