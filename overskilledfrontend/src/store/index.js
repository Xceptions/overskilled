import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    abouts: []
  },
  mutations: {
    SET_ABOUTS ( state, abouts ) {
      state.abouts = abouts
    }
  },
  actions: {
    getPosts ({ commit }) {
      axios.get('http://127.0.0.1:8000/about')
      .then ( response => {
        commit('SET_ABOUTS', response.data)
      } )
    }
  },
  modules: {
  }
})
