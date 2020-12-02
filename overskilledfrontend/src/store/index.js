import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    abouts: [],
    howtos: [],
    projects: []
  },
  mutations: {
    SET_ABOUTS (state, abouts) {
      state.abouts = abouts
    },
    SET_HOWTOS (state, howtos) {
      state.howtos = howtos
    },
    SET_PROJECTS (state, projects) {
      state.projects = projects
    }
  },
  actions: {
    getAbouts ({ commit }) {
      axios.get('http://127.0.0.1:8000/about')
        .then(response => {
          commit('SET_ABOUTS', response.data)
        })
    },
    getHowTos ({ commit }) {
      axios.get('http://127.0.0.1:8000/howto')
        .then(response => {
          commit('SET_HOWTOS', response.data)
        })
    },
    getProjects ({ commit }) {
      axios.get('http://127.0.0.1:8000/viewprojects')
        .then(response => {
          commit('SET_PROJECTS', response.data)
        })
    }
  },
  modules: {
  }
})
