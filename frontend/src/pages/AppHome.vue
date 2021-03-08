<template>
  <v-app id="inspire">
    <MainMenu></MainMenu>

    <v-main>
      <HelloWorld></HelloWorld>
    </v-main>

    <v-footer app>
      <span>&copy; 2020</span>
    </v-footer>
  </v-app>
</template>

<script>
  import HelloWorld from "../components/HelloWorld";
  import MainMenu from "../components/MainMenu"
  
  export default {
    components: { MainMenu, HelloWorld },

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
