<template>
  <v-container>

      <v-row align="center" justify="center">
        <v-col cols="12" sm="10" lg="10">
          <h1>{{ post.title }}</h1>
          <p>{{ post.modify_dt }} written by {{ post.owner }}</p>
        </v-col>

      </v-row>
      <v-row align="start" justify="center">
        <v-col cols="12" sm="8" lg="7">
          <v-card class="pa-2" outlined tile>
            <p style="white-space: pre-wrap;"> {{post.content}} </p>
            <div>
              <strong>TAGS:</strong>
              <v-chip class="ma-2" outlined v-for="(tag, index) in post.tags" :key="index"> Pyrthon </v-chip>
            </div>
          </v-card>
        </v-col>
        <v-col cols="12" sm="4" lg="3">
          <v-card class="pa-2 mb-5" tile>
            <p>prev post</p>
            <h2 @click="fetchPostDetail(post.prev.id)">{{ post.prev.title }}</h2>
          </v-card>
          <v-card class="pa-2 mb-5" tile>
            <p>next post</p>
            <h2 @click="fetchPostDetail(post.next.id)">{{ post.next.title }}</h2>
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
  import axios from "axios";

  export default {
    name: 'HelloWorld',

    data: () => ({
      post: {},
    }),

    created() {
      console.log("created() ...");
      const postId = 2;
      this.fetchPostDetail(postId);
    },

    methods: {
      fetchPostDetail(postId) {
        console.log("fetchPostDetail()...");
        axios.get('/api/post/${postId}/')
        .then(res => {
          console.log("post detail get res", res);
          this.post = res.data;
        })
        .catch(err => {
          console.log("post detail get err.response", err.response);
          alert(err.response.status + ' ' + err.response.statusText);
        });
      },
    },
  }
</script>
