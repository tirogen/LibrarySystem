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
      <div v-for="roomType in roomTypes" class="col-4">
        <div :class="{'card' : true, 'selected' : selectedType === roomType.type}"
             @click="selectRoomType(roomType.type)">
          <div class="card-children"><i :class="getRoomTypeIcon(roomType.type)"></i></div>
          <div class="card-children"><strong>{{roomType.type}}</strong></div>
          <div class="card-children">max {{roomType.capacity}} persons</div>
        </div>
      </div>
    </div>
    <div>{{reservedTimeSlot}}</div>
    <div>you selected {{selectedRoom}}</div>
    <div class="mt-5">
      <h6 class="mb-2"><strong>Select Room</strong></h6>
      <div class="row">
        <div class="mr-3 select-room">
          <b-form-select class="" v-model="selectedRoom" :options="roomNameOptions"></b-form-select>
        </div>
        <div>you selected {{selectedRoom}}</div>
      </div>
    </div>
    <div v-if="selectedRoom" class="mt-5">
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
    </div>
  </div>
</template>

<script>
import { mapGetters, mapState } from 'vuex'

export default {
  components: {},
  data() {
    return {
      timeSlot: [],
      selectedRoom: '',
      selectedType: '',
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
    this.$store.dispatch('student/fetchRoomTypes')
  },
  computed: {
    ...mapState({
      isLoading: state => state.student.isLoading,
      roomTypes: state => state.student.roomTypes,
      roomNames: state => state.student.roomNames,
      reservedTimeSlot: state => state.student.reservedTimeSlot,
    }),
    ...mapGetters({
      roomNameOptions: 'student/getRoomNameOptions',
    }),
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
  },

}
</script>

<style scoped>
h4, h6 {
  text-align: left;
}

.select-room {
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