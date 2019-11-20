import librarianService from '../../services/librarianService'
import {cloneDeep} from "lodash";
import {baseState, baseMutations} from "../state";

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
  deleteReservedRooms({commit}, id) {
      librarianService.deleteReservedRoom(id)
      .then(response => {
        commit('deleteReservedRoom', {response, id})
      })
  }
}

const mutations = {
  ...cloneDeep(baseMutations),
  setReservedRooms (state, reservedRooms) {
    state.reservedRooms = reservedRooms
  },
  deleteReservedRoom (state, {response, id}) {
    if(response == 200){
      state.reservedRooms = state.reservedRooms.filter(reservedRoom => reservedRoom.id != id)
    }
    //state.reservedRooms = reservedRooms
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
