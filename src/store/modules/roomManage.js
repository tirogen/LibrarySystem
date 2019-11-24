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
  rooms: [],
  librarians: [],
  roomTypes: []
}

const actions = {
  fetchRooms({commit}) {
    commit('loading')
    librarianService.fetchRooms()
      .then(rooms => {
        commit('setRooms', rooms)
        commit('success')
      })
  },
  fetchLibrarians({commit}) {
    commit('loading')
    librarianService.fetchLibrarians()
      .then(librarians => {
        commit('setLibrarians', librarians)
        commit('success')
      })
  },
  fetchRoomTypes({commit}) {
    commit('loading')
    librarianService.fetchRoomTypes()
      .then(roomTypes => {
        commit('setRoomTypes', roomTypes)
        commit('success')
      })
  },
  deleteRoomType({commit}, id) {
    commit('loading')
    librarianService.deleteRoom(id)
      .then(response => {
        commit('deleteRoom', {response,id})
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
  setRooms(state, rooms) {
    state.rooms = rooms
  },
  setLibrarians(state, librarians) {
    state.librarians = librarians
  },
  setRoomTypes(state, roomTypes) {
    state.roomTypes = roomTypes
  },
  deleteRoom(state, {response, id}) {
    if (response == 200) {
      state.rooms = state.rooms.filter(room => room.id != id)
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
