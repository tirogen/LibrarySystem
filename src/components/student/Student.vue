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
import {mapState, mapActions} from 'vuex'

export default {
  mounted() {
    this.fetchReservedRooms()
  },
  computed: mapState({
    reservedRooms: state => state.student.reservedRooms
  }),
  methods: {
    ...mapActions({
      fetchReservedRooms: 'student/fetchReservedRooms'
    })
  }
}
</script>

<style scoped>

</style>