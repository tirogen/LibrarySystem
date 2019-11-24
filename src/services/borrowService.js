import api from '@/services/api'

export default {
  fetchbooks() {
    return api.get('/borrow/borrow/')
      .then(response => {
        // console.log(response)
        return response.data})
  },
  deleteBook(id) {
    return api.delete(`borrow/borrow/${id}/`, { timeout: 10000 })
      .then(response => response.data)
  },
}
