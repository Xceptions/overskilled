import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    abouts: [],
    howtos: [],
    projects: [],
    projectdetails: [],
    competitions: []
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
    },
    SET_PROJECTDETAILS (state, projectdetails) {
      state.projectdetails = projectdetails
    },
    SET_COMPETITIONS (state, competitions) {
      state.competitions = competitions
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
    },
    getProjectDetails ({ commit }, payload) {
      axios.get('http://127.0.0.1:8000/projectdetails/' + payload + '/')
        .then(response => {
          commit('SET_PROJECTDETAILS', response.data)
        })
    },
    getCompetitions ({ commit }) {
      axios.get('http://127.0.0.1:8000/viewcompetitions')
        .then(response => {
          commit('SET_COMPETITIONS', response.data)
        })
    }
  },
  modules: {
  }
})
