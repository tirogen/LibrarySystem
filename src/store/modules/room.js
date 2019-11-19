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
  fectchRooms ({ commit }) {
    commit('loading')
    roomService.fectchRooms()
    .then(rooms => {
      commit('setRooms', rooms)
      commit('success')
    })
    .catch(err => {
      commit('error')
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
  }
}

const mutations = {
  setGadgets (state, gadgets) {
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
