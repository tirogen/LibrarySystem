import roomService from '../../services/roomService'
import { cloneDeep } from 'lodash'
import {baseState, baseMutation} from "../state";

const state = {
  ...cloneDeep(baseState),
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
  ...cloneDeep(baseMutation),
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
