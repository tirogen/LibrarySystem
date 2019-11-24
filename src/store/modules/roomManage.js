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

const getters = {
  rooms: state => {
    return state.rooms
  },
  librarians: state => {
    return state.librarians
  },
  roomTypes: state => {
    return state.roomTypes
  }
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
  deleteRoom({commit}, id) {
    commit('loading')
    librarianService.deleteRoom(id)
      .then(response => {
        commit('deleteRoom', {response,id})
        commit('success')
      })
  },
  updateRoom({commit}, room) {
    commit('loading')
    librarianService.updateRoom(room)
      .then(response => {
        commit('updateRoom', response)
        commit('success')
      })
  },
  addRoom({commit}, room) {
    commit('loading')
    librarianService.addRoom(room)
      .then(response => {
        commit('addRoom', response)
        commit('success')
      })
  },
}

const mutations = {
  ...cloneDeep(baseMutations),
  setRooms(state, rooms) {
    console.log('set room')
    state.rooms = rooms
    console.log(state.rooms)
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
  updateRoom(state, response) {
    if (response.status == 200) {
      let index = state.rooms.findIndex(room => {
        return room.id == response.data.id
      })
      state.rooms[index] = response.data
    }
  },
  addRoom(state, response) {
    if (response.status == 200) {
      state.rooms = response.data
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
