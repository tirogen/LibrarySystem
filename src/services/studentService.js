import api from '@/services/api'

export default {
  fetchReservedRooms() {
    return api.get(`reservedRoom/getTop20/`)
              .then(response => response.data)
  },

  fetchRoomTypes(){
    return api.get('room/roomTypes').then(response => response.data)
  },

  fetchReservedTimeSlot(type, date){
    return api.get(`room/${type}/0`).then(response => response.data)
  }
}