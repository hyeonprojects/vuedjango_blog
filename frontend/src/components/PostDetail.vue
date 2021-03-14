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
              <v-chip class="ma-2 my-hover" outlined v-for="(tag, index) in post.tags" :key="index" @click="serverPage(tag)"> {{ tag }} </v-chip>
            </div>
          </v-card>
        </v-col>
        <v-col cols="12" sm="4" lg="3">
          <v-card class="pa-2 mb-5" tile>
            <p>prev post</p>
            <h2 v-if="post.prev" @click="fetchPostDetail(post.prev.id)" class="my-hover">{{ post.prev.title }}</h2>
          </v-card>
          <v-card class="pa-2 mb-5" tile>
            <p>next post</p>
            <h2 v-if="post.next" @click="fetchPostDetail(post.next.id)" class="my-hover">{{ post.next.title }}</h2>
          </v-card>
          <v-card class="pa-2" tile>
            <h2>Tag Cloud</h2>
            <v-chip v-for="(tag, index) in tagCloud" :key="index" @click="serverPage(tag.name)"
             class="ma-2" :color="tag.color" text-color="white">
              <v-avatar left :class="tag.color + ' darken-4'">
                {{ tag.count }}
              </v-avatar>
              {{ tag.name }}
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
      tagCloud: [],
    }),

    created() {
      console.log("created() ...");
      const postId = 2;
      this.fetchPostDetail(postId);
      this.fetchTagCloud();
    },

    methods: {
      fetchPostDetail(postId) {
        console.log("fetchPostDetail()...", postId);

        axios.get(`/api/post/${postId}/`)
        .then(res => {
          console.log("post detail get res", res);
          this.post = res.data;
        })
        .catch(err => {
          console.log("post detail get err.response", err.response);
          alert(err.response.status + ' ' + err.response.statusText);
        });
      },

      fetchTagCloud() {
        console.log("fetchTagCloud()...");
        axios.get('/api/tag/cloud/')
        .then(res => {
          console.log("tag cloud get res", res);
          this.tagCloud = res.data;
          this.tagCloud.forEach(element => {
            if (element.weight === 3) element.color = 'green';
            else if (element.weight === 2) element.color = 'blue-grey';
            else if (element.weight === 1) element.color = 'grey';
          })
        })
        .catch(err => {
          console.log("tag cloud get err.response", err.response);
          alert(err.response.status + ' ' + err.response.statusText);
        });
      },

      serverPage(tagname) {
        console.log("serverPage()...", tagname)
        location.href = `/blog/post/list/?tagname=${tagname}`;
      },

    },
  }
</script>

<style scoped>
  .my-hover:hover {
    cursor: pointer;
    font-style: italic;
  }
</style>
