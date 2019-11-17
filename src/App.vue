<template>
  <div id="app">
    <b-container>
      <div id="nav">
       <router-link :to="{ name: 'home' }">Home</router-link> |
       <router-link :to="{ name: 'student' }">Student</router-link> |
       <router-link :to="{ name: 'librarian' }">Librarian</router-link>
      </div>
      <router-view/>
    </b-container>
  </div>
</template>

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
