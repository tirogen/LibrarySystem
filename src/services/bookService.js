import api from '@/services/api'

export default {
  fetchbooks() {
    return api.get('/book/book/')
      .then(response => {
        // console.log(response)
        return response.data
      }
      )
  },
  deleteBook(id) {
    return api.delete(`book/book/${id}/`, { timeout: 10000 })
      .then(response => response.data)
  },
  postBook(data) {
    return api.post(`book/book/`, data, { timeout: 10000 })
      .then(response => response.data)
  },
}
