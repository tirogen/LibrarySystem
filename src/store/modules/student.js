/* eslint-disable */
import studentService from '../../services/studentService'
import { cloneDeep } from 'lodash'
import { baseState, baseMutations } from '../state'
import moment from 'moment'

const state = {
  ...cloneDeep(baseState),
  isReservedTimeSlotLoading: false,
  reservedTimeSlot: [],
  reservedRooms: [],
  roomTypes: [],
  roomNames: [],
  timeSlots: [],
  activeReservation: [],
  reservationInProgress: false,
  reservationSuccess: false,
  reservationError: false,
  studentList: []
}

const getters = {
  getRoomNameOptions: state => {
    const options = state.roomNames.map(room => room.name).map(
      name => ({ 'value': name, 'text': name }))
    const noOptions = [
      {
        'value': null,
        'text': 'No Room Available',
        'disabled': true,
      }]
    return options.length !== 0 ? options : noOptions
  },
}

const mutations = {
  ...cloneDeep(baseMutations),
  setTimeSlots(state, timeSlots) {
    state.timeSlots = timeSlots
  },
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
  setActiveReservation(state, activeReservation) {
    state.activeReservation = activeReservation
  },
  reservationInProgress(state) {
    state.reservationInProgress = true
  },
  reservationSuccess(state) {
    state.reservationSuccess = true
    state.reservationError = false
    state.reservationInProgress = false
  },
  reservationError(state) {
    state.reservationError = true
    state.reservationSuccess = false
    state.reservationInProgress = false
  },
  removeReservation(state, reservationId) {
    state.activeReservation = state.activeReservation.filter(reservation => reservation.reservationId !== reservationId)
  },
  setStudentList(state, studentList) {
    // alert("set")
    // console.log(studentList)
    state.studentList = studentList
  }
}

const actions = {
  initializeState({ commit }) {
    commit('setTimeSlots', generateTimeSlots())
  },
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
      commit('setRoomNames', response.data)
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
  bookForRoom({ commit }, form) {
    commit('reservationInProgress')
    studentService.bookForRoom(form).then(response => {
      commit('reservationSuccess')
    }).catch(err => {
      commit('reservationError')
    })
  },
  fetchActiveReservation({ commit }, studentId) {
    commit('loading')
    studentService.fetchActiveReservation(studentId).then(response => {
      commit('success')
      commit('setActiveReservation', response.data)
    }).catch(err => {
      commit('error', err)
    })
  },
  cancelReservation({commit}, reservationId) {
    commit('loading')
    studentService.cancelReservation(reservationId).then(response => {
      commit('removeReservation', reservationId)
      commit('success')
    }).catch(err => {
      commit('error', err)
    })
  },
  fetchStudentList({commit}) {
    commit('loading')
    studentService.fetchStudentList().then(response => {
      // console.log(response.data)
      commit('setStudentList', response.data)
      commit('success')
    }).catch(err => {
      commit('error', err)
    })
  },
}

function generateTimeSlots() {
  let hrs = 8, state = 0
  let min = ['00', '30']
  const timeSlots = []
  while (hrs !== 16) {
    if (state === 0) {
      timeSlots.push({
        start: `${hrs}:${min[state]}`,
        end: `${hrs}:${min[1 - state]}`,
        available: true,
      })
      state = 1
    } else if (state === 1) {
      timeSlots.push({
        start: `${hrs}:${min[state]}`,
        end: `${hrs + 1}:${min[1 - state]}`,
        available: true,
      })
      hrs += 1
      state = 0
    }
  }
  return timeSlots
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
}