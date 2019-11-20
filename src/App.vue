<template>
  <div id="app" class="mt-0">
    <Layout>
      <router-view/>
    </Layout>
  </div>
</template>
<script>
import Layout from "./layout/Layout";

export default {
  components: {Layout},
}
</script>
<style>
#app {
  font-family: 'Bai Jamjuree', 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
