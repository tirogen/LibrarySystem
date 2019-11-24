import roomService from '../../services/roomService'
import { cloneDeep } from 'lodash'
import { baseState, baseMutations } from '../state'

const state = {
  ...cloneDeep(baseState),
  gadgets: [],
  rooms: {},
  roomNames: []
}

const getters = {
  rooms: state => {
    return state.rooms
  }
}

const actions = {
  setFilter({commit}) {
    commit('setFilter')
  },
  fetchRoomNames({ commit }, roomType) {
    commit('setRoomNames', roomType)
  },
  fetchRooms({ commit }) {
    commit('loading')
    roomService.fetchRooms()
      .then(rooms => {
        commit('setRooms', rooms)
        commit('success')
      })
      .catch(err => {
        commit('error')
      })
  },
  fetchGadgets({ commit }) {
    roomService.fetchGadgets().then(gadgets => {
      commit('setGadgets', gadgets)
    })
  },
  postGadget({ commit }, newGadget) {
    roomService.postGadget(newGadget)
      .then(gadgets => {
        commit('setGadgets', gadgets)
        commit('success')
      })
      .catch(err => {
        commit('error')
      })
  },
  deleteGadget({ commit }, id) {
    commit('loading')
    roomService.deleteGadget(id)
      .then(res => {
        commit('deleteGad', res)
        // if (res.status == 200) {
          commit('success')
        //   commit('deleteGadget',res.data)
        // } else {
        //   commit('errors')
        // }
      })
      .catch(err => {
        commit('error')
      })
  },
  updateGadget({ commit }, updateGadget) {
    commit('loading')
    roomService.updateGadget(updateGadget)
      .then(res => {
        commit('updateGadgetInfo', res)
        commit('success')
      })
      .catch(err => {
        commit('error')
      })
  }
}

const mutations = {
  ...cloneDeep(baseMutations),
  setFilter(state, row) {
    state.filtered = true
    state.numRow = row
  },
  setGadgets(state, gadgets) {
    state.gadgets = gadgets
  },
  setRooms(state, rooms) {
    state.rooms = rooms
  },
  setRoomNames(state, roomType) {
    state.roomNames = Object.keys(state.rooms[roomType])
  },
  updateGadgetInfo(state, res) {
    let index = state.gadgets.findIndex(gadget => {
      return gadget.GadgetID == res["GadgetID"]
    })
    alert(index)
    // Vue.$set(state.gadgets, index, res.data)
    state.gadgets[index] = res
    const obj = {}
    state.gadgets.push(obj)
    state.gadgets.pop()
  },
  deleteGad(state, dat) {
    state.gadgets = state.gadgets.filter((gad) => gad.GadgetID != dat["id"])
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
}
