import Vue from 'vue'
import Vuex from 'vuex'
import messages from './modules/messages'
import librarian from './modules/librarian'
import room from './modules/room'
import punish from './modules/punish'
import book from './modules/book'
import student from './modules/student'
import borrow from './modules/borrow'
import roomType from './modules/roomType'
import borrowing from './modules/borrowing'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    messages,
    librarian,
    room,
    punish,
    book,
    student,
    borrow,
    roomType
    borrowing
  }
})
