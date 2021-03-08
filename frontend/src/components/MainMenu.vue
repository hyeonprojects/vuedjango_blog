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
        <v-btn text href='/post_list.html'>PostList</v-btn>
        <v-btn text href='/post_detail.html'>PostDetial</v-btn>

        <v-spacer></v-spacer>
  
        <v-menu offset-y left bottom>
          <template v-slot:activator="{ on, attrs }">
            <v-btn text v-bind="attrs" v-on="on">
              <v-icon>mdi-account</v-icon>Anonymous
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
          </template>
  
          <v-list>
            <v-list-item>
              <v-list-item-title>Login</v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title>Register</v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title>Logout</v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title>Password change</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-app-bar>
  </div>
</template>

<script>
export default {
    data: () => ({
      drawer: null,
    }),
}
</script>

<style>

</style>