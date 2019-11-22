import api from '@/services/api'
import moment from 'moment'

export default {
  fetchReservedRooms() {
    return api.get(`reservedRoom/getTop20/`).then(response => response.data)
  },

  fetchRoomTypes() {
    return api.get('room/types/')
  },

  fetchReservedTimeSlot(type) {
    const date = moment().format('YYYY-MM-DD')
    return api.get(`room/${type}/${date}/`)
  },

  fetchRoomNameByType(type) {
    return api.get(`room/names/${type}/`)
  },

  bookForRoom(form) {
    return api.post(`room/bookForRoom/`, form)
  }
}