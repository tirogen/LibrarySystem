import roomService from '../../services/roomService'
import { cloneDeep } from 'lodash'
import { baseState, baseMutations } from '../state'

const state = {
  ...cloneDeep(baseState),
  gadgets: [],
  rooms: {},
  roomNames: [],
}

const getters = {
  rooms: state => {
    return state.rooms
  },
}

const actions = {
  fetchRoomNames({ commit }, roomType) {
    commit('setRoomNames', roomType)
  },
  fetchRooms({ commit }) {
    commit('loading')
    roomService.fetchRooms().then(rooms => {
      commit('setRooms', rooms)
      commit('success')
    }).catch(err => {
      commit('error')
    })
  },
  fetchGadgets({ commit }) {
    roomService.fetchGadgets().then(gadgets => {
      commit('setGadgets', gadgets)
    })
  },
  postGadget({ commit }, newGadget) {
    roomService.postGadget(newGadget).then(gadgets => {
      commit('setGadgets', gadgets)
    }).catch(err => {
      commit('error')
    })
  },
  deleteGadget({ commit }, id) {
    commit('loading')
    roomService.deleteGadget(id).then(res => {
      commit('deleteGad', res.data)

      // if (res.status == 200) {
      //   commit('success')
      //   commit('deleteGadget',res.data)
      // } else {
      //   commit('error')
      // }
    }).catch(err => {
      commit('error')
    })
  },
  updateGadget({ commit }, updateGadget) {
    commit('loading')
    roomService.updateGadget(updateGadget).then(res => {
      commit('updateGadgetInfo', res)
    }).catch(err => {
      commit('error ')
    })
  },
}

const mutations = {
  ...cloneDeep(baseMutations),
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
      return gadget.GadgetID == res.data.GadgetID
    })
    state.gadgets = [res.data, ...state.gadgets.filter(gadget => gadget.GadgetID !== res.data.GadgetID)]
    //state.gadgets[index] = res.data
    console.log(state.gadgets)

  },
  deleteGad(state, dat) {
    alert('deletesucc')
    state.gadgets = state.gadgets.filter((gad) => {
      if (gad.GadgetID == dat['id']) {
        console.log(dat)
        return false
      } else {
        return true
      }
    })
    // state.gadgets[index] = gd
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
}
