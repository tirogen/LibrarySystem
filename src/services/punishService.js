import api from '@/services/api'

export default {
  fetchAllPenalties() {
    return api.get(`punish/penalty`, {timeout: 10000})
              .then(response => response.data)
  },
  fetchPunishInfo(data) {
    return api.get(`punish/getPunishInfo/${data.firstname}/${data.lastname}/`, {timeout: 10000})
              .then(response => response.data)
  },
  deletePenalty(id){
    return api.delete(`punish/penalty/${id}/`, {timeout: 10000})
              .then(response => response)
  },
  deletePunish(id){
    return api.delete(`punish/punish/${id}/`, {timeout: 10000})
              .then(response => response)
  },
  postPunish(data){
    return api.post(`punish/punish/`, data,{timeout: 10000})
              .then(response => response)
  }
}
