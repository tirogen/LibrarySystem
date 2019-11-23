import bookService from '../../services/bookService'
import { cloneDeep } from "lodash";
import { baseState, baseMutations } from "../state";
import { strictEqual } from 'assert';

const state = {
  ...cloneDeep(baseState),
  books: [],
  bookdict: {},
  isbns: []
}

const getters = {
  books: state => {
    return state.books
  }
}

const actions = {
  fetchBooks({ commit }) {
    commit('loading')
    bookService.fetchbooks()
      .then(books => {
        // alert("got book back")
        commit('setBooks', books)
        commit('success')
      })
      .catch(err => {
        commit('error', err)
      })
  },
  deleteBooks({ commit }, id) {
    commit('loading')
    bookService.deleteBook(id).then(data => {
      //delte from local table
      commit('deleteBook', data["id"])
      commit('success')
    }).catch(err => {
      commit('error')
    })
  },
  postBooks({ commit }, book) {
    commit('loading')
    bookService.postBook(book).then(books => {
      // post get all book 
      commit('setBooks', books)
      commit('success')
    }).catch(err => {
      commit('error')
    })
  }

}

const mutations = {
  ...cloneDeep(baseMutations),
  setBooks(state, books) {
    // transform books obj to books array 
    state.bookdict = books
    state.isbns = Object.keys(books)
    // console.log(state.isbns)
    state.books = Object.keys(books).map(id => {
      return {
        "isbn" : id,
        "name": books[id]["name"],
        "category" : books[id]["category"],
        "author": books[id]["author"],
        "number": books[id]["number"]
      }
    }
    )
  },
  deleteBook(state, id) {
    state.books = state.books.filter((book) => {
      return book.id != id
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
