<template>
  <v-container>

      <v-row align="center" justify="center">
        <v-col cols="12" sm="10" lg="10">
          <h1>Post Title here</h1>
          <p>2020-07-10 written by hyeon</p>
        </v-col>

      </v-row>
      <v-row align="start" justify="center">
        <v-col cols="12" sm="8" lg="7">
          <v-card class="pa-2" outlined tile>
            <p>
              나는 뷰랑 장고를 학습중입니다. <br>
              <br>
              <br>
              <br>
              <br>
              <br>
              <br>
              <br>
              <br>
              <br>
              <br>
              <br>
              그리고 Vuetify를 학습하며 사용하고 있습니다.
            </p>
            <div>
              <strong>TAGS:</strong>
              <v-chip class="ma-2" outlined>
                Pyrthon
              </v-chip>
              <v-chip class="ma-2" outlined>
                Django
              </v-chip>
            </div>
          </v-card>
        </v-col>
        <v-col cols="12" sm="4" lg="3">
          <v-card class="pa-2 mb-5" tile>
            <p>prev post</p>
            <h2>Previous title here</h2>
          </v-card>
          <v-card class="pa-2 mb-5" tile>
            <p>next post</p>
            <h2>Next title here</h2>
          </v-card>
          <v-card class="pa-2" tile>
            <h2>Tag Cloud</h2>
            <v-chip class="ma-2" color="green" text-color="white">
              <v-avatar left class="green darken-4">
                1
              </v-avatar>
              Python
            </v-chip>
            <v-chip class="ma-2" color="green" text-color="white">
              <v-avatar left class="green darken-4">
                1
              </v-avatar>
              Django
            </v-chip>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
</template>

<script>
  export default {
    name: 'HelloWorld',

    data: () => ({
      ecosystem: [
        {
          text: 'vuetify-loader',
          href: 'https://github.com/vuetifyjs/vuetify-loader',
        },
        {
          text: 'github',
          href: 'https://github.com/vuetifyjs/vuetify',
        },
        {
          text: 'awesome-vuetify',
          href: 'https://github.com/vuetifyjs/awesome-vuetify',
        },
      ],
      importantLinks: [
        {
          text: 'Documentation',
          href: 'https://vuetifyjs.com',
        },
        {
          text: 'Chat',
          href: 'https://community.vuetifyjs.com',
        },
        {
          text: 'Made with Vuetify',
          href: 'https://madewithvuejs.com/vuetify',
        },
        {
          text: 'Twitter',
          href: 'https://twitter.com/vuetifyjs',
        },
        {
          text: 'Articles',
          href: 'https://medium.com/vuetify',
        },
      ],
      whatsNext: [
        {
          text: 'Explore components',
          href: 'https://vuetifyjs.com/components/api-explorer',
        },
        {
          text: 'Select a layout',
          href: 'https://vuetifyjs.com/getting-started/pre-made-layouts',
        },
        {
          text: 'Frequently Asked Questions',
          href: 'https://vuetifyjs.com/getting-started/frequently-asked-questions',
        },
      ],
    }),
  }
</script>
