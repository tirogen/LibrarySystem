import punishService from '../../services/punishService'

const state = {
  penalties: []
}

const getters = {
  penalties: state => {
    return state.penalties
  }
}

const actions = {
  GetAllPenalties ({ commit }) {
    punishService.fetchAllPenalties()
    .then(penalties => {
      commit('setPenalties', penalties)
    })
  },
}

const mutations = {
  setPenalties (state, penalties) {
    state.penalties = penalties
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
