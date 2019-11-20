import studentService from '../../services/studentService'
import { cloneDeep } from 'lodash'
import { baseState, baseMutations } from '../state'

const state = {
  ...cloneDeep(baseState),
  isReservedTimeSlotLoading: false,
  reservedTimeSlot: [],
  reservedRooms: [],
  roomTypes: [],
  roomNames: [],
  availableTimeSlot: null,
}

const getters = {
  getRoomNameOptions: (state) => {
    return state.roomNames.map(name => ({ 'value': name, 'text': name }))
  },
}

const mutations = {
  ...cloneDeep(baseMutations),
  setReservedRooms(state, reservedRooms) {
    state.reservedRooms = reservedRooms
  },
  setRoomTypes(state, roomTypes) {
    state.roomTypes = roomTypes
  },
  reservedTimeSlotLoading(state) {
    state.isReservedTimeSlotLoading = true
  },
  reservedTimeSlotSuccess(state) {
    state.isReservedTimeSlotLoading = false
  },
  setReservedTimeSlot(state, timeSlots) {
    state.reservedTimeSlot = timeSlots
  },
  setRoomNames(state, roomNames) {
    state.roomNames = roomNames
  },
}

const actions = {
  fetchReservedRooms({ commit }) {
    commit('loading')
    studentService.fetchReservedRooms().then(response => {
        commit('setReservedRooms', response)
        commit('success')
      },
    ).catch(err => {
      commit('error', err)
    })
  },
  fetchRoomTypes({ commit }) {
    commit('loading')
    studentService.fetchRoomTypes().then(response => {
      commit('setRoomTypes', response.data)
      commit('success')
    }).catch(err => {
      commit('error', err)
    })
  },
  fetchRoomNames({ commit }, roomType) {
    studentService.fetchRoomNameByType(roomType).then(response => {
      commit('setRoomNames', response.data.map(room => room.name))
    }).catch(err => {
      commit('error', err)
    })
  },
  fetchReservedTimeSlot({ commit }, type) {
    commit('reservedTimeSlotLoading')
    studentService.fetchReservedTimeSlot(type).then(response => {
      commit('setReservedTimeSlot', response.data)
      commit('reservedTimeSlotSuccess')
    })
  },
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
}