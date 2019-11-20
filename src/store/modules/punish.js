import punishService from '../../services/punishService'

const state = {
  penalties: [],
  firstname: '',
  lastname: '',
}

const getters = {
  penalties: state => {
    return state.penalties
  },
  punishInfo: state => {
    return state.punishInfo
  }
}

const actions = {
  getAllPenalties ({ commit }) {
    punishService.fetchAllPenalties()
    .then(penalties => {
      commit('setPenalties', penalties)
    })
  },
  getPunishInfo ({ commit }) {
    punishService.fetchPunishInfo()
    .then(punishInfo => {
      commit('setPunishInfo', punishInfo)
    })
  }
}

const mutations = {
  setPenalties (state, penalties) {
    state.penalties = penalties
  },
  setPunishInfo (state, punishInfo) {
    state.punishInfo = punishInfo
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
