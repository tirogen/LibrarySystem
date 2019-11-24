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

  }
  
  const mutations = {
    setBorrows (state, borrows) {
        state.borrows = borrows
      },

  }
  
  export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
  }
  