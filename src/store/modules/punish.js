import punishService from '../../services/punishService'

const state = {
  penalties: [],
  punishInfo: [],
  firstname: '',
  lastname: '',
}

const getters = {
}

const actions = {
  getAllPenalties ({ commit }) {
    punishService.fetchAllPenalties()
    .then(penalties => {
      commit('setPenalties', penalties)
    })
  },
  getPunishInfo ({ commit }, data) {
    punishService.fetchPunishInfo(data)
    .then(punishInfo => {
      commit('setPunishInfo', punishInfo)
    })
  },
  deletePenalty({commit}, id) {
    punishService.deletePenalty(id)
    .then(response => {
      commit('deletePenalty', response)
    })
  }
}

const mutations = {
  setPenalties (state, penalties) {
    state.penalties = penalties
  },
  setPunishInfo (state, punishInfo) {
    state.punishInfo = punishInfo
  },
  deletePenalty(state, response){
    if(response.status == 200){
      state.penalties = state.penalties.filter((penalty) => penalty.id != response.data.id)
    }
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
