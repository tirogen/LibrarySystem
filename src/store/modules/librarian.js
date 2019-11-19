import librarianService from '../../services/librarianService'
import {cloneDeep} from "lodash";
import {baseState, baseMutation} from "../state";

const state = {
  ...cloneDeep(baseState),
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
  ...cloneDeep(baseMutation),
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
