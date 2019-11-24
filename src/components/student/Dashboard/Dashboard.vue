<template>
  <div class="container">
    <ActiveReservation/>
    <BorrowingList/>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import ActiveReservation from './ActiveReservation'
import BorrowingList from '../BorrowingList/BorrowingList'
export default {
  components: {
    ActiveReservation,
    BorrowingList
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