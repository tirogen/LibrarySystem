import api from '@/services/api'

export default {
  fetchReservedRooms() {
    return api.get(`reservedRoom/getReservedRooms/`)
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

  fetchRoomTypes() {
    return api.get(`manageRoom/roomTypes/`)
              .then(response => response.data)
  },
  deleteRoomType(type) {
    return api.delete(`manageRoom/roomTypes/${type}/`)
              .then(response => response.status)
  },
}
