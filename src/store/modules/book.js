import bookService from '../../services/bookService'
import {cloneDeep} from "lodash";
import {baseState, baseMutations} from "../state";

const state = {
  ...cloneDeep(baseState),
  books: [],
}

const getters = {
  books: state => {
    return state.books
  }
}

const actions = {
  getBooks ({ commit }) {
    commit('loading')
    bookService.fetchbooks()
    .then(books => {
      commit('setBooks', books)
      commit('success')
    })
    .catch(err => {
      commit('error', err)
    })
  }
}

const mutations = {
  ...cloneDeep(baseMutations),
  setBooks (state, books) {
    state.books = books
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
