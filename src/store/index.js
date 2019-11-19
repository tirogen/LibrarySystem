import Vue from 'vue'
import Vuex from 'vuex'
import messages from './modules/messages'
import librarian from './modules/librarian'
import room from './modules/room'
import punish from './modules/punish'
import book from './modules/book'
import student from './modules/student'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    messages,
    librarian,
    room,
    punish,
    book,
    student
  }
})
