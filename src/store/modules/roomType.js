import librarianService from '../../services/librarianService'
import {
  cloneDeep
} from "lodash";
import {
  baseState,
  baseMutations
} from "../state";

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
  fetchRoomTypes({commit}) {
    commit('loading')
    librarianService.fetchRoomTypes()
      .then(roomTypes => {
        commit('setRoomTypes', roomTypes)
        commit('success')
      })
  },
  deleteRoomTypes({commit}, type) {
    commit('loading')
    librarianService.deleteRoomType(type)
      .then(response => {
        commit('deleteRoomType', {response,type})
        commit('success')
      })
  }
}

const mutations = {
  ...cloneDeep(baseMutations),
  setRoomTypes(state, roomTypes) {
    state.roomTypes = roomTypes
  },
  deleteRoomType(state, {response, type}) {
    if (response == 200) {
      state.roomTypes = state.roomTypes.filter(roomType => roomType.Type != type)
    }
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
