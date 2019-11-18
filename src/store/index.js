import Vue from 'vue'
import Vuex from 'vuex'
import messages from './modules/messages'
import librarian from './modules/librarian'
import room from './modules/room'
import punish from './modules/punish'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    messages,
    librarian,
    room,
    punish
  }
})
