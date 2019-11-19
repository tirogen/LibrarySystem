import roomService from '../../services/roomService'
import { cloneDeep } from 'lodash'
import {baseState, baseMutations} from "../state";

const state = {
  ...cloneDeep(baseState),
  gadgets: [],
  rooms: {}
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
  ...cloneDeep(baseMutations),
  setGadgets (state, gadgets) {
    state.gadgets = gadgets
  },
  setRooms (state, rooms) {
    state.rooms = rooms
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
