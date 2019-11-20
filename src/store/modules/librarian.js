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
  deleteReservedRoom({commit}, id) {
      librarianService.deleteReservedRoom(id)
      .then(response => {
        commit('deleteReservedRoom', {response, id})
      })
  },
  checkInReservedRoom({commit}, id) {
      librarianService.checkInReservedRoom(id)
      .then(response => {
        commit('checkInReservedRoom', {response, id})
      })
  },
  checkOutReservedRoom({commit}, id) {
      librarianService.checkOutReservedRoom(id)
      .then(response => {
        commit('checkOutReservedRoom', {response, id})
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
      state.reservedRooms = state.reservedRooms.filter(reservedRoom => reservedRoom.RoomTime_id != id)
    }
  },
  checkInReservedRoom (state, {response, id}) {
    if(response.status == 200){
      state.reservedRooms = state.reservedRooms.filter(reservedRoom => {
        if(reservedRoom.id == id) reservedRoom.TimeIn = response.data[0]
        return reservedRoom
      })
    }
  },
  checkOutReservedRoom (state, {response, id}) {
    if(response.status == 200){
      state.reservedRooms = state.reservedRooms.filter(reservedRoom => {
        if(reservedRoom.id == id) reservedRoom.TimeOut = response.data[0]
        return reservedRoom
      })
    }
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
