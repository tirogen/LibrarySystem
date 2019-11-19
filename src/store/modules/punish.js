import punishService from '../../services/punishService'
import {cloneDeep} from "lodash";
import {baseState, baseMutations} from "../state";

const state = {
<<<<<<< HEAD
  penalties: []
=======
  ...cloneDeep(baseState),
  penalty: []
>>>>>>> refs/remotes/origin/master
}

const getters = {
  penalties: state => {
    return state.penalties
  }
}

const actions = {
<<<<<<< HEAD
  GetAllPenalties ({ commit }) {
    punishService.fetchAllPenalties()
    .then(penalties => {
      commit('setPenalties', penalties)
=======
  getAllPenalty ({ commit }) {
    punishService.fetchAllPenalty()
    .then(penalty => {
        console.log(penalty);
      commit('setPenalty', penalty)
>>>>>>> refs/remotes/origin/master
    })
  },
}

const mutations = {
<<<<<<< HEAD
  setPenalties (state, penalties) {
    state.penalties = penalties
=======
  ...cloneDeep(baseMutations),
  setPenalty (state, penalty) {
    state.penalty = penalty
>>>>>>> refs/remotes/origin/master
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
