import api from '@/services/api'

export default {
  fetchbooks() {
    return api.get('/book/getBook/')
              .then(response => response.data)
  },
}
