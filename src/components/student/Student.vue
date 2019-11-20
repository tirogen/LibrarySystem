<template>
  <div>
    <h1>HELL YEAH <i class="fas fa-check fa-3x"></i></h1>
    <b-button variant="outline-primary">
      <router-link to="/student/reserve-room/">
        Reserve Room >
      </router-link>
    </b-button>
    {{reservedRooms}}
  </div>
</template>

<script>
import {mapState} from 'vuex'

export default {
  mounted() {
    this.$store.dispatch('student/fetchReservedRooms')
  },
  computed: {
    ...mapState({
      reservedRooms: state => state.student.reservedRooms
    }),
  },
  methods: {
  }
}
</script>

<style scoped>

</style>