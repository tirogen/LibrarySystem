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
  roomTypes: []
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
  },
  updateRoomType({commit}, {OldType, Type, Capacity}) {
    commit('loading')
    librarianService.updateRoomType({OldType, Type, Capacity})
      .then(response => {
        commit('updateRoomType', response)
        commit('success')
      })
  },
  addRoomType({commit}, {Type, Capacity}) {
    commit('loading')
    librarianService.addRoomType({Type, Capacity})
      .then(response => {
        commit('addRoomType', response)
        commit('success')
      })
  },
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
  },
  updateRoomType(state, response) {
    if (response.status == 200) {
      let index = state.roomTypes.findIndex(roomType => {
        return roomType.Type == response.data.OldType
      })
      state.roomTypes[index] = response.data
    }
  },
  addRoomType(state, response) {
    if (response.status == 200) {
      state.roomTypes = response.data
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
