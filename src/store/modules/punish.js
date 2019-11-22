import punishService from '../../services/punishService'

const state = {
  penalties: [],
  punishInfo: {},
  firstname: '',
  lastname: '',
}

const getters = {
}

const actions = {
  getAllPenalties ({ commit }) {
    punishService.fetchAllPenalties()
    .then(penalties => {
      commit('setPenalties', penalties)
    })
  },
  getPunishInfo ({ commit }, data) {
    punishService.fetchPunishInfo(data)
    .then(punishInfo => {
      commit('setPunishInfo', punishInfo)
    })
  },
  deletePenalty({commit}, id) {
    punishService.deletePenalty(id)
    .then(response => {
      commit('deletePenalty', response)
    })
  },
  deletePunish({ commit }, id) {
    punishService.deletePunish(id)
    .then(response => {
      commit('deletePunish', response)
    })
  },
  punishStudent({ commit }, data) {
    punishService.postPunish(data)
    .then(response => {
      commit('setPunishInfoHistory', response.data)
    })
  },
  updatePenalty({ commit }, data) {
    console.log("action")
    punishService.updatePenalty(data)
    .then(response => {
      commit('updatePenalty', response)
    })
  }
}

const mutations = {
  setPenalties (state, penalties) {
    state.penalties = penalties
  },
  setPunishInfo (state, punishInfo) {
    state.punishInfo = punishInfo
  },
  setPunishInfoHistory (state, history) {
    state.punishInfo.histories.push(history)
    state.punishInfo.remainingPoint = state.punishInfo.remainingPoint - history.Point 
  },
  deletePenalty(state, response){
    if(response.status == 200){
      state.penalties = state.penalties.filter((penalty) => penalty.id != response.data.id)
    }
  },
  deletePunish(state, response){
    if(response.status == 200){
      state.punishInfo.histories = state.punishInfo.histories.filter(history => {
        if(history.id == response.data.id){
          state.punishInfo.remainingPoint = state.punishInfo.remainingPoint + history.Point 
        }
        return history.id != response.data.id
      })
    }
  },
  updatePenalty(state, response){
    if(response.status == 200){
      let index = state.penalties.findIndex(penalty => penalty.id == response.data.id);
      state.penalties[index].Name = response.data.Name;
      state.penalties[index].Point = response.data.Point;
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
