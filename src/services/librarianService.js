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
  updateRoomType(roomType) {
    return api.put('manageRoom/roomTypes/',JSON.stringify(roomType)).then(response => response)
  },
  addRoomType(roomType) {
    return api.post('manageRoom/roomTypes/',JSON.stringify(roomType)).then(response => response)
  },

  fetchRooms() {
    return api.get(`manageRoom/rooms/`).then(response => response.data)
  },
  fetchLibrarians() {
    return api.get(`manageRoom/librarians/`).then(response => response.data)
  },
  deleteRoom(id) {
    return api.delete(`manageRoom/rooms/${id}/`).then(response => response.status)
  },
  updateRoom(room) {
    return api.put('manageRoom/rooms/',JSON.stringify(room)).then(response => response)
  },
  addRoom(room) {
    return api.post('manageRoom/rooms/',JSON.stringify(room)).then(response => response)
  },
}
