import Vue from 'vue'
import Vuex from 'vuex'
import messages from './modules/messages'
import librarian from './modules/librarian'
import room from './modules/room'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    messages,
    librarian,
    room
  }
})
