<template>
  <div v-if="isLoading" class="w-100 py-5 d-flex align-items-center justify-content-center">
    <div class="pr-3"><i class="fas fa-circle-notch fa-spin fa-2x"></i></div>
    <div><strong style="font-size: 24px">  Loading...  </strong></div>
  </div>
  <div v-else>
    <div class="pt-3">
      <h4><strong>Select Room Type</strong></h4>
    </div>
    <div class="row">
      <div v-for="roomType in roomTypes" class="col-4">
        <div :class="{'card' : true, 'selected' : selectedType === roomType.type}" @click="selectRoomType(roomType.type)">
          <div class="card-children"><i :class="getRoomTypeIcon(roomType.type)"></i></div>
          <div class="card-children"><strong>{{roomType.type}}</strong></div>
          <div class="card-children">max {{roomType.capacity}} persons</div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-6">
<!--        <b-form-select v-model="selected" :options="options"></b-form-select>-->
      </div>
      <div class="col-6">
<!--        <b-form-select v-model="selected" :options="options"></b-form-select>-->
      </div>
    </div>
  </div>
</template>

<script>
import {mapState} from "vuex";

export default {
  components: {},
  data() {
    return {
      selectedType: '',
      selectedDate: '',
      selectedTime: '',
    }
  },
  mounted() {
    this.$store.dispatch('student/fetchRoomTypes')
  },
  computed: {
    ...mapState({
      isLoading: state => state.student.isLoading,
      roomTypes: state => state.student.roomTypes,
    }),
  },
  methods: {
    getRoomTypeIcon(type) {
      switch (type) {
        case 'The Box' : return 'fas fa-bed fa-3x'
        case 'Study Room' : return 'fas fa-book fa-3x'
        case 'Seminar Room' : return 'fas fa-users fa-3x'
      }
    },
    selectRoomType(type) {
      this.selectedType = type
      this.$store.dispatch('student/getAvailableTimeSlot', type, null)
    }
  }

}
</script>

<style scoped>
h4 {
  text-align: left;
}
.card{
  color: #a7a1a7;
  background: hsla(0,0%,89%,.3);
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