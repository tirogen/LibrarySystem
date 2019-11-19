<template>
  <div id="app" class="mt-0">
<!--    <b-container>-->
<!--      <h1>Library System</h1>-->
<!--      <div id="nav">-->
<!--       <router-link :to="{ name: 'home' }">Home</router-link> |-->
<!--       <router-link :to="{ name: 'student' }">Student</router-link> |-->
<!--       <router-link :to="{ name: 'librarian' }">Librarian</router-link>-->
<!--      </div>-->
<!--      <router-view/>-->
<!--    </b-container>-->
    <Layout>
      <router-view/>
    </Layout>
  </div>
</template>
<script>
  import Layout from "./layout/Layout";
  export default {
      components: {Layout},
      comments: {
          Layout
      }
  }
</script>
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
