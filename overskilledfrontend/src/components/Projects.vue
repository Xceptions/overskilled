<template>
  <div class="projects">
    <h1>Projects</h1>
    <div id="">
        <div v-for="(item, idx) in projects" :key="item.proj" class="item_card">
            <img alt="Vue logo" src="../assets/logo.png" id="proj_img">
            <div>
                <h3>Project: {{ item.proj }}</h3>
                <h3>Description: {{ item.Description }}</h3>
                <h3>Amount: {{ item.Amount }}</h3>
                <button>Apply</button>
            </div>
        </div>
    </div>
    <div>here</div>
  </div>
</template>


<script>
export default {
    name: 'Projects',
    data() {
        return {
            projects: [
                {'proj': "Build my assignment", 'Description': "fjaodjfadjfaof", 'Amount': "$100"},
                {'proj': "Build my assignment", 'Description': "fjaodjfadjfaof", 'Amount': "$100"},
                {'proj': "Build my assignment", 'Description': "fjaodjfadjfaof", 'Amount': "$100"},
                {'proj': "Build my assignment", 'Description': "fjaodjfadjfaof", 'Amount': "$100"},
                {'proj': "Build my assignment", 'Description': "fjaodjfadjfaof", 'Amount': "$100"},
                {'proj': "Build my assignment", 'Description': "fjaodjfadjfaof", 'Amount': "$100"}
            ]
        }
    }
}
</script>

<style scoped lang="scss">
.item_card {
    box-shadow: 0px 0px 5px 1px rgba(230, 230, 230, 0.7);
    width: 60%;
    margin-left: auto;
    margin-right: auto;
    margin-top: 20px;
    margin-bottom: 20px;
    padding: 20px;
    display: flex;
    flex-direction: row;
    // justify-content: center;
    
}

#proj_img {
    width: 20%;
    height: 20%;
}

</style>