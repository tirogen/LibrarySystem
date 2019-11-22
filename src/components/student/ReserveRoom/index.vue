<template>
  <div v-if="isLoading" class="w-100 my-5 d-flex align-items-center justify-content-center">
    <div class="pr-3"><i class="fas fa-circle-notch fa-spin fa-2x"></i></div>
    <div><strong style="font-size: 24px"> Loading... </strong></div>
  </div>
  <div v-else>
    <div class="mt-3">
      <h4><strong>Select Room Type</strong></h4>
    </div>
    <div class="row">
      <div v-for="roomType in roomTypes" :key="roomType.type" class="col-4">
        <div :class="{'card' : true, 'selected' : selectedType === roomType.type}"
             @click="selectRoomType(roomType.type)">
          <div class="card-children"><i :class="getRoomTypeIcon(roomType.type)"></i></div>
          <div class="card-children"><strong>{{roomType.type}}</strong></div>
          <div class="card-children">max {{roomType.capacity}} persons</div>
        </div>
      </div>
    </div>
    <div>{{reservedTimeSlot}}</div>
    <div>{{timePeriodOptions}}</div>
    <div>you selected {{selectedRoom}}</div>
    <div>you selected {{selectedTimePeriod}}</div>
    <div class="mt-5">
      <div class="row">
        <div class="col-sm-4">
          <h6 class="mb-2"><strong>Select Room</strong></h6>
          <div class="mr-3 ">
            <b-form-select class="" v-model="selectedRoom" :options="roomNameOptions"></b-form-select>
          </div>
        </div>
        <div class="col-sm-4">
          <h6 class="mb-2"><strong>Select Duration</strong></h6>
          <div class="mr-3 ">
            <b-form-select class="" v-model="selectedDuration" :options="durationOptions"></b-form-select>
          </div>
        </div>
        <div class="col-sm-4">
          <h6 class="mb-2"><strong>Select Time</strong></h6>
          <div class="mr-3 ">
            <b-form-select class="" v-model="selectedTimePeriod" :options="timePeriodOptions"></b-form-select>
          </div>
        </div>
      </div>
    </div>
    <div v-if="selectedRoom" class="my-5 col-sm-12">
      <h6 class="mb-2"><strong>Require Student ID</strong></h6>
      <div class="row">
        <div class="mr-3 student-id-input">
          <b-form-input v-model="student1.id" placeholder="Enter your name"></b-form-input>
        </div>
        <div class="student-name">
          Name for student1 {{student1.id}}
        </div>
      </div>
      <div v-if="selectedType !== 'The Box'" class="row">
        <div class="mr-3 student-id-input">
          <b-form-input v-model="student2.id" placeholder="Enter your name"></b-form-input>
        </div>
        <div class="student-name">
          Name for student2 {{student2.id}}
        </div>
      </div>
      <div v-if="selectedType !== 'The Box'" class="row">
        <div class="mr-3 student-id-input">
          <b-form-input v-model="student3.id" placeholder="Enter your name"></b-form-input>
        </div>
        <div class="student-name">
          Name for student3 {{student3.id}}
        </div>
      </div>
      <div v-if="selectedType !== 'The Box'" class="row">
        <div class="mr-3 student-id-input">
          <b-form-input v-model="student4.id" placeholder="Enter your name"></b-form-input>
        </div>
        <div class="student-name">
          Name for student4 {{student4.id}}
        </div>
      </div>
      <div v-if="selectedType === 'Seminar Room'" class="row">
        <div class="mr-3 student-id-input">
          <b-form-input v-model="student5.id" placeholder="Enter your name"></b-form-input>
        </div>
        <div class="student-name">
          Name for student5 {{student5.id}}
        </div>
      </div>
      <div v-if="selectedType === 'Seminar Room'" class="row">
        <div class="mr-3 student-id-input">
          <b-form-input v-model="student6.id" placeholder="Enter your name"></b-form-input>
        </div>
        <div class="student-name">
          Name for student6 {{student6.id}}
        </div>
      </div>
      <b-button pill variant="outline-secondary" class="my-3" @click="bookForRoom()" :disabled="!validateFormSubmit()">
        Confirm and Reserve
      </b-button>
    </div>
    <div class="d-flex">
    </div>
  </div>
</template>

<script>
import { mapGetters, mapState } from 'vuex'
import moment from 'moment'

export default {
  components: {},
  data() {
    return {
      timeSlot: [],
      selectedRoom: '',
      selectedType: '',
      selectedDuration: 30,
      selectedTimePeriod: '',
      durationOptions: [
        { 'value': 30, 'text': '30 minutes' },
        { 'value': 60, 'text': '60 minutes' },
        { 'value': 90, 'text': '90 minutes' },
        { 'value': 120, 'text': '120 minutes' }],
      student1: { id: '', name: '' },
      student2: { id: '', name: '' },
      student3: { id: '', name: '' },
      student4: { id: '', name: '' },
      student5: { id: '', name: '' },
      student6: { id: '', name: '' },
      form: {
        startTime: '',
        endTime: '',
        date: '',
        roomId: '',
        studentId: '',
        friendIds: [],
      },
    }
  },
  mounted() {
    this.$store.dispatch('student/initializeState')
    this.$store.dispatch('student/fetchRoomTypes')
  },
  computed: {
    ...mapState({
      isLoading: state => state.student.isLoading,
      roomTypes: state => state.student.roomTypes,
      roomNames: state => state.student.roomNames,
      reservedTimeSlot: state => state.student.reservedTimeSlot,
      timeSlots: state => state.student.timeSlots,
    }),
    ...mapGetters({
      roomNameOptions: 'student/getRoomNameOptions',
    }),
    timePeriodOptions() {
      if (!this.selectedRoom) return [{ 'value': null, 'text': 'Please Select Room First', 'disabled': true }]
      if (!this.selectedRoom) return [{ 'value': null, 'text': 'Please Select Room First', 'disabled': true }]
      return this.getAvailableTimePeriods()
    },
  },
  methods: {
    getRoomTypeIcon(type) {
      switch (type) {
        case 'The Box' :
          return 'fas fa-bed fa-3x'
        case 'Study Room' :
          return 'fas fa-book fa-3x'
        case 'Seminar Room' :
          return 'fas fa-users fa-3x'
      }
    },
    selectRoomType(type) {
      this.selectedType = type
      this.selectedRoom = ''
      this.$store.dispatch('student/fetchRoomNames', type)
      this.$store.dispatch('student/fetchReservedTimeSlot', type)
    },
    bookForRoom() {
      this.$store.dispatch('student/bookForRoom', this.getSubmissionForm())
    },
    getSubmissionForm() {
      return this.form
    },
    validateFormSubmit() {
      if (!this.selectedType || !this.selectedRoom) return false
      if (this.selectedType !== 'The Box' && !(this.student2.id && this.student3.id && this.student4.id)) return false
      if (this.selectedType === 'Seminar Room' && !(this.student5.id && this.student6.id)) return false
      return this.student1.id !== ''
    },
    getAvailableTimePeriods() {
      const timePeriod = [], timeSlots = this.timeSlots, reservedTimeSlot = this.reservedTimeSlot
      const reservedTime = reservedTimeSlot.filter(slot => slot.name === this.selectedRoom)

      timeSlots.forEach(slot => {
        const startArr = slot.start.split(':').map(e => parseInt(e))
        const endArr = slot.end.split(':').map(e => parseInt(e))
        const slotStart = moment().hours(startArr[0]).minutes(startArr[1])
        const slotEnd = moment().hours(endArr[0]).minutes(endArr[1])
        reservedTime.forEach(reserved => {
          const reservedStartArr = reserved['start_time'].split(':').map(e => parseInt(e))
          const reservedEndArr = reserved['end_time'].split(':').map(e => parseInt(e))
          const reservedStart = moment().hours(reservedStartArr[0]).minutes(reservedStartArr[1])
          const reservedEnd = moment().hours(reservedEndArr[0]).minutes(reservedEndArr[1])
          if (reservedStart <= slotStart && slotEnd <=
            reservedEnd) slot.available = false
        })
      })
      const periods = this.generateTimePeriods(this.selectedDuration / 30, timeSlots)
      return periods
    },
    generateTimePeriods(slotNeeds, timeSlots) {
      const periods = []
      for (let i = 0; i < timeSlots.length - slotNeeds + 1; i++) {
        let flag = true
        for (let j = 0; j < slotNeeds; j++) {
          if (!timeSlots[i + j].available) flag = false
        }
        if (flag) {
          const option = `${timeSlots[i].start} - ${timeSlots[i + slotNeeds - 1].end}`
          periods.push({
            'value': option, 'text': option,
          })
        }
      }
      return periods
    },
  },

}
</script>

<style scoped>
h4, h6 {
  text-align: left;
}

.dropdown-options {
  min-width: 20%;
}

.student-id-input {
  min-width: 20%;
}

.row {
  align-items: center;
  margin: 0.25rem 0;
}

.card {
  color: #a7a1a7;
  background: hsla(0, 0%, 89%, .3);
  border: 1px solid #e2e2e2;
  transition: 0.3s;
}

.card:hover {
  cursor: pointer;
  color: white;
  background: #a7a1a7;
  transition: 0.3s;
}

.card-children {
  margin: 0.5rem 0;
}

.selected {
  color: white;
  background: #565656 !important;
}

</style>