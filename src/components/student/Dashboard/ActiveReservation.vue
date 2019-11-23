<template>
  <div class="my-container">
    <b-modal id="prompt-cancel-modal" title="Confirm cancellation">
      <div>
        <div><strong>Room: {{currentPromptForCancel.Room}}</strong></div>
        <div><strong>Time: {{currentPromptForCancel.Time}}</strong></div>
        <div>Are you sure you want to cancel this reservation?</div>
        <div>This action cannot be undone.</div>
      </div>
      <template v-slot:modal-footer>
        <div class="row">
          <b-button variant="primary" @click="processCancelReservation()" style="min-width: 100px">
            CONFIRM
          </b-button>
          <b-button variant="outline-secondary" class="mx-2" @click="resetPromptForCancel()" style="min-width: 100px">
            CANCEL
          </b-button>
        </div>
      </template>
    </b-modal>
    <div style="font-size: 24px"><strong>Your Active Reservation</strong></div>
    <div v-if="!activeReservation">You have no active reservation</div>
    <div v-for="reservation in mappedActiveReservation" class="row  my-2" v-else>
      <div class="col-sm-4"><strong>Room: </strong>{{reservation.Room}}</div>
      <div class="col-sm-4"><strong>Time: </strong>{{reservation.Time}}</div>
      <div class="col-sm-4">
        <b-button variant="danger" size="sm" @click="promptCancelReservation(reservation)">
          CANCEL
        </b-button>
      </div>
    </div>
    <div class="row align-items-center">
      <b-button variant="outline-primary" class="scaleup-btn" :disabled="activeReservation" style="margin-left: 15px" @click="goToReserveRoom()">
        <i class="fas fa-check"></i> Reserve Room >
      </b-button>
      <p class="text-danger" v-if="activeReservation" style="margin: auto 0.5rem">You can have only one active reservation</p>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  data() {
    return {
      currentPromptForCancel: {},
    }
  },
  mounted() {
    this.$store.dispatch('student/fetchActiveReservation', 'student1')
  },
  computed: {
    ...mapState({
      activeReservation: state => state.student.activeReservation,
    }),
    mappedActiveReservation() {
      return this.activeReservation.map(reservation => {
        const start = reservation.startTime[0] === '0' ? reservation.startTime.slice(1, 5) : reservation.startTime.slice(0, 5)
        const end = reservation.endTime[0] === '0' ? reservation.endTime.slice(1, 5) : reservation.endTime.slice(0, 5)
        return {
          'Room': reservation.roomName,
          'Time': `${start} - ${end}`,
          'ID': reservation.reservationId,
        }
      })
    },
  },
  methods: {
    processCancelReservation() {
      console.log(`canceling id ${this.currentPromptForCancel.ID}`)
      this.$store.dispatch('student/cancelReservation', this.currentPromptForCancel.ID)
      this.resetPromptForCancel()
    },
    promptCancelReservation(reservation) {
      this.currentPromptForCancel = reservation
      this.$bvModal.show('prompt-cancel-modal')
    },
    resetPromptForCancel() {
      this.currentPromptForCancel = {}
      this.$bvModal.hide('prompt-cancel-modal')
    },
    goToReserveRoom() {
      this.$router.push({path:'student/reserve-room'})
    }
  },
}
</script>

<style scoped>
.my-container {
  width: 75%;
  margin: 2rem auto;
  text-align: left;
}

.scaleup-btn {
  transition: 0.2s;
}

.scaleup-btn:hover {
  color: white;
  background-color: #007bff;
  /*transform: scale(1.2);*/
  transition: 0.2s;
}

.router-linker {
  color: #007bff;
  text-decoration: none;
}
</style>