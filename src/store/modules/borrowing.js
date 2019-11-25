import studentService from '../../services/studentService'

const state = {
    borrows: [],
  }
  
  const getters = {
  }
  
  const actions = {
    getBorrow ({ commit }, id) {
        studentService.fetchBorrowingBook(id)
        .then(borrows => {
          commit('setBorrows', borrows.data)
        })
      },  
      updateRenewTime({ commit }, data) {
        studentService.updateRenewTime(data)
        .then(response => {
          commit('updateRenewTime', response)
        })
      },

  }
  
  const mutations = {
      setBorrows (state, borrows) {
        state.borrows = borrows
      },
      updateRenewTime(state, response){
        if(response.status == 200){
          let index = state.borrows.findIndex(borrow => borrow.id == response.data.id);
          state.borrows[index].EndDate = response.data.EndDate;
          state.borrows[index].RenewTimes = response.data.RenewTimes;
          state.borrows[index].id = response.data.id;
        }
      },

  }
  
  export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
  }
  