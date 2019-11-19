import bookService from '../../services/bookService'
import {cloneDeep} from "lodash";
import {baseState, baseMutation} from "../state";

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
  ...cloneDeep(baseMutation),
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
