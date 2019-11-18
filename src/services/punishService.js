import api from '@/services/api'

export default {
  fetchAllPenalty() {
    return api.get(`punish/getAllPenalty/`)
              .then(response => response.data)
  },
}
