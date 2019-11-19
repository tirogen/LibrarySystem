import studentService from "../../services/studentService";
import {cloneDeep} from 'lodash'
import {baseState, baseMutations} from "../state";

const state = {
  ...cloneDeep(baseState),
  reservedRooms: [],
}

const getters = {}

const mutations = {
  ...cloneDeep(baseMutations),
  setReservedRooms(state, reservedRooms) {
    state.reservedRooms = reservedRooms
  }
}

const actions = {
  fetchReservedRooms({commit}) {
    commit('loading')
    studentService.fetchReservedRooms()
      .then(response => {
          commit('setReservedRooms', response)
        }
      )
      .catch(err => {
        commit('error', err)
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