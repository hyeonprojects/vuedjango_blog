<template>
  <v-container>
    <v-data-table
      :headers="headers"
      :items="posts"
      sort-by="name"
      class="elevation-1"
      :items-per-page="5"
      @click:row="serverPage"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title
            >Post List
            <span v-if="tagname" class="body-1 font-italic ml-3"
              >(with {{ tagname }} tagged)</span
            >
          </v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            dark
            class="mb-2"
            @click="dialogOpen('create', {})"
          >
            New Post
          </v-btn>
        </v-toolbar>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" @click.stop="dialogOpen('update', item)">
          mdi-pencil
        </v-icon>
        <v-icon small @click.stop="deletePost(item)"> mdi-delete </v-icon>
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="fetchPostList"> Reset </v-btn>
      </template>
    </v-data-table>

    <v-dialog v-model="dialog" max-width="800px">
      <v-card>
        <v-card-title>
          <span class="headline">{{ formTitle }}</span>
        </v-card-title>

        <v-card-text>
          <v-form id="post-form" ref="postForm">
            <v-text-field
              label="ID"
              name="id"
              :value="editedItem.id"
            ></v-text-field>
            <v-text-field
              label="TITLE"
              name="title"
              :value="editedItem.title"
            ></v-text-field>
            <v-text-field
              label="DESCRIPTION"
              name="description"
              :value="editedItem.description"
            ></v-text-field>
            <v-textarea
              label="CONTENT"
              name="content"
              :value="editedItem.content"
            ></v-textarea>
            <v-text-field
              label="OWNER"
              name="owner"
              readonly
              :value="editedItem.owner"
            ></v-text-field>
            <v-text-field
              label="TAGS"
              name="tags"
              :value="editedItem.tags"
            ></v-text-field>
          </v-form>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="cancel"> Cancel </v-btn>
          <v-btn color="blue darken-1" text @click="save"> Save </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "PostList",
  data: () => ({
    dialog: false,
    dialogDelete: false,
    tagname: "",
    headers: [
      {
        text: "ID",
        align: "start",
        sortable: false,
        value: "name",
      },
      { text: "제목", value: "title" },
      { text: "요약", value: "description" },
      { text: "수정일", value: "modify_dt" },
      { text: "작성일", value: "owner" },
      { text: "Actions", value: "actions", sortable: false },
    ],
    posts: [],
    editedIndex: -1,
    editedItem: {},
    actionKind: "",
  }),

  computed: {
    formTitle() {
      // return this.editedIndex === -1 ? "New Item" : "Edit Item";
      if (this.actionKind === "create") return "Create Item";
      else return "Update Item";
    },
  },

  created() {
    const params = new URL(location).searchParams;
    this.tagname = params.get("tagname");
    this.fetchPostList();
  },

  methods: {
    fetchPostList() {
      console.log("fetchPostList()...", this.tagname);

      let getUrl = "";
      if (this.tagname) getUrl = `/api/post/list/?tagname=${this.tagname}`;
      else getUrl = "/api/post/list/";

      axios
        .get(getUrl)
        .then((res) => {
          console.log("post get res", res);
          this.posts = res.data;
        })
        .catch((err) => {
          console.log("post list get err. response", err.response);
          alert(err.response.status + " " + err.response.statusText);
        });
    },

    serverPage(item) {
      console.log("serverPage()...", item);
      location.href = `/blog/post/${item.id}/`;
    },

    dialogOpen(actionKind, item) {
      console.log("dialogOpen()...", actionKind);
      this.actionKind = actionKind;
      if (actionKind === "create") {
        this.editedIndex = -1;
        this.editedItem = "";
      } else {
        this.editedIndex = this.posts.indexOf(item);
        this.editedItem = Object.assign({}, item); //object.assign은 앞에 객체에 뒤에 객체를 병합하는 것
      }
      this.dialog = true;
    },

    cancel() {
      console.log("cancel()...");
      this.dialog = false;
    },

    save() {
      console.log("save()....");
      if (this.actionKind === "create") this.createPost();
      else this.updatePost();
      this.dialog = false;
    },

    createPost() {
      console.log("createPost()...");
      const postData = new FormData(document.getElementById("post-form"));
      axios
        .post("/api/post/create/", postData)
        .then((res) => {
          console.log("create post get res", res);
          this.posts.push(res.data);
        })
        .catch((err) => {
          console.log("create post err.response", err.response);
          alert(err.response.status + " " + err.response.statusText);
        });
    },

    updatePost() {
      console.log("updatePost()...");
      const postData = new FormData(document.getElementById("post-form"));
      axios
        .post(`/api/post/${this.editedItem.id}/update/`, postData)
        .then((res) => {
          console.log("update post get res", res);
          this.posts.splice(this.editedIndex, 1, res.data);
        })
        .catch((err) => {
          console.log("update post err.response", err.response);
          alert(err.response.status + " " + err.response.statusText);
        });
    },

    deletePost(item) {
      console.log("deletePost()...", item);
      if (!confirm("Are you sure to delete ?")) return;
      axios
        .delete(`/api/post/${item.id}/delete/`)
        .then((res) => {
          console.log("post delete res", res);
          const index = this.posts.indexOf(item);
          this.posts.splice(index, 1);
        })
        .catch((err) => {
          console.log("update post err.response", err.response);
          alert(err.response.status + " " + err.response.statusText);
        });
    },
  },
};
</script>

<style scoped>
.v-data-table >>> tbody >>> tr {
  cursor: pointer;
}
</style>