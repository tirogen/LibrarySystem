import studentService from "../../services/studentService";
import {cloneDeep} from 'lodash'
import {baseState, baseMutations} from "../state";

const state = {
  ...cloneDeep(baseState),
  reservedRooms: [],
  roomTypes:[]
}

const getters = {}

const mutations = {
  ...cloneDeep(baseMutations),
  setReservedRooms(state, reservedRooms) {
    state.reservedRooms = reservedRooms
  },
  setRoomTypes(state, roomTypes) {
    state.roomTypes = roomTypes
  }
}

const actions = {
  fetchReservedRooms({commit}) {
    commit('loading')
    studentService.fetchReservedRooms()
      .then(response => {
          commit('setReservedRooms', response)
        commit('success')
        }
      )
      .catch(err => {
        commit('error', err)
      })
  },
  fetchRoomTypes({commit}) {
    commit('loading')
    studentService.fetchRoomTypes()
      .then(response => {
        commit('setRoomTypes', response)
        commit('success')
      })
      .catch(err => {
        commit('error', err)
      })
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
}