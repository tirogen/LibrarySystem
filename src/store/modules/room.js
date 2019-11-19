import roomService from '../../services/roomService'

const state = {
  isLoading: false,
  isSuccess: false,
  isError: false,
  gadgets: [],
  rooms: []
}

const getters = {
  rooms: state => {
    return state.rooms
  }
}

const actions = {
  fetchRooms ({ commit }) {
    commit('loading')
    roomService.fetchRooms()
    .then(rooms => {
      console.log(rooms)
      commit('setRooms', rooms)
      commit('success')
    })
    .catch(err => {
      commit('errors')
    })
  },
  fetchGadgets ({ commit }) {
    roomService.fetchGadgets()
    .then(gadgets => {
      commit('setGadgets', gadgets)
    })
  },
  postGadget ({commit}, newGadget) {
    roomService.postGadget(newGadget)
    .then(gadgets => {
      commit('setGadgets',gadgets)
    })
    .catch(err => {
      commit('errors')
    })
  }
}

const mutations = {
  setGadgets (state, gadgets) {
    // console.log(gadgets)
    state.gadgets = gadgets
  },
  setRooms (state, rooms) {
    state.rooms = rooms
  },
  loading (state){
    state.isLoading = true
  },
  success (state){
    state.isSuccess = true,
    state.isLoading = false
  },
  errors (state) {
    state.isError = true,
    state.isLoading = false
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
