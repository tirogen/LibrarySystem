import Vue from 'vue'
import Vuex from 'vuex'
import messages from './modules/messages'
import librarian from './modules/librarian'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    messages,
    librarian
  }
})
