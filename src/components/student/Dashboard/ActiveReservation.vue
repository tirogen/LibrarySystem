<template>
  <div>
    <b-button variant="outline-primary" class="scaleup-btn my-5">
      <i class="fas fa-check"></i>
      <router-link to="/student/reserve-room/" class="router-linker">
        Reserve Room >
      </router-link>
    </b-button>
  </div>
</template>

<script>
export default {
}
</script>

<style scoped>
.scaleup-btn {
  transition: 0.2s;
}

.scaleup-btn:hover {
  background-color: white;
  color: #007bff;
  transform: scale(1.2);
  transition: 0.2s;
}

.router-linker {
  color: #007bff;
  text-decoration: none;
}
</style>