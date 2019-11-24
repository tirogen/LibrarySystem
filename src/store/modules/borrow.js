import bookService from '../../services/bookService'
import { cloneDeep } from "lodash";
import { baseState, baseMutations } from "../state";
import { strictEqual } from 'assert';
import borrowService from '../../services/borrowService';

const state = {
  ...cloneDeep(baseState),
  borrows: []
}

const getters = {
  books: state => {
    return state.books
  }
}

const actions = {
  fetchBorrow({ commit }) {
    commit('loading')
    borrowService.fetchBorrow()
      .then(books => {
        // alert("got book back")
        commit('setBorrow', books)
        commit('success')
      })
      .catch(err => {
        commit('error', err)
      })
  },
  deleteBorrow({ commit }, id) {
    commit('loading')
    borrowService.deleteBorow(id).then(data => {
      //delte from local table
      commit('deleteBorrow', data)
      commit('success')
    }).catch(err => {
      commit('error')
    })
  }

}

const mutations = {
  ...cloneDeep(baseMutations),
  setBorrow(state, borrows) {
    // transform books obj to books array 
      state.borrows = borrows
    )
  },
  deleteBorrow(state, data) {
    state.borrows = state.borrows.filter((borrow) => {
      if(borrow.borrowID == data["borrowID"]) {
        return false
      }
      return true
    })
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
