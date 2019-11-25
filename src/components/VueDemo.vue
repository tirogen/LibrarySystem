<template>
<div class="hello">
  <h1 class="mt-4 mb-4">Library System : Bee Group</h1>
  <b-row>
    <b-col cols="8">
      <img src="@/assets/591953.jpg" class="img-fluid"></img>
    </b-col>
    <b-col>
      <img src="@/assets/B.jpg" class="img-fluid"></img>
    </b-col>
  </b-row>
</div>
</template>

<script>
import Layout from "../layout/Layout";

export default {
  name: 'VueDemo',
  comments: {
    Layout,
  },
  props: {}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
