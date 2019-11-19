<template>
  <div>
    <Navbar/>
    <main id="main-container">
      <div class="container">
        <slot/>
      </div>
    </main>
<!--    <footer class="LayoutDefault__footer">-->
<!--      &copy; Awesome Company-->
<!--    </footer>-->
  </div>
</template>

<script>
  import Navbar from "./Navbar";
    export default {
        name: "Layout",
        components: {
          Navbar
        }
    }
</script>

<style scoped>

</style>