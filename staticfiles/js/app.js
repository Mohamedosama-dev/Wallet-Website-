// static/js/app.js
import Vue from 'vue';
import Home from './components/Home.vue'; // Adjust path as necessary

// Create the Vue instance
new Vue({
  el: '#app',
  components: {
    'home-page': Home
  }
});
