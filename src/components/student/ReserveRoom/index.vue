<template>
  <div v-if="isLoading" class="w-100 my-5 d-flex align-items-center justify-content-center">
    <div class="pr-3"><i class="fas fa-circle-notch fa-spin fa-2x"></i></div>
    <div><strong style="font-size: 24px"> Loading... </strong></div>
  </div>
  <div v-else>
    <div>
      <b-modal id="reserve-room-confirm-modal" title="Confirm Reservation">
        <div>
          <div class="row">Type: {{selectedType}}</div>
          <div class="row">Room: {{selectedRoom}}</div>
          <div class="row">Duration: {{selectedDuration}}</div>
          <div class="row">Time: {{selectedTimePeriod}}</div>
        </div>
        <template v-slot:modal-footer>
          <div>
            <div class="row w-100" v-if="reservationError">
              <p class="text-danger"><strong>Room reservation failed.</strong></p>
            </div>
            <div class="row w-100" v-if="reservationSuccess">
              <p class="text-primary"><strong>Room reservation successful</strong></p>
            </div>
            <div class="row" v-if="!reservationSuccess && !reservationError">
              <b-button variant="primary" @click="bookForRoom()" style="min-width: 100px">
                <div v-if="reservationInProgress"><i class="fas fa-circle-notch fa-spin"></i></div>
                <div v-else>CONFIRM</div>
              </b-button>
              <b-button variant="outline-secondary" class="ml-2" @click="$bvModal.hide('reserve-room-confirm-modal')" style="min-width: 100px">
                CANCEL
              </b-button>
            </div>
            <div class="row" v-else>
              <b-button variant="outline-secondary" class="ml-2" @click="$router.push({path:'/student'})" style="min-width: 100px">
                Back to Student Home
              </b-button>
            </div>
          </div>
        </template>
      </b-modal>
    </div>
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
<!--    <div>{{reservedTimeSlot}}</div>-->
<!--    <div>{{timePeriodOptions}}</div>-->
<!--    <div>you selected {{selectedRoom}}</div>-->
<!--    <div>you selected {{selectedTimePeriod}}</div>-->
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
          <b-form-input v-model="student1.id" :onChange="setStudentNameOnInput(1)" placeholder="Enter your name"></b-form-input>
        </div>
        <div class="student-name">
          {{student1.name}}
        </div>
      </div>
      <div v-if="selectedType !== 'The Box'" class="row">
        <div class="mr-3 student-id-input">
          <b-form-input v-model="student2.id" :onChange="setStudentNameOnInput(2)" placeholder="Enter your name"></b-form-input>
        </div>
        <div class="student-name">
          {{student2.name}}
        </div>
      </div>
      <div v-if="selectedType !== 'The Box'" class="row">
        <div class="mr-3 student-id-input">
          <b-form-input v-model="student3.id" :onChange="setStudentNameOnInput(3)" placeholder="Enter your name"></b-form-input>
        </div>
        <div class="student-name">
          {{student3.name}}
        </div>
      </div>
      <div v-if="selectedType !== 'The Box'" class="row">
        <div class="mr-3 student-id-input">
          <b-form-input v-model="student4.id" :onChange="setStudentNameOnInput(4)" placeholder="Enter your name"></b-form-input>
        </div>
        <div class="student-name">
          {{student4.name}}
        </div>
      </div>
      <div v-if="selectedType === 'Seminar Room'" class="row">
        <div class="mr-3 student-id-input">
          <b-form-input v-model="student5.id" :onChange="setStudentNameOnInput(5)" placeholder="Enter your name"></b-form-input>
        </div>
        <div class="student-name">
          {{student5.name}}
        </div>
      </div>
      <div v-if="selectedType === 'Seminar Room'" class="row">
        <div class="mr-3 student-id-input">
          <b-form-input v-model="student6.id" :onChange="setStudentNameOnInput(6)" placeholder="Enter your name"></b-form-input>
        </div>
        <div class="student-name">
          {{student6.name}}
        </div>
      </div>
      <b-button pill v-b-modal.reserve-room-confirm-modal variant="outline-secondary" class="my-3" :disabled="!validateFormSubmit()">
        Reserve
      </b-button>
    </div>
    <div class="d-flex">
    </div>
  </div>
</template>

<script>
import { mapGetters, mapState } from 'vuex'
import moment from 'moment'
import studentService from '../../../services/studentService'

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
      student1: { id: 'student1', name: '' },
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
      waitTime: 0,
    }
  },
  mounted() {
    this.$store.dispatch('student/initializeState')
    this.$store.dispatch('student/fetchRoomTypes')
    this.setStudentNameOnInput(1)
  },
  computed: {
    ...mapState({
      isLoading: state => state.student.isLoading,
      roomTypes: state => state.student.roomTypes,
      roomNames: state => state.student.roomNames,
      reservedTimeSlot: state => state.student.reservedTimeSlot,
      timeSlots: state => state.student.timeSlots,
      reservationInProgress: state => state.student.reservationInProgress,
      reservationSuccess: state => state.student.reservationSuccess,
      reservationError: state => state.student.reservationError,
    }),
    ...mapGetters({
      getRoomNameOptions: 'student/getRoomNameOptions',
    }),
    roomNameOptions() {
      if (!this.selectedType) return [{ 'value': null, 'text': 'Please Select Room Type First', 'disabled': true }]
      return this.getRoomNameOptions
    },
    timePeriodOptions() {
      if (!this.selectedRoom) return [{ 'value': null, 'text': 'Please Select Room First', 'disabled': true }]
      return this.getAvailableTimePeriods()
    },
    redirectTime() {
      return this.waitTime
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
      this.getSubmissionForm()
      this.$store.dispatch('student/bookForRoom', this.form)
    },
    getSubmissionForm() {
      this.form.date = moment().format('YYYY-MM-DD')
      this.form.startTime = this.selectedTimePeriod.split(' - ')[0]
      this.form.endTime = this.selectedTimePeriod.split(' - ')[1]
      this.form.roomId = this.roomNames.filter(room => room.name === this.selectedRoom).map(room => room.roomId)[0]
      this.form.studentId = this.student1.id
      this.form.friendIds = []
      if (this.selectedType !== 'The Box') this.form.friendIds.push(this.student2.id, this.student3.id, this.student4.id)
      if (this.selectedType === 'Seminar Room') this.form.friendIds.push(this.student5.id, this.student6.id)
      return this.form
    },
    validateFormSubmit() {
      if (!this.selectedType || !this.selectedRoom || !this.selectedTimePeriod) return false
      if (this.selectedType !== 'The Box' && !(this.student2.id && this.student3.id && this.student4.id)) return false
      if (this.selectedType === 'Seminar Room' && !(this.student5.id && this.student6.id)) return false
      return this.student1.id !== ''
    },
    getAvailableTimePeriods() {
      const timeSlots = this.timeSlots, reservedTimeSlot = this.reservedTimeSlot
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
    async setStudentNameOnInput(inputNumber) {
      const inputKey = `student${inputNumber}`
      const studentId = this[inputKey].id
      if (studentId.length === 8 && studentId.slice(0, 7) === 'student') {
        let result = ''
        await studentService.getStudentName(studentId).then(response => {
          if (response.status === 204) result = 'Not Found'
          else {
            const data = response.data[0]
            result = `${data.Firstname} ${data.Lastname}`
          }
        }).catch(err => {
          console.error(err)
        })
        this[inputKey].name = result
      } else {
        this[inputKey].name = 'Invalid ID'
      }
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
    sleep(milliseconds) {
      let start = new Date().getTime()
      for (let i = 0; i < 1e7; i++) {
        if ((new Date().getTime() - start) > milliseconds) break
      }
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