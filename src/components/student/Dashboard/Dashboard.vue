<template>
  <ActiveReservation/>
</template>

<script>
import { mapState } from 'vuex'
import ActiveReservation from './ActiveReservation'
export default {
  components: {
    ActiveReservation,
  },
  mounted() {
  },
  computed: {
    ...mapState({
    }),
  },
  methods: {},
}
</script>

<style scoped>

</style>