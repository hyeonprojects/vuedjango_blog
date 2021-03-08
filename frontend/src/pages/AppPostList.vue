<template>
  <v-app id="inspire">
    <MainMenu></MainMenu>

    <v-main>
      <PostList></PostList>
    </v-main>

    <v-footer app>
      <span>&copy; 2020</span>
    </v-footer>
  </v-app>
</template>

<script>
  import MainMenu from "../components/MainMenu"
  import PostList from "../components/PostList";
  
  export default {
    components: { MainMenu, PostList },

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
