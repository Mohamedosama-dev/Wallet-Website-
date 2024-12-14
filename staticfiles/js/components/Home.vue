<!-- static/js/components/Home.vue -->
<template>
  <div class="home">
    <h1>Welcome to the Wallet App</h1>
    <a href="/sign-up" class="btn">Sign Up</a>
    <a href="/sign-in" class="btn">Sign In</a>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
};
</script>

<style scoped>
.home {
  text-align: center;
}

h1 {
  font-size: 3em;
  margin-bottom: 20px;
}

a.btn {
  display: inline-block;
  text-decoration: none;
  color: #005f73;
  background-color: #ffffff;
  padding: 15px 30px;
  border-radius: 50px;
  font-size: 1.5em;
  font-weight: 500;
  transition: background-color 0.3s, color 0.3s;
  margin: 10px;
  box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
}

a.btn:hover {
  background-color: #0a9396;
  color: #ffffff;
  transform: translateY(-3px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
}
</style>
