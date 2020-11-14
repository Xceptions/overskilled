import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Post from '../views/Post.vue'
import HowTo from '../views/HowTo.vue'
import Competitions from '../components/Competitions.vue'
import Talks from '../components/Talks.vue'
import Projects from '../components/Projects.vue'
import Jobs from '../components/Jobs.vue'

const routes = [
  {
    path: '/',
    redirect: '/home'
  },
  {
    path: '/home',
    name: 'Home',
    component: Home,
    children: [
      {path: '', component: Projects},
      {path: 'competitions', component: Competitions},
      {path: 'talks', component: Talks},
      {path: 'jobs', component: Jobs}
    ]
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/post',
    name: 'Post',
    component: Post
  },
  {
    path: '/howto',
    name: 'HowTo',
    component: HowTo,
    children: [
      {path: '', component: Projects},
      {path: 'competitions', component: Competitions},
      {path: 'talks', component: Talks},
      {path: 'jobs', component: Jobs}
    ]
  },
  {
    path: '/competitions',
    name: 'Competitions',
    component: Competitions
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
