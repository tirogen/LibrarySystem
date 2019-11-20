<template>
  <div>
    <h1><i class="fas fa-check"></i></h1>
    <b-button variant="outline-primary">
      <router-link to="/student/reserve-room/">
        Reserve Room >
      </router-link>
    </b-button>
    <div>
      {{reservedRooms}}
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  mounted() {
    this.$store.dispatch('student/fetchReservedRooms')
  },
  computed: {
    ...mapState({
      reservedRooms: state => state.student.reservedRooms,
    }),
  },
  methods: {},
}
</script>

<style scoped>

</style>