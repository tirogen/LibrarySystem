import studentService from "../../services/studentService";
import {cloneDeep} from 'lodash'
import {baseState, baseMutations} from "../state";

const state = {
  ...cloneDeep(baseState),
  reservedRooms: [],
  roomTypes:[],
  availableTimeSlot: null,
}

const getters = {}

const mutations = {
  ...cloneDeep(baseMutations),
  setReservedRooms(state, reservedRooms) {
    state.reservedRooms = reservedRooms
  },
  setRoomTypes(state, roomTypes) {
    state.roomTypes = roomTypes
  },
  setAvailableTimeSlot(state, timeSlots) {
    state.availableTimeSlot = timeSlots
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
  },
  getAvailableTimeSlot({commit}, type, date) {
    studentService.getAvailableTimeSlot(type, date)
      .then(response => {
        console.log(response)
        commit('setAvailableTimeSlot', response)
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