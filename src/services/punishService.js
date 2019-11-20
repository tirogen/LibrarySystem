import api from '@/services/api'

export default {
  fetchAllPenalties() {
    return api.get(`punish/penalty`, {timeout: 10000})
              .then(response => response.data)
  },
  fetchPunishInfo(FName, LName) {
    return api.get(`punish/getPunishInfo/${FName}/${LName}/`)
              .then(response => response.data)
  }
}
