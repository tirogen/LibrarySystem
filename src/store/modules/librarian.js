import librarianService from '../../services/librarianService'

const state = {
  reservedRooms: []
}

const getters = {
  reservedRooms: state => {
    return state.reservedRooms
  }
}

const actions = {
  getReservedRooms ({ commit }) {
    librarianService.fetchReservedRooms()
    .then(reservedRooms => {
      commit('setReservedRooms', reservedRooms)
    })
  },
}

const mutations = {
  setReservedRooms (state, reservedRooms) {
    state.reservedRooms = reservedRooms
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
