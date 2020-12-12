<template>
  <div>
    Project
  </div>
</template>

<script>
export default {
  name: 'ProjectDetails',
  computed: {
    projects () {
      return this.$store.state.projects
    }
  },
  mounted () {
    const projectId = this.$route.query.projectId
    this.$store.dispatch('getProjectDetails', projectId)
  }
}
</script>
