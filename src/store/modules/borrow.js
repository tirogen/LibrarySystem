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
  borrows: state => {
    return state.borrows
  }
}

const actions = {
  fetchBorrow({ commit }) {
    commit('loading')
    borrowService.fetchBorrow()
      .then(borrows => {
        //alert("got borrow back")
        // console.log(borrows)
        commit('setBorrow', borrows)
        commit('success')
      })
      .catch(err => {
        commit('error', err)
      })
  },
  deleteBorrow({ commit }, id) {
    commit('loading')
    borrowService.deleteBorrow(id).then(data => {
      //delte from local table
      alert(data)
      commit('deleteBorrow', data)
      commit('success')
    }).catch(err => {
      commit('error')
    })
  },
  postBorrow({commit}, obj) 
  {
    alert("add")
    commit('loading')
    borrowService.postBorrow(obj).then(data => {
      //delte from local table
      commit('setBorrow', data)
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
    console.log(borrows)
    state.borrows = borrows
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
