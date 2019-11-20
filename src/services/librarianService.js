import api from '@/services/api'

export default {
  fetchReservedRooms() {
    return api.get(`reservedRoom/getTop20/`)
              .then(response => response.data)
  },
  deleteReservedRoom(id) {
    return api.delete(`reservedRoom/delete/${id}/`)
              .then(response => response.status)
  },
  checkInReservedRoom(id) {
    return api.patch(`reservedRoom/checkIn/${id}/`)
              .then(response => response)
  },
  checkOutReservedRoom(id) {
    return api.patch(`reservedRoom/checkOut/${id}/`)
              .then(response => response)
  },
}
