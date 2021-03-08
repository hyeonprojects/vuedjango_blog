<template>
  <v-app id="inspire">
    <MainMenu></MainMenu>

    <v-main>
      <PostDetail></PostDetail>
    </v-main>

    <v-footer app>
      <span>&copy; 2020</span>
    </v-footer>
  </v-app>
</template>

<script>
  import MainMenu from "../components/MainMenu"
  import PostDetail from "../components/PostDetail";
  
  export default {
    components: { MainMenu, PostDetail },

    props: {
      source: String,
    },

    data: () => ({
      // drawer: null,
    }),

    created: () => {
      // this.$vuetify.theme.dark = true
    },
  }
</script>
