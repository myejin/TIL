<template>
  <v-app>
    <v-card class="overflow-hidden">
      <v-app-bar
        absolute
        color="#6A76AB"
        dark
        shrink-on-scroll
        prominent
        src="https://picsum.photos/1920/1080?random"
        fade-img-on-scroll
        scroll-target="#scrolling-techniques-3"
      >
        <template v-slot:img="{ props }">
          <v-img
            v-bind="props"
            gradient="to top right, rgba(100,115,201,.7), rgba(25,32,72,.7)"
          ></v-img>
        </template>

        <v-app-bar-nav-icon>
          <v-img
            alt="Vuetify Logo"
            class="shrink mr-2"
            contain
            src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
            transition="scale-transition"
            width=3%
          />
        </v-app-bar-nav-icon>
        <v-app-bar-title>
          <v-img
            alt="Vuetify Name"
            class="shrink mt-1 hidden-sm-and-down"
            contain
            min-width="100"
            src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
            width="100"
          />
        </v-app-bar-title>
        <v-spacer></v-spacer>
        <v-btn icon @click="goSearch">
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
        <v-btn icon @click="goWishList">
          <v-icon>mdi-heart</v-icon>
        </v-btn>
        <v-btn icon @click="goSetting">
          <v-icon>mdi-dots-vertical</v-icon>
        </v-btn>

        <template v-slot:extension>
          <v-tabs align-with-title>
            <v-tab @click="goHome">
              Home
            </v-tab>
            <v-tab @click="goAbout">
              About
            </v-tab>
          </v-tabs>
        </template>
      </v-app-bar>
      <v-sheet
        id="scrolling-techniques-3"
        class="overflow-y-auto"
        max-height="600"
      >
        <v-container style="height: 224px; border: none;"></v-container>
      </v-sheet>
    </v-card>

    <router-view/>
    <br><br>
    <v-footer
      bottom
      absolute
      padless
    >
      <v-row
        justify="center"
        no-gutters
      >
        <v-btn
          v-for="link in links"
          :key="link"
          color="black"
          text
          rounded
          class="my-2"
        >
          {{ link }}
        </v-btn>
      </v-row>
    </v-footer>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    links: [
        'Home',
        'About Us',
        'Team',
        'Services',
        'Contact Us',
      ],
  }),
  methods: {
    goHome: function () {
      this.$router.push({ name: 'Home' })
    },
    goAbout: function () {
      this.$router.push({ name: 'About' })
    },
    goSearch: function () {
      //
    },
    goWishList: function () {
      //
    },
    goSetting: function () {
      //
    }
  }
};
</script>
