import punishService from '../../services/punishService'
import {cloneDeep} from "lodash";
import {baseState, baseMutation} from "../state";

const state = {
  ...cloneDeep(baseState),
  penalty: []
}

const getters = {
  penalty: state => {
    return state.penalty
  }
}

const actions = {
  getAllPenalty ({ commit }) {
    punishService.fetchAllPenalty()
    .then(penalty => {
        console.log(penalty);
      commit('setPenalty', penalty)
    })
  },
}

const mutations = {
  ...cloneDeep(baseMutation),
  setPenalty (state, penalty) {
    state.penalty = penalty
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
