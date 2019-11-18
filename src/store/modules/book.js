import bookService from '../../services/bookService'

const state = {
  isLoading: false,
  isSuccess: false,
  isError: false,
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
      commit('error')
    })
  }
}

const mutations = {
  setBooks (state, books) {
    state.books = books
  },
  loading (state){
    state.isLoading = true
  },
  success (state){
    state.isSuccess = true,
    state.isLoading = false
  },
  errors (state) {
    state.isError = true,
    state.isLoading = false
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
