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
}
