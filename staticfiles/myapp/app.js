// static/your_app/app.js

import Vue from 'vue';

// HomePage component
Vue.component('home-page', {
    template: `
        <div class="home">
            <h1>Welcome to the Wallet App</h1>
            <a href="/sign-up" class="btn">Sign Up</a>
            <a href="/sign-in" class="btn">Sign In</a>
        </div>
    `,
});

// Create the Vue instance
new Vue({
    el: '#app',
});
