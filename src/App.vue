<template>
  <div
    id="app"
    class="mt-0"
    data-aos="fade-up"
    data-aos-offset="200"
    data-aos-delay="50"
    data-aos-duration="1000"
    data-aos-easing="ease-in-out"
    data-aos-mirror="true"
    data-aos-once="true"
    data-aos-anchor-placement="top-center"
  >
    <Layout>
      <router-view />
    </Layout>
  </div>
</template>
<script>
import Layout from "./layout/Layout";

export default {
  components: { Layout }
};
</script>
<style>
#app {
  font-family: "Bai Jamjuree", "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
