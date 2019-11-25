import api from '@/services/api'

export default {
  fetchBorrow() {
    return api.get('/borrow/borrow/')
      .then(response => {
        // console.log(response)
        return response.data})
  },
  deleteBorrow(id) {
    return api.delete(`borrow/borrow/${id}/`, { timeout: 10000 })
      .then(response => response.data)
  },
  postBorrow(obj) {
    // console.log(obj)
    return api.post('borrow/borrow/',obj)
      .then(response => response.data)
  },
  getCalculate(id) {
    return api.post(`punish/calculatePoint/${id}/`)
  }
}
