import punishService from '../../services/punishService'

const state = {
  penalty: []
}

const getters = {
  penalty: state => {
    return state.penalty
  }
}

const actions = {
  getAllPenalty ({ commit }) {
      console.log("here");
    punishService.fetchAllPenalty()
    .then(penalty => {
        console.log(penalty);
      commit('setPenalty', penalty)
    })
  },
}

const mutations = {
  setPenalty (state, penalty) {
    state.penalty = penalty
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
