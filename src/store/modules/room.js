import roomService from '../../services/roomService'
import { cloneDeep } from 'lodash'
import {baseState, baseMutations} from "../state";

const state = {
  ...cloneDeep(baseState),
  gadgets: [],
  rooms: {},
  roomNames: [],
}

const getters = {
  rooms: state => {
    return state.rooms
  }
}

const actions = {
  fetchRoomNames ({commit}, roomType) {
    commit('setRoomNames',roomType)
  },
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
  },
  deleteGadget ({commit}, id) {
    commit('loading')
    roomService.deleteGadget(id)
    .then(res => {
      commit('setGadgets',gadgets)
      // console.log(res)
      // check status
      if (res.status == "") {
        commit('success')
      } else {
        commit('errors')
      }
    })
    .catch(err => {
      commit('errors')
    })
  },
  updateGadget ({commit}, updateGadget) {
    commit('loading')
    roomService.updateGadget(updateGadget)
    .then(res => {
      if (res.status == 200) {
        commit('success')
        commit('updateGadget',res.data)
      } else {
        commit('errors')
      }
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
  setRoomNames(state, roomType) {
    state.roomNames = Object.keys(state.rooms[roomType])
  },
  updateGadget(state,gadget) {
    let index = state.gadgets.findIndex(gadget => gadget.id == gadget.id);
    // console.log(gadget)
    state.gadgets[index] = gadget
    // state.rooms[index].Name = response.data.Name;
    // state.rooms[index].Point = response.data.Point;
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
