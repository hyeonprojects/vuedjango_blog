<template>
  <div>
      <v-navigation-drawer v-model="drawer" app clipped>
      <v-list dense>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-view-dashboard</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>dashboard</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-cog</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Settings</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app clipped-left color="indigo" dark>
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
  
        <v-toolbar-title>vue.js - django</v-toolbar-title>
  
        <v-spacer></v-spacer>
        
        <v-btn text href='/'>Home</v-btn>
        <v-btn text href='/blog/post/list/'>Blog</v-btn>
        <v-btn text href='/admin/'>Admin</v-btn>
        <v-btn text>/</v-btn>
        <v-btn text href='/post_list.html'>PostList</v-btn>
        <v-btn text href='/post_detail.html'>PostDetail</v-btn>

        <v-spacer></v-spacer>
  
        <v-menu offset-y left bottom>
          <template v-slot:activator="{ on, attrs }">
            <v-btn text v-bind="attrs" v-on="on">
              <v-icon>mdi-account</v-icon>Anonymous
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
          </template>
  
          <v-list>
            <v-list-item @click="dialog.login = true">
              <v-list-item-title>Login</v-list-item-title>
            </v-list-item>
            <v-list-item @click="dialog.register = true">
              <v-list-item-title>Register</v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title>Logout</v-list-item-title>
            </v-list-item>
            <v-list-item @click="dialog.pwdchg = true">
              <v-list-item-title>Password change</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
    </v-app-bar>

    <!-- login dialog -->
    <v-dialog v-model="dialog.login" max-width="600">
      <v-card class="elevation-12">
        <v-toolbar color="primary" dark flat>
          <v-toolbar-title>Login Form</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-card-text>
          <v-form id="login-form">
            <v-text-field label="username" name="username" prepend-icon="mdi-account" type="text">
            </v-text-field>
            <v-text-field label="password" name="password" prepend-icon="mdi-lock" type="password">
            </v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text color="gray" @click="cancel('login')">Cancel</v-btn>
          <v-btn color="primary" @click="save('login')">Login</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- register dialog -->
    <v-dialog v-model="dialog.register" max-width="600">
      <v-card class="elevation-12">
        <v-toolbar color="success" dark flat>
          <v-toolbar-title>Register Form</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-card-text>
          <v-form>
            <v-text-field label="username" name="username" prepend-icon="mdi-account" type="text">
            </v-text-field>
            <v-text-field label="password" name="password1" prepend-icon="mdi-lock" type="password">
            </v-text-field>
            <v-text-field label="password again" name="password2" prepend-icon="mdi-lock" type="password">
            </v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text color="gray" @click="dialog.register = false">Cancel</v-btn>
          <v-btn color="success" @click="dialog.register = false">Register</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- pwdchg dialog -->
    <v-dialog v-model="dialog.pwdchg" max-width="600">
      <v-card class="elevation-12">
        <v-toolbar color="warning" dark flat>
          <v-toolbar-title>Password change Form</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-card-text>
          <v-form>
            <v-text-field label="old_password" name="old_password" prepend-icon="mdi-lock" type="password">
            </v-text-field>
            <v-text-field label="new password" name="new_password1" prepend-icon="mdi-lock" type="password">
            </v-text-field>
            <v-text-field label="new password again" name="new_password2" prepend-icon="mdi-lock" type="password">
            </v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text color="gray" @click="dialog.pwdchg = false">Cancel</v-btn>
          <v-btn color="warning" @click="dialog.pwdchg = false">Password change</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from 'axios';

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

export default {
    data: () => ({
      drawer: null,
      dialog: {
        login: false,
        register: false,
        pwdchg: false,
      },
      me: {},
    }),

    methods : {
      cancel(kind) {
        console.log("cancel()...", kind);
        if (kind === 'login') this.dialog.login = false;
        else if (kind === 'register') this.dialog.register = false;
        else if (kind === 'pwdchg') this.dialog.pwdchg = false;
      },

      save(kind) {
        console.log("save()...", kind);
        if (kind === 'login') {
          this.login();
          this.dialog.login = false;
        } else if (kind === 'register') {
          this.register();
          this.dialog.register = false;
        } else if (kind === 'pwdchg') {
          this.pwdchg();
          this.dialog.pwdchg = false;
        }
      },

      login() {
        console.log("login()...");
        const postData = new FormData(document.getElementById('login-form'))
        axios.post('/api/login/', postData)
        .then(res => {
          console.log("login post res", res);
          this.me = res.data;
        })
        .catch(err => {
          console.log("login post err. response", err.response);
          alert("login nok");
        });
      },
    },
}
</script>

<style>

</style>